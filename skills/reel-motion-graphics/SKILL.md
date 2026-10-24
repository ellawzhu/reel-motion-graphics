---
name: reel-motion-graphics
description: Ella's Instagram-reel-style motion graphics + sound design for her talking-head videos, in one of three named aesthetics — GREEN OASIS (forest-green editorial cards, giant serif titles behind her head, mock app UI, punchy SFX), NEUTRAL COLORS (soft beige, white iOS cards, gold italic keywords, sparkles, butter-yellow circle wipes, sparse "ting" sounds) or CLASSIC CALLIGRAPHY (script title lockup, handwritten notebook inserts, slow fades, soft music bed) — every graphic bilingual EN + 中文, rendered with HyperFrames. Use this whenever Ella wants motion graphics, "animations", on-screen graphics, "make it look like this reel", "green oasis", "neutral", "calligraphy", "add the green cards", "text behind my head", "handwritten notes", a course/program announcement or promo dressed up, or wants sound effects / sound design added to one of her videos — even if she just drops a talking-head video plus a reference reel and says "do this to mine". Not for plain burned subtitles (caption-burn workflow) or 小红书 cover images (video-thumbnail or rednote-thumbnail).
---

# Reel motion graphics

Dresses one of Ella's portrait talking-head videos in the style of reels she has chosen, then adds sound.
First built 2026-10-20 on her affiliate-program announcement; every script here reproduces that video
exactly (`references/example-affiliate/`).

## Step 0: pick the aesthetic

Use the one she names. If she doesn't name one, ask, because they differ in graphics *and* sound. Read that
aesthetic's file before planning; each lists its reference reel, stills to look at, CSS classes, motion and
measured sound.

| Aesthetic | Feel | Graphics | Sound | Read |
|---|---|---|---|---|
| **green oasis** (default) | punchy, information-dense | green cards, titles behind her head, phone/chat UI, checklists, count-ups | SFX only: booms, whooshes, pops, clicks, typing | `references/aesthetics/green-oasis.md` |
| **neutral colors** | soft, airy, warm beige | white iOS cards, gold italic keywords, "Step N:" + sparkles, yellow sticker pills, butter-yellow circle wipes | sparse "ting" on transitions only, no music | `references/aesthetics/neutral-colors.md` |
| **classic calligraphy** | quiet, editorial, handwritten | one script title lockup + handwritten notebook cutaways, slow fades | no SFX; one soft music bed ~6 dB under voice (ask for the source) | `references/aesthetics/classic-calligraphy.md` |

Set the theme in `cards.py` (`THEME = 'neutral-colors'` / `'classic-calligraphy'`; omit for green oasis) and
start from that aesthetic's example folder: `example-affiliate/`, `example-neutral/`, `example-calligraphy/`.

**Her defaults (all aesthetics; keep them unless she says otherwise):**
- Every graphic is **bilingual**: English with its 中文 line. **No running word-by-word captions**; she burns
  her own subtitles separately. When she has a bilingual SRT for the video, use its English as source text and
  its 中文 as a guide for the graphics' wording.
- **Graphics sit right above her head**: not pinned to the top of the frame, not down at her body (her
  request, 2026-10-20). Use `PLACE = 'above-head'` in cards.py (see "Above-head placement"). The one exception
  is green-oasis hero titles that go *behind* her head with a cut-out.
- Output is 1080×1920 / 30 fps, audio at -14 LUFS. Name it `<source base> motion graphics 中英 sfx.mp4` in the
  source's folder, never overwriting the source.

## Pipeline

Paths: `SK=~/.claude/skills/reel-motion-graphics`, project `P` = `hyperframes-student-kit/video-projects/<slug>/`.
Run every `npx hyperframes` command from inside `$P/public`.

1. **Prep** (~2 min per 5 min of 4K): `bash $SK/scripts/prep.sh "<video>" <slug>`. It makes the proxy, audio,
   embedded `source.srt` (if the video has one) and whisper `transcript.json`. If she has a separate
   `<name> bilingual.srt`, write its English lines to `$P/source.srt` (it beats whisper for wording).
2. **Check for burned-in subtitles** (see "Videos that already have subtitles" below) and **shot changes**
   (a different framing near the end is common). Both change where graphics may go.
3. **Align**: `python3 -I $SK/scripts/align.py $P`, which writes `words.json`.
4. **Plan the beats**: write `$P/beats.json` (key → exact spoken phrase, `["phrase", after_s]` if it repeats),
   then `python3 -I $SK/scripts/beats.py $P`, which writes `times.json`. A phrase that isn't found stops the
   run; fix the phrase, never type a time in.
5. **Cards**: write `$P/scripts/cards.py` (`THEME`, `CARDS`, `FG`), `$P/scripts/cards.js` (timeline) and
   optional `scripts/extra.css`, starting from the aesthetic's example folder.
6. **Cut-outs** (green oasis hero titles only; background job, ~2.5 s compute per second of footage):
   `uv run --with rembg --with "numba>=0.59" --with scipy --with onnxruntime python -I $SK/scripts/matte.py $P fg-intro:0:8.6 ...`
7. **Place + build + look**: with `PLACE = 'above-head'`, first run headtop once (background, ~3-4 min per
   20 min of video): `uv run --with rembg --with "numba>=0.59" --with scipy --with onnxruntime --with pillow python -I $SK/scripts/headtop.py $P`,
   then `python3 -I $SK/scripts/build.py $P && node $SK/scripts/place.mjs $P && python3 -I $SK/scripts/build.py $P`
   (re-run that trio after any card edit). Without PLACE, just `python3 -I $SK/scripts/build.py $P`. Then `npx hyperframes lint` (0 errors; structure
   warnings are expected), `npx hyperframes snapshot . --no-end --at <every card's fullest moment>`, and
   **Read every contact sheet**. Fix and repeat until every card is readable, nothing runs off an edge, nothing
   covers her face or her subtitles, and each card arrives on its phrase.
8. **Render** (~1.3× the video's length): `PRODUCER_BROWSER_GPU_MODE=hardware npx hyperframes render . --quality standard --fps 30 -o ../renders/<slug>.mp4`
   in the background for anything over ~5 min. Pull frames from the MP4 to confirm.
9. **Sound**: write `$P/scripts/cues.py` per the aesthetic, `uv run --with numpy --with soundfile python -I $SK/scripts/sfx.py $P`,
   then `bash $SK/scripts/mix.sh $P $P/renders/<slug>.mp4 $P/renders/<slug>-sfx.mp4`. Re-balancing sound never
   needs a re-render. (Calligraphy: music bed instead; get the source from her first.)
10. **Deliver** to the source folder, open it in QuickTime, and send a short preview clip (the chat upload limit
    is 30 MB). Tell her what's on screen, any wording you invented, and that sound was checked by measurement,
    not by ear.

## Choosing beats

Let the transcript decide the card: a checklist when she enumerates, a flow when she explains steps, a number
moment when a number is the point, a mock-up when she describes tapping through an app. Pace by length and by
aesthetic: green oasis ~1 card per 8-12 s on short videos and ~1 per 20-30 s past 10 minutes; neutral one per
5-8 s with long plain stretches; calligraphy one notebook insert per section. Big moments (hero titles, circle
wipes, notebook spreads) stay scarce, 3-5 per short video. Time every card and row to the phrase, not
the sentence start.

## Above-head placement
`headtop.py` mattes one frame per second and records the top of her head (first row where her silhouette
is ≥12% of the frame wide, so raised hands don't count). `build.py` gives each card an anchor (the 10th
percentile of head-top while that card is on screen) and writes a script-free `measure.html`; `place.mjs`
measures every card's real height in headless Chrome and writes `placement.json`: a translateY that puts
the card's bottom 30 px above her head. Track-3 cards take the slot right above her head; a track-2 card on
screen at the same time stacks above it. Nothing goes above y 170: tall cards shrink (not below 72%) instead.
If two overlapping cards still can't both fit, shorten one (e.g. end the title when the next card arrives)
rather than letting it shrink to unreadable. Write cards in their natural layout (any `top:` value); placement
moves them. On "how i've learned English" her head top sat around y 640-720, and higher in the selfie outro.

## Videos that already have subtitles
Scan before placing anything: sample ~30 frames and find rows of near-white pixels with a dark outline (the
subtitle). On "how i've learned English subbed" they sat at y ≈ 428-522 (of 1920), above her head. Then:
- keep graphics in a TOP zone (y 60-390) and a LOW zone over her body (y 1130-1650, x ≤ 900);
- no titles behind her head (there's no room above it once the subtitles take that band);
- re-check the zones at every shot change (the selfie outro needed bottom placement).
If she gives you the clean (unsubtitled) cut of the same video, keep the same subtitle-safe layout when she
plans to burn her subtitles afterwards; check the two cuts line up with an audio cross-correlation first.

## Things that have bitten before
- **GSAP selector lists leak.** `H('card', '.a, .b')` only scopes `.a`; `.b` matches every card on the page.
  Pass an array: `[H('card', '.a'), '#b']`.
- **Never stack a CSS `translateX(-50%)` with a GSAP `xPercent`.** Centre wide lines with
  `left:0;width:1080px;text-align:center` and shift with `padding-left/right`.
- **Plain strings in cards.py that contain `{zh(...)}` must be f-strings**, or the code prints on screen.
- Rows that appear later use `grow()` (display:none until they land), or the card shows an empty block. In list
  cards set rows `flex-wrap: nowrap` with the text span `flex: 1`, or a long row strands its tick on its own line.
- After appending 中文, check chip rows and buttons for overflow/wrapping; long hand-lettered asides need their
  中文 on its own line.
- A strike line across a WIDE element needs a shallow angle (-2 to -4°) or it climbs into the heading above.
- The matte is per-window: if a hero title outlives its `FG` window, her head pops back under the text.

## Files
- `scripts/` prep.sh · align.py · beats.py · matte.py · headtop.py · build.py (THEME + PLACE aware) · place.mjs · sfx.py · mix.sh
- `assets/style.css`: base design system (green oasis). `assets/themes/`: `neutral-colors.css`, `classic-calligraphy.css`.
- `assets/helpers.js`: `inOut pop grow type blink heroIn heroOut H q` + neutral `iris twinkle floatIn` +
  calligraphy `writeOn softIn softOut`.
- `assets/stills/<aesthetic>/`: reference contact sheets/key frames, and our own demo of each look.
- `assets/sfx/`: bundled Pixabay effects (free for commercial use).
- `references/aesthetics/`: `green-oasis.md` (+ `green-oasis-cards.md`, `green-oasis-sound.md`),
  `neutral-colors.md`, `classic-calligraphy.md`.
- `references/example-affiliate/`, `example-neutral/`, `example-calligraphy/`: starter projects
  (cards.py, cards.js, cues.py; affiliate also has beats.json).
