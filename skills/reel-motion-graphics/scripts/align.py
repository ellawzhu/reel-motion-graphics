# align.py <project-dir>
# Writes words.json: the verbatim words of source.srt (her edited subtitle text) re-timed
# onto whisper's word timings with difflib; unmatched words are interpolated inside
# their cue. With no source.srt, the whisper transcript is used as-is.
import json, re, difflib, sys, os

os.chdir(sys.argv[1])
wh = json.load(open('transcript.json'))
if not os.path.exists('source.srt'):
    json.dump([{'text': w['text'], 'start': w['start'], 'end': w['end']} for w in wh], open('words.json', 'w'), indent=0)
    sys.exit(print(len(wh), 'words (whisper only, no source.srt)'))

def ts(s):
    h, m, r = s.split(':'); s, ms = r.split(',')
    return int(h)*3600 + int(m)*60 + int(s) + int(ms)/1000
cues = []
for b in open('source.srt', encoding='utf-8-sig').read().strip().split('\n\n'):
    L = b.strip().split('\n'); a, e = L[1].split(' --> ')
    cues.append((ts(a), ts(e), ' '.join(L[2:])))
words = []
for ci, (a, e, t) in enumerate(cues):
    toks = t.split()
    for i, w in enumerate(toks):
        words.append({'text': w, 'cue': ci, 'start': a + (e-a)*i/len(toks), 'end': a + (e-a)*(i+1)/len(toks)})
norm = lambda s: re.sub(r"[^a-z0-9%]", '', s.lower())
A = [norm(w['text']) for w in words]; B = [norm(w['text']) for w in wh]
hit = 0
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
    if tag == 'equal':
        for k in range(i2 - i1):
            words[i1+k].update(start=wh[j1+k]['start'], end=wh[j1+k]['end'], m=1); hit += 1
n = len(words); i = 0
while i < n:
    if words[i].get('m'): i += 1; continue
    j = i
    while j < n and not words[j].get('m'): j += 1
    lo = words[i-1]['end'] if i > 0 else cues[words[i]['cue']][0]
    hi = max(lo, words[j]['start'] if j < n else cues[words[j-1]['cue']][1])
    for k in range(i, j):
        words[k]['start'] = lo + (hi-lo)*(k-i)/(j-i); words[k]['end'] = lo + (hi-lo)*(k-i+1)/(j-i)
    i = j
for w in words: w.pop('m', None)
json.dump(words, open('words.json', 'w'), indent=0)
print(f'{hit}/{n} words matched to whisper timings')
