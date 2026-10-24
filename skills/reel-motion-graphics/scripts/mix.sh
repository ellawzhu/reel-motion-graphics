#!/usr/bin/env bash
# mix.sh <project-dir> <render.mp4> <out.mp4>
# Lays sfx-mix.wav under the rendered video's voice and normalizes to -14 LUFS / -1.5 dBTP
# (Reels / 小红书 / TikTok level; her raw recordings sit near -23 LUFS). Video is copied, not re-encoded,
# so re-balancing sound never needs a re-render.
set -euo pipefail
P="$1"; IN="$2"; OUT="$3"
ffmpeg -v error -y -i "$IN" -i "$P/public/assets/sfx-mix.wav" -filter_complex \
  "[0:a]aresample=48000[v];[v][1:a]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 256k -movflags +faststart "$OUT"
ffmpeg -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:)"
