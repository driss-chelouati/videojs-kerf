#!/bin/bash
# Runs a render behind the shared heavy lock. usage: shoot.sh <step> <python args...>
STEP=$1; shift
export LD_LIBRARY_PATH="$HOME/.cache/orvio-chromium-libs/usr/lib/x86_64-linux-gnu${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
LOCK="node $HOME/projects/orvio/plugins/orvio-daily/tools/heavy-lock.mjs"
$LOCK acquire --slug kerf --step "$STEP" --wait 540 && { python3 "$HOME/projects/videojs-kerf/tools/shoot.py" "$@"; rc=$?; $LOCK release --slug kerf --step "$STEP"; exit $rc; }
