#!/bin/bash
# Re-encodes the Sparvek film for the workbench (the MP4s are not committed; Mux hosts the film once Driss uploads it).
set -e
P="$(dirname "$0")/../skin/apps/preview/public/media"; V=/home/driss/reels/sparvek/out
ffmpeg -v error -y -i $V/169/sparvek-reel-169.mp4 -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$P/sparvek-169.mp4"
ffmpeg -v error -y -i $V/916/sparvek-reel-916.mp4 -vf scale=1080:-2 -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$P/sparvek-916.mp4"
