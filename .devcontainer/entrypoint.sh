#!/bin/bash
set -euo pipefail

export HISTFILE=/commandhistory/.bash_history
export HISTSIZE=100000
export HISTFILESIZE=200000
shopt -s histappend
PROMPT_COMMAND="history -a; history -n"

sleep infinity


