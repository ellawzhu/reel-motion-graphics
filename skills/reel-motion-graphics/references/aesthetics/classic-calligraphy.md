# Aesthetic: CLASSIC CALLIGRAPHY

Reference reel: `~/Downloads/igexport-Derd9IvoWaj.mp4` (68 s, "Think Like An Editor — Part One").
Stills: `assets/stills/classic-calligraphy/` (key-frames, contact-sheet, our-demo).
Theme CSS: `assets/themes/classic-calligraphy.css` · set `THEME = 'classic-calligraphy'` in cards.py.
Starter: `references/example-calligraphy/` (cards.py, cards.js, cues.py).

## The feel
Quiet, editorial, old-money desk: bookshelves, a podcast mic, a walnut desk, a fountain pen. The reel's whole
argument is *against* overstimulating edits, so restraint IS the aesthetic. There are only two kinds of
graphic:
1. **One script title lockup** over the footage at the start: "THINK LIKE / *An Editor* / PART ONE": thin
   tracked serif caps around a big white calligraphic script word. Small, white, no box.
2. **Handwritten notebook inserts**: in the reel these are real overhead shots of her hand writing in a spiral
   notebook ("AI Edits: – overstimulating graphics – constant transitions", "Fast-paced ≠ Reach",
   "Questions to ask: 1. Am I being sold something? 2. How can I differentiate?", "Follow for Part Two").
   We recreate them as a full-frame cutaway: walnut desk + open lined notebook, text written on line by line.

Captions in the reel are tiny white sans at mid-frame; Ella burns her own subtitles, so skip them.

## Visual vocabulary → class
| In the reel | Use |
|---|---|
| THINK LIKE / *An Editor* / PART ONE | `.c-lockup` (`.caps`, `.script`, `.caps`, `.zh` in Ma Shan Zheng brush font) |
| Overhead notebook, pen writing a list | `.c-desk` + `.c-book` > `.c-page` / `.c-spiral` / `.c-page`, lines are `.c-hand` (EN, Kalam) and `.c-hand.zh` (Long Cang) · `writeOn()` |
| Big two-word spread ("Think Like an Editor" / "Part One") | `.c-hand.big` on each page |
| "≠" or a crossed-out word | `.c-strike` (scaleX 0 → 1) or write the ≠ as text |
| An occasional quiet pull-quote over footage | `.c-note` (Cormorant italic + 中文) |
| Small lower-third in the same voice | `.c-lower` |

Palette: warm white `#fbf8f2` · paper `#f6f1df` with faint blue rules · marker ink `#1a1a1a` · one red accent
`#b3261e` used at most once or twice · walnut `#4a2a1a`. Fonts: Pinyon Script (script), Cormorant Garamond
(caps/italic), Kalam (handwriting); 中文: Ma Shan Zheng (brush title), Long Cang (handwriting), Noto Serif SC.

Motion: `softIn()` / `softOut()` (slow fades, no movement) and `writeOn()` at ~11 characters/s, the pace of
the pen in the reel. No pops, no bounces, no whooshing cards, no count-ups. Notebook inserts are cutaways
(they cover her completely), so use them for lists, key contrasts and the closing line. Roughly 4-6 per
minute of the reel's 68 s; for a long video, one per section is plenty.

## Sound (measured)
**No sound effects at all.** One continuous soft music bed (~123 BPM) sits about 6 dB under the voice
for the whole video, with no ducking tricks or hits. Music needs a source decision from Ella before building:
her own track, local MusicGen generation, or none (voice only). `cues.py` stays empty.
If she wants pen sounds on the notebook inserts, that's an addition beyond the reference; ask first.
