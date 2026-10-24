# Aesthetic: NEUTRAL COLORS

Reference reel: `~/Downloads/igexport-Det1_bgydPz.mp4` (85 s, "My Claude Edits System", 5 steps).
Stills: `assets/stills/neutral-colors/` (key-frames, contact-sheet, sound-moments, our-demo).
Theme CSS: `assets/themes/neutral-colors.css` · set `THEME = 'neutral-colors'` in cards.py.
Starter: `references/example-neutral/` (cards.py, cards.js, cues.py).

## The feel
Soft, airy, warm-beige, "Apple Notes" creator look. Nothing heavy sits on the footage: no dark panels, no
saturated colour blocks. Graphics feel like light stickers and phone screenshots resting on a sunny room.
Calm pace: roughly one graphic every 5-8 s, and long stretches of plain talking-head.

## Visual vocabulary (what's in the reel → class to use)
| In the reel | Use |
|---|---|
| Opening lockup "My *Claude Edits* / S Y S T E M": white serif + gold italic serif word, wide-tracked caps under | `.n-title` (`.big` with `<em>`, `.caps`, `.zh`) |
| Yellow sticker "5 Steps → No Course", bold black sans, tilted | `.n-pill` |
| Section header "Step 1: *Claude Code*" with ✦ ✦ sparkles twinkling above | `.sparkles` + `.n-step` · `twinkle()` |
| Keyword in captions/kickers set in gold italic serif ("Go to *Claude* Code") | `.n-kick` with `<em>` |
| White iOS cards: comments ("Add a comment…"), follow card, "The Only 3 Tools" list | `.n-card`, `.n-row`, `.n-input` |
| Cream document windows (traffic-light bar): "Video Style Menu", Notes | `.n-doc` (`.bar`, `.body`, `h3`) |
| Fan of her past thumbnails/screenshots floating around her | `.n-thumb` with her real images; ask her for them |
| Book cover sticker top-right ("Steal Like an Artist") | an `<img>` in `.n-thumb`-like frame, slight tilt |
| Butter-yellow circle wipe between sections, sometimes collapsing onto her face | `.n-iris` · `iris()` |
| Black interlude card "Raw *Clip* → Option *A·B·C*" | `.n-dark` + `.lab` |
| Full-frame screen recordings with a soft warm fade top and bottom | she supplies the recording; place it as a card or full frame |

Palette: white `#fff` text with soft shadow · gold italic `#f1d77a` · butter yellow `#f2df78` · cream `#f7f2e8` ·
ink `#1d1d1f`. Fonts: Instrument Serif (italic for keywords), Inter Tight; 中文 in Noto Serif SC for titles,
Noto Sans SC in cards.

Motion: `floatIn()` (fade + 30 px rise, power3, **no overshoot**). Sparkles twinkle. Cards slide up from the
bottom. One iris wipe per section change. Never the green-oasis `back.out` bounces.

Layout: titles in the top band; cards/stickers in the lower half over her body (left 120, width ~760) and
clear of the right-side rail. Fine to sit beside her head on the sides; the reel does.

## Sound (measured)
No music at all. About 13 sounds in 85 s, only on transitions and big arrivals, never under ordinary talking:
- bright short "ting" (~3 kHz, 0.2-0.3 s) when the yellow wipe opens/closes and when a sticker/book drops in → `sparkle` / `ping`
- one low soft thud for the thumbnail-collage arrival → `impact-bass-1` at ×0.5
- small clicks for UI cards → `click-soft`
Level: tings ~16 dB under voice peaks; the thud ~4 dB under. See `example-neutral/cues.py`.

## Needs from Ella before building
Her thumbnails / screenshots / book covers / screen recordings if the video references them; the reel's
look depends on real images. Without them, use `.n-card` / `.n-doc` text versions.
