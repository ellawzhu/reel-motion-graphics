# reel-motion-graphics

A Claude Code skill that adds Instagram-reel-style motion graphics and sound design to a talking-head video. Every graphic is bilingual EN + 中文, rendered with [HyperFrames](https://hyperframes.dev).

Three aesthetics:

- **Green oasis** (default): forest-green editorial cards, giant serif titles behind the speaker's head, mock app UI, punchy SFX.
- **Neutral colors**: soft beige, white iOS cards, gold italic keywords, sparkles, butter-yellow circle wipes, sparse "ting" sounds.
- **Classic calligraphy**: script title lockup, handwritten notebook inserts, slow fades, a soft music bed.

## Install

In Claude Code:

```
/plugin marketplace add <your-github-username>/reel-motion-graphics
/plugin install reel-motion-graphics@reel-motion-graphics
```

Or copy `skills/reel-motion-graphics/` into `~/.claude/skills/`.

## Requirements

- HyperFrames CLI (`npx hyperframes`) and Node
- `uv` (Python: rembg, onnxruntime, scipy, numpy, soundfile, Pillow) and `ffmpeg`

## Setup notes

- `scripts/prep.sh` sets `KIT` to my HyperFrames workspace (`/Volumes/G-DRIVE ArmorATD/hyperframes-student-kit`). Change it to yours.
- Sound effects are not included. Download the Pixabay sounds listed in `assets/sfx/CREDITS.md` into `assets/sfx/`.
- Reference-reel stills are not included; only my own demo renders are.
