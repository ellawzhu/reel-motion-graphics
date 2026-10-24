# build.py <project-dir>
# Assembles <project>/public/index.html from:
#   times.json            beat times (beats.py)
#   scripts/cards.py      CARDS = [(id, start, end, track, cls, html), ...] and FG = [(name, start, end), ...]
#                         — executed with T, DUR, zh(), row(), TICK, CURSOR, STAR already defined
#   scripts/cards.js      the per-card GSAP timeline code (T, tl and assets/helpers.js are in scope)
#   scripts/extra.css     optional per-video style overrides
# plus this skill's assets/style.css + assets/helpers.js. If cards.py sets THEME (an aesthetic other than
# the default 'green-oasis'), assets/themes/<THEME>.css and that theme's fonts are added too.
import json, os, sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(sys.argv[1])
T = json.load(open('times.json'))
DUR = T['end']

def zh(s, cls=''): return f'<u class="zh {cls}">{s}</u>'
TICK = '<svg class="tick" viewBox="0 0 24 24"><path d="M5 12.5l4.2 4.2L19 7" /></svg>'
CURSOR = '<svg class="cursor" viewBox="0 0 40 52"><path d="M3 3l0 40 10-10 7 15 7-3-7-15 14 0z" /></svg>'
STAR = '<svg class="star" viewBox="0 0 24 24"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
def row(rid, en, cn, lead=TICK, cls=''):
    return f'<div class="row {cls}" id="{rid}">{lead}<span>{en}{zh(cn)}</span></div>'

ns = dict(T=T, DUR=DUR, zh=zh, row=row, TICK=TICK, CURSOR=CURSOR, STAR=STAR)
exec(open('scripts/cards.py', encoding='utf-8').read(), ns)
CARDS, FG = ns['CARDS'], ns.get('FG', [])
THEME = ns.get('THEME', 'green-oasis')
PLACE = ns.get('PLACE', 'zones')          # 'zones' = positions as written; 'above-head' = scripts/place.mjs
tm = lambda k: T[k] if isinstance(k, str) else k
placement = {}
if PLACE == 'above-head':
    # anchor = the highest head-top while the card is up (median-filtered so one odd frame can't yank it)
    ht = json.load(open('headtop.json'))
    sm = [sorted(ht[max(0, i - 1):i + 2])[len(ht[max(0, i - 1):i + 2]) // 2] for i in range(len(ht))]
    inp = []
    for cid, a, b, track, cls, body in CARDS:
        a, b = tm(a), tm(b)
        # only the seconds the card is actually up (a shot change right after it must not count), and the
        # 10th percentile rather than the min, so one odd reading (hand, hair flip) can't yank the card up
        win = sorted(sm[max(0, int(a)):min(len(sm), int(b) + 1)]) or [600]
        inp.append(dict(id=cid, a=a, b=b, track=track, anchor=win[len(win) // 10], fixed=cls == 'fixed'))
    json.dump(inp, open('placement-input.json', 'w'), indent=0)
    if os.path.exists('placement.json'): placement = json.load(open('placement.json'))

hosts = []
for cid, a, b, track, cls, body in CARDS:
    a, b = tm(a), tm(b)
    assert b > a, f'card {cid} ends before it starts'
    z = 3 if cls == 'hero' else 5          # hero titles sit under the speaker cut-out (z 4)
    pl = placement.get(cid)
    tf = f';transform:translateY({pl["dy"]}px) scale({pl["s"]});transform-origin:50% {pl["ob"]}px' if pl else ''
    hosts.append(f'<div class="card-host clip {cls}" data-card-id="{cid}" data-start="{a:.3f}" data-duration="{b-a:.3f}" '
                 f'data-track-index="{track}" style="z-index:{z}{tf}">{body}\n</div>')
fg = '\n'.join(f'<video class="fg" id="{n}" src="assets/{n}.webm" muted playsinline data-start="{a}" data-duration="{b-a:.2f}" data-track-index="{10+i}"></video>'
               for i, (n, a, b) in enumerate(FG))

css = open(f'{SKILL}/assets/style.css').read()
fonts = 'family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@500;600;700;800&family=Caveat:wght@600&family=Noto+Sans+SC:wght@500;700&family=Noto+Serif+SC:wght@600;700'
if THEME != 'green-oasis':
    css += '\n' + open(f'{SKILL}/assets/themes/{THEME}.css').read()
    fonts += {'neutral-colors': '',
              'classic-calligraphy': '&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Kalam&family=Ma+Shan+Zheng&family=Long+Cang'}[THEME]
if os.path.exists('scripts/extra.css'): css += '\n' + open('scripts/extra.css').read()
js = open(f'{SKILL}/assets/helpers.js').read() + '\n' + open('scripts/cards.js', encoding='utf-8').read()
title = os.path.basename(os.getcwd())
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=1080, height=1920" />
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=block" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
{css}
</style>
</head>
<body>
<div id="stage" data-composition-id="{title}" data-start="0" data-duration="{DUR}" data-fps="30" data-width="1080" data-height="1920">
<video id="bg-video" src="assets/input-video.mp4" muted playsinline data-start="0" data-duration="{DUR}" data-track-index="0"></video>
<audio id="vo" src="assets/audio.mp3" data-start="0" data-duration="{DUR}" data-track-index="1"></audio>
{fg}
{chr(10).join(hosts)}
<script>
(function () {{
const T = {json.dumps(T)};
const tl = gsap.timeline({{ paused: true }});
{js}
tl.set({{}}, {{}}, {DUR});
window.__timelines = window.__timelines || {{}};
window.__timelines["{title}"] = tl;
}})();
</script>
</div>
</body>
</html>
'''
open('public/index.html', 'w').write(page)
if PLACE == 'above-head':
    # script-free copy for scripts/place.mjs to measure the cards' natural layout
    import re
    # (no video/audio either: a long proxy would keep the page loading forever)
    m = re.sub(r'<script.*?</script>', '', page, flags=re.S)
    open('public/measure.html', 'w').write(re.sub(r'<(video|audio)\b.*?</\1>', '', m, flags=re.S))
print(THEME + ',', PLACE + (' (placed)' if placement else ''), ':', len(CARDS), 'cards,', len(FG), 'cut-out windows ->', os.path.abspath('public/index.html'))
