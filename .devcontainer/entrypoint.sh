#!/bin/bash
set -euo pipefail

# ------------------------------------------------------------
# Create test veth interfaces (optional)
# ------------------------------------------------------------
# Create test veth interfaces (only if permitted)
if ip link add veth1.1 type veth peer name veth1.2 2>/dev/null; then
    ip link set veth1.1 up
    ip link set veth1.2 up

    # ip addr flush dev veth1.1
    # ip addr flush dev veth1.2
    # ip -6 addr flush dev veth1.1
    # ip -6 addr flush dev veth1.2

    echo "[entrypoint] veth interfaces ready"
else
    echo "[entrypoint] WARNING: cannot create veth interfaces (missing NET_ADMIN?)"
fi


# ------------------------------------------------------------
# Persistent bash history
# ------------------------------------------------------------
export HISTFILE=/commandhistory/.bash_history
export HISTSIZE=100000
export HISTFILESIZE=200000
shopt -s histappend
PROMPT_COMMAND="history -a; history -n"

# ------------------------------------------------------------
# Start bngblaster controller (port 4711)
# ------------------------------------------------------------
BNG_CTRL_BIN="/usr/local/bin/bngblasterctrl"
BNG_CTRL_PORT="4711"
BNG_CTRL_LOGFILE="/tmp/bngblasterctrl.log"

BNG_CTRL_PID=""

if [ -x "$BNG_CTRL_BIN" ]; then
  echo "[entrypoint] Starting bngblaster controller on :${BNG_CTRL_PORT} ..."
  "$BNG_CTRL_BIN" -addr ":${BNG_CTRL_PORT}" >"$BNG_CTRL_LOGFILE" 2>&1 &
  BNG_CTRL_PID="$!"
else
  echo "[entrypoint] WARNING: bngblaster controller binary not found at $BNG_CTRL_BIN"
fi

# ------------------------------------------------------------
# Start Reflex WUI (dev mode) on frontend/back-end ports only
#   Frontend: 4712
#   Backend : 4713
# ------------------------------------------------------------
REFLEX_APP_DIR="/workspaces/Bng-Blaster-Controller-WUI"
REFLEX_LOGFILE="/tmp/reflex.log"
REFLEX_PID=""

# Use explicit ports so they don't collide with controller
export REFLEX_FRONTEND_PORT="4712"
export REFLEX_BACKEND_PORT="4713"
export API_URL="http://127.0.0.1:${REFLEX_BACKEND_PORT}"  # optional, handy

if command -v reflex >/dev/null 2>&1; then
  if [ -d "$REFLEX_APP_DIR" ]; then
    cd "$REFLEX_APP_DIR"

    # If the app hasn't been initialized yet, don't fail hard.
    # (You'll see it in the log and can run `reflex init` once.)
    echo "[entrypoint] Starting Reflex dev server (frontend:${REFLEX_FRONTEND_PORT} backend:${REFLEX_BACKEND_PORT}) ..."
    reflex run --env dev --frontend-port "${REFLEX_FRONTEND_PORT}" --backend-port "${REFLEX_BACKEND_PORT}" \
      >"$REFLEX_LOGFILE" 2>&1 &
    REFLEX_PID="$!"
  else
    echo "[entrypoint] WARNING: Reflex app dir not found: $REFLEX_APP_DIR"
  fi
else
  echo "[entrypoint] WARNING: reflex not installed (pip install reflex)"
fi

# ------------------------------------------------------------
# Graceful shutdown
# ------------------------------------------------------------
term_handler() {
  echo "[entrypoint] Caught termination signal"

  if [ -n "${REFLEX_PID}" ] && kill -0 "${REFLEX_PID}" 2>/dev/null; then
    echo "[entrypoint] Stopping Reflex (PID ${REFLEX_PID})"
    kill "${REFLEX_PID}" || true
    wait "${REFLEX_PID}" || true
  fi

  if [ -n "${BNG_CTRL_PID}" ] && kill -0 "${BNG_CTRL_PID}" 2>/dev/null; then
    echo "[entrypoint] Stopping bngblaster controller (PID ${BNG_CTRL_PID})"
    kill "${BNG_CTRL_PID}" || true
    wait "${BNG_CTRL_PID}" || true
  fi

  exit 0
}

trap term_handler SIGTERM SIGINT

# ------------------------------------------------------------
# Keep container alive (and forward signals)
# ------------------------------------------------------------
sleep infinity &
wait $!
