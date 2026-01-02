FROM mcr.microsoft.com/devcontainers/base:ubuntu

# ------------------------------------------------------------
# Base packages
# ------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    python3 \
    python3-pip \
    tcpdump \
    wget \
    unzip \
    build-essential \
    pkg-config \
    cmake \
    libpcap-dev \
    libcunit1-dev \
    libncurses5-dev \
    libssl-dev \
    libjansson-dev \
    libnuma-dev \
    golang-go \
 && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------
# Persistent bash history (root + vscode)
# ------------------------------------------------------------
RUN mkdir -p /commandhistory \
 && chmod 777 /commandhistory \
 && touch /commandhistory/.bash_history \
 && chmod 666 /commandhistory/.bash_history \
 && printf '\n# Persistent bash history (devcontainer)\nexport HISTFILE=/commandhistory/.bash_history\nexport HISTSIZE=100000\nexport HISTFILESIZE=200000\nshopt -s histappend\nPROMPT_COMMAND="history -a; history -n; $PROMPT_COMMAND"\n' \
    >> /etc/bash.bashrc

# ------------------------------------------------------------
# Python dependencies
# ------------------------------------------------------------
COPY requirements.devcontainer /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt --break-system-packages

# ------------------------------------------------------------
# libdict
#  - amd64: install .deb
#  - arm64: build from source
# ------------------------------------------------------------
RUN set -eux; \
    ARCH="$(dpkg --print-architecture)"; \
    if [ "$ARCH" = "amd64" ]; then \
        cd /tmp; \
        wget -q https://github.com/rtbrick/libdict/releases/download/1.0.5/libdict-ubuntu-22.04.zip; \
        unzip -q libdict-ubuntu-22.04.zip; \
        dpkg -i libdict_1.0.5_amd64.deb libdict-dev_1.0.5_amd64.deb; \
        rm -f libdict-ubuntu-22.04.zip; \
    elif [ "$ARCH" = "arm64" ]; then \
        git clone --depth 1 --branch 1.0.5 https://github.com/rtbrick/libdict.git /tmp/libdict; \
        cmake -S /tmp/libdict -B /tmp/libdict/build -DCMAKE_BUILD_TYPE=Release; \
        cmake --build /tmp/libdict/build -j"$(nproc)"; \
        cmake --install /tmp/libdict/build; \
        ldconfig; \
        rm -rf /tmp/libdict; \
    else \
        echo "Unsupported architecture: $ARCH" >&2; exit 1; \
    fi

# ------------------------------------------------------------
# Clone & build bngblaster (native arch)
# ------------------------------------------------------------
RUN set -eux; \
    git clone https://github.com/rtbrick/bngblaster.git /opt/bngblaster; \
    cmake -S /opt/bngblaster -B /opt/bngblaster/build -DCMAKE_BUILD_TYPE=RelWithDebInfo; \
    cmake --build /opt/bngblaster/build -j"$(nproc)"; \
    cmake --install /opt/bngblaster/build; \
    ldconfig

# ------------------------------------------------------------
# bngblaster-controller
#  - amd64: install .deb
#  - arm64: build from release source tarball (auto-detect main)
# ------------------------------------------------------------
ARG BNG_CONTROLLER_VERSION=0.1.3

RUN set -eux; \
    ARCH="$(dpkg --print-architecture)"; \
    if [ "$ARCH" = "amd64" ]; then \
        cd /tmp; \
        wget -q https://github.com/rtbrick/bngblaster-controller/releases/download/v${BNG_CONTROLLER_VERSION}/bngblaster-controller_${BNG_CONTROLLER_VERSION}_amd64.deb; \
        dpkg -i bngblaster-controller_${BNG_CONTROLLER_VERSION}_amd64.deb; \
        rm -f bngblaster-controller_${BNG_CONTROLLER_VERSION}_amd64.deb; \
    elif [ "$ARCH" = "arm64" ]; then \
        cd /tmp; \
        wget -q https://github.com/rtbrick/bngblaster-controller/archive/refs/tags/v${BNG_CONTROLLER_VERSION}.tar.gz \
        -O bngblaster-controller.tar.gz \
        || wget -q https://github.com/rtbrick/bngblaster-controller/archive/refs/tags/${BNG_CONTROLLER_VERSION}.tar.gz \
        -O bngblaster-controller.tar.gz; \
        rm -rf /tmp/bngblaster-controller-src; \
        mkdir -p /tmp/bngblaster-controller-src; \
        tar -xzf /tmp/bngblaster-controller.tar.gz -C /tmp/bngblaster-controller-src --strip-components=1; \
        cd /tmp/bngblaster-controller-src; \
        \
        # 1) Prefer known cmd path if present
        if [ -d "./cmd/bngblasterctrl" ]; then \
            go build -o /usr/local/bin/bngblasterctrl ./cmd/bngblasterctrl; \
        else \
            # 2) Fallback: find first cmd/* directory containing "package main"
            MAIN_DIR="$(grep -Rsl --include='*.go' '^package main' ./cmd 2>/dev/null | head -n 1 | xargs -r dirname)"; \
            test -n "$MAIN_DIR"; \
            go build -o /usr/local/bin/bngblasterctrl "$MAIN_DIR"; \
        fi; \
        chmod 0755 /usr/local/bin/bngblasterctrl; \
        ln -sf /usr/local/bin/bngblasterctrl /usr/local/bin/bngblaster-controller; \
        rm -rf /tmp/bngblaster-controller-src /tmp/bngblaster-controller.tar.gz; \
    else \
        echo "Unsupported architecture: $ARCH" >&2; exit 1; \
    fi



# ------------------------------------------------------------
# Entrypoint
# ------------------------------------------------------------
COPY .devcontainer/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["sleep", "infinity"]
