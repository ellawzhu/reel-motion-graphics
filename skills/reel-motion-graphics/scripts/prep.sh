#!/usr/bin/env bash
# prep.sh <source-video> <project-slug>
# Creates hyperframes-student-kit/video-projects/<slug>/ with a 1080x1920/30fps proxy
# (dense GOP so the renderer can seek), audio.mp3, the embedded subtitle track if
# any (source.srt), and a word-level whisper transcript (transcript.json).
set -euo pipefail
SRC="$1"; SLUG="$2"
KIT="/Volumes/G-DRIVE ArmorATD/hyperframes-student-kit"
SKILL="$(cd "$(dirname "$0")/.." && pwd)"
P="$KIT/video-projects/$SLUG"
mkdir -p "$P/public/assets/sfx" "$P/scripts" "$P/renders"
cd "$P"
cp -n "$KIT/video-projects/may-shorts-19/hyperframes.json" . 2>/dev/null || true
cp -n hyperframes.json public/ 2>/dev/null || true
cp -n "$SKILL/assets/sfx/"*.mp3 "$SKILL/assets/sfx/CREDITS.md" public/assets/sfx/

ffmpeg -v error -y -i "$SRC" -vn -acodec libmp3lame -q:a 2 audio.mp3
cp audio.mp3 public/assets/audio.mp3
# portrait sources are 2160x3840 (sometimes via a rotation flag); scale handles both
ffmpeg -v error -y -i "$SRC" -map 0:v:0 -map 0:a:0 -vf "scale=1080:1920:flags=lanczos,fps=30" \
  -c:v h264_videotoolbox -b:v 12M -g 30 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart \
  public/assets/input-video.mp4
if ffprobe -v error -select_streams s -show_entries stream=index -of csv=p=0 "$SRC" | grep -q .; then
  ffmpeg -v error -y -i "$SRC" -map 0:s:0 source.srt && echo "embedded subtitles -> source.srt"
fi
# the CLI also prints a summary to stdout: keep it out of transcript.json
npx hyperframes transcribe audio.mp3 -d . --json --model small.en > transcribe-summary.json 2> transcribe.log
python3 -c "import json;d=json.load(open('transcript.json'));print(len(d),'words, ends',d[-1]['end'])"
ffprobe -v error -show_entries format=duration -of csv=p=0 public/assets/input-video.mp4
echo "project: $P"
