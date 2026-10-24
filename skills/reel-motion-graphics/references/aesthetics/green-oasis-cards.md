# Card catalog

Every graphic type built so far, where its full markup lives in `example-affiliate/cards.py` (look up the card id),
its timeline code in `example-affiliate/cards.js`, and its sound in `example-affiliate/cues.py`. Copy the closest one
and rewrite its words. Pick a card for **what is being said**, not for variety: a list when she enumerates, a number
hero when a number is the point, a mock UI when she describes tapping through an app.

## Contents
1. Hero titles (behind her head)
2. Information cards
3. Mock app UI
4. Small accents
5. Layout zones and sizing
6. Bilingual rules

## 1. Hero titles — giant serif type behind the speaker
Use for the 3-5 biggest moments of a video: the opening, the headline offer, the key number, the punchline.
More than ~5 and they stop feeling big. Each needs a cut-out window in `FG` (scripts/matte.py), covering
the hero's on-screen time plus ~0.3 s either side.

| id in example | Shape | Sound |
|---|---|---|
| `intro` | green full-bleed cold open (`.greenbg` wipes up via clip-path), `hero-zh` + `hero-word` + `hero-ital` | `impact-bass-1` on land, `whoosh` (peak) on the wipe |
| `cover` | magazine cover: `.mast` (two corner labels), `.rule`, giant word, italic gold subword, `.barcode` | `impact-bass-2` on land, `pop` on the italic |
| `p30` | number hero: count-up `0→30` in `#p30V`, italic `commission <u class="zh hz-gold">佣金</u>` inline | `riser` (align `end`) + 8 `key-press` ticks during the count + `impact-bass-2` on land |
| `five` | mast + `hero-zh` line + `hero-word huge sm` + italic | `impact-bass-1`, `sparkle` |
| `wins` | `hero-zh` above, word, italic | `impact-bass-2`, `sparkle` |

Hero class is `hero` (z 3, under the cut-out at z 4). Vertical stack that clears her head (head top ≈ y 560-700
at 1080×1920 in her usual framing): mast y 120 → `hero-zh` y 160-170 → `hero-word` y 190-250 → `hero-ital` y 420-520.
Some overlap of the italic line with her hair is the look; the word itself must stay readable.

## 2. Information cards — forest-green panels in the top band
| id | Use when she… | Build-up |
|---|---|---|
| `course` | names a product/course | card + thumb rotate in, pill pops |
| `who`, `slot`, `rednote` | lists conditions/steps (checklist) | `grow()` each `row()` on its phrase, tick scales in |
| `why` | gives numbered reasons | `grow()` rows with `<b class="num">01</b>` leads |
| `stores` | contrasts old vs new | two `.store` cards; red `.strike` slashes the old one |
| `refund` | explains a sequence/flow | `.node` → `.arr` (scaleX) → `.node`, then an `.eq` line |
| `deadline` | gives a date/time limit | big date + `.track/.fill` bar scaling to the % elapsed |
| `clock` | mentions limited time | `.digits` counting down via onUpdate |
| `acclaim` | mentions reviews / good feedback / testimonials | 5 stars, then REAL review cards (`REVIEWS` in cards.py) drop onto a `.pile` one per ~1.25 s; the covered card's text fades so only its edge shows; all `.rev` cards share one height |
| `simple`, `incent`, `giveback`, `top5` | says a quotable line | `center-block` serif display/quote + Caveat `.hand` aside |

Rows must use `grow()`, not `pop()`: hidden rows otherwise still take space and the card shows an empty block.

## 3. Mock app UI (reference reel 1's signature)
| id | What | Sound |
|---|---|---|
| `genesis`, `end` | chat/comment bar typing (`type()` + `blink()` caret), 中文 typed on a second line | `typing` per line |
| `howto` | phone: store grid → product detail slides in → icon tap → bottom sheet → toast, with `.cursor` moves and a numbered `.steps` rail | `click` per tap, `whoosh-short` per slide, `notification` on the toast |
| `follow` | Follow pill, cursor taps, button flips to "Following ✓ · 已关注" | `click` + `ping` |
| `group` | group chat, bubbles `grow()` in left/right | `pop` per bubble |
| `share` | row of pill chips (EN over 中文) | `pop` per chip |
| `live` | red LIVE pill pulsing | `ping` |

**Testimonials must be real.** Ella supplies screenshots of her students' messages. Quote a short verbatim line
from each (pick the most specific benefit: detailed feedback, studying together, speaking more naturally),
add an English gloss, and label it with cohort + the display name shown (第三期学员 · April). Never write or paraphrase
a review yourself. If she gives none, show stars only.

## 4. Small accents
`friends` (avatar dots multiplying around "Ella"), `stars` (5 stars staggered 0.09 s), `.hand` Caveat asides.

## 5. Layout zones and sizing (1080×1920)
- **Top band y 80-560** is where every non-hero card lives: ceiling/background, clear of her face.
- Cards are `left:60 width:960` (`.gcard`) or centred; keep the bottom edge above ~600 or it covers her face.
- Nothing in the lower half: that's her face, hands and the platform UI (caption area, right-side like/comment rail).
- Chip rows: three chips max per row at 68 px, or they run off the edges.
- Buttons and pills: add `white-space: nowrap` once 中文 is appended, or they wrap mid-word.

## 6. Bilingual rules
Every piece of English on screen gets its 中文: a `zh()` line under it (cards, rows, bubbles, nodes, chips),
` · 中文` appended inline in kickers/mast/pills, or a `hero-zh` line above a hero title. Use the 小红书 terms
her audience uses: posts → 笔记, affiliate → 带货 / 带货推广, commission → 佣金, follow → 关注, group chat → 群聊, live → 直播.
Typed text gets its 中文 typed after it (second `type()` call ~1.7 s later, slower cps).
