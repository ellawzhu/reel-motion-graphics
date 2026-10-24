# Sound design

## What the reference reels do (measured, voice separated out with demucs)
- **Reel 1 (green editorial):** sparse. Deep low booms (~300 Hz centroid, ~2 s tail) when hero titles land,
  ~6 dB above voice peaks; tiny UI clicks/pops 15-18 dB under voice; a typing tick burst while text types;
  a riser into a reveal; a music swell only for the outro.
- **Reel 2 (word-pop captions):** a continuous ~117 BPM music bed ~7 dB under the voice plus frequent short hits.

Ella chose **SFX only, no music bed** (2026-10-20). Ask before adding music; if she wants it, the options are
local MusicGen generation, a track she supplies, or HeyGen's catalog (needs the heygen CLI and sign-in).

## Cue grammar — one sound per visual event
| Visual event | Sound | align |
|---|---|---|
| hero title lands | `impact-bass-1` / `impact-bass-2` | onset |
| number counts up | `key-press` × 6-8 at ~0.11 s spacing | onset |
| big number lands | `riser` | **end** (so it crests on the hit) |
| card slides/rises in | `whoosh-short` (×0.6-1.0) | onset |
| full-screen wipe | `whoosh` | peak |
| chip / row / bubble / star pops | `pop` (×0.5-0.8; quieter when several fire close together) | onset |
| checkmark ticks in | `click-soft` 0.25 s after its row | onset |
| cursor tap | `click` | onset |
| text types | `typing` (1.5 s burst; one per typed line) | onset |
| toast / message arrives | `notification` | onset |
| success (followed, refunded, qualified) | `ping` or `chime` | onset |
| a highlight shimmer on a hero | `sparkle` | onset |
| something crossed out / wrong | `error` (×0.6) | onset |
| clock counting | `key-press` once per second | onset |

Don't add sounds for exits; the reels don't, and it gets busy. Time each cue off the SAME `T[...] + offset`
expression its animation uses in cards.js, so picture and sound can't drift apart.

## Levels
Her raw voice: ~-23 LUFS integrated, short-term (50 ms) peaks near -18 dBFS. The `GAIN` table in
scripts/sfx.py is set against that. Loudness targets after mixing: `mix.sh` normalizes to **-14 LUFS, -1.5 dBTP**.

Verify after mixing, don't assume:
- Bass hits should land within ~0.05 s of their title: low-pass the final mix at 120 Hz and find the 50 ms-RMS
  peak in a ±1 s window around each hero time.
- Median SFX-vs-voice (where both are active) should sit around -13 to -16 dB.

## Library quirks (bundled Pixabay files, free for commercial use, no credit needed)
- `impact-bass-1/2` are ~2 s SUSTAINED near-0 dBFS drones, not hits. sfx.py shapes them with an exponential
  decay (τ 0.45 s); aligning `impact-bass-2` by its sample peak lands it ~0.8 s late, so align by onset.
- `riser` is 10 s; its loudest sample is NOT at the end, so use `align='end'`.
- `whoosh` and `whoosh-short` are the same file; `click` and `click-soft` too. Vary with gain, not file.
