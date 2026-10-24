# beats.py <project-dir>
# Resolves beats.json {"key": "spoken phrase" | ["phrase", after_seconds] | number} into
# times.json {"key": seconds} by finding each phrase in words.json. Every graphic and
# every sound cue is timed off these keys, so picture and sound stay in sync.
# A phrase that isn't found stops the run: fix the phrase, never guess the time.
import json, re, sys, os

os.chdir(sys.argv[1])
W = json.load(open('words.json'))
N = [re.sub(r"[^a-z0-9%]", '', w['text'].lower()) for w in W]

def at(phrase, after=0.0):
    p = [re.sub(r"[^a-z0-9%]", '', x.lower()) for x in phrase.split()]
    for i in range(len(N) - len(p) + 1):
        if W[i]['start'] >= after and N[i:i+len(p)] == p:
            return round(W[i]['start'], 3)
    raise SystemExit(f'phrase not found: {phrase!r} after {after}s')

dur = float(os.popen('ffprobe -v error -show_entries format=duration -of csv=p=0 public/assets/input-video.mp4').read())
T = {}
for k, v in json.load(open('beats.json')).items():
    T[k] = v if isinstance(v, (int, float)) else at(*v) if isinstance(v, list) else at(v)
T['end'] = round(dur, 3)
json.dump(T, open('times.json', 'w'), indent=1)
print('  '.join(f'{k}={v}' for k, v in T.items()))
