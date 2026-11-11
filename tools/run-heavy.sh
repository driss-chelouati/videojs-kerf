#!/bin/bash
# Runs a Playwright step behind the shared heavy lock. usage: run-heavy.sh <step> <script.py> [args...]
STEP=$1; shift
export LD_LIBRARY_PATH="$HOME/.cache/orvio-chromium-libs/usr/lib/x86_64-linux-gnu${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
LOCK="node $HOME/projects/orvio/plugins/orvio-daily/tools/heavy-lock.mjs"
for i in $(seq 1 20); do
  if $LOCK acquire --slug kerf --step "$STEP" --wait 540 2>/dev/null; then
    python3 "$@"; rc=$?; $LOCK release --slug kerf --step "$STEP"; exit $rc
  fi
done
echo "heavy lock not acquired"; exit 1
