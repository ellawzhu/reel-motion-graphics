# sfx.py <project-dir>
# Renders <project>/public/assets/sfx-mix.wav from scripts/cues.py, which is executed with
# T (times.json) and cue(t, name, gain=1.0, align='onset') in scope.
#   align='onset' the sound's attack lands on t (pops, clicks, booms, typing)
#   align='peak'  its loudest moment lands on t (whooshes timed to a motion's midpoint)
#   align='end'   it finishes at t (the riser, so it crests as a number lands)
# Sound names are files in public/assets/sfx/ (copied from this skill's assets/sfx).
import json, subprocess, sys, os
import numpy as np, soundfile as sf

SR = 48000
os.chdir(sys.argv[1])
T = json.load(open('times.json'))
DUR = T['end']

# Gains put each library file at the level the reference reels use against a voice whose
# short-term peaks sit near -18 dBFS: booms ~6 dB above voice peaks, whooshes/pops
# ~6-8 dB under, clicks/typing ~10 dB under. See references/aesthetics/green-oasis-sound.md.
GAIN = {'impact-bass-1': 0.36, 'impact-bass-2': 0.33, 'whoosh': 0.14, 'whoosh-short': 0.13, 'whoosh-cinematic': 0.12,
        'pop': 0.21, 'click': 0.5, 'click-soft': 0.4, 'typing': 0.8, 'key-press': 0.6, 'sparkle': 0.12, 'ping': 0.5,
        'chime': 0.6, 'notification': 0.32, 'riser': 0.12, 'error': 0.5, 'glitch-1': 0.15, 'glitch-2': 0.1, 'glitch-3': 0.3}

LIB = {}
def clip(name):
    if name not in LIB:
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'public/assets/sfx/{name}.mp3', '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'],
                             capture_output=True, check=True).stdout
        a = np.frombuffer(raw, dtype=np.float32).reshape(-1, 2)
        env = np.abs(a).max(axis=1)
        onset = int(np.argmax(env > env.max() * 0.1))
        if name.startswith('impact'):
            # the library "impacts" are ~2 s sustained near-0 dBFS drones; shape them into a decaying boom
            t = np.clip(np.arange(len(a)) - onset, 0, None) / SR
            a = a * np.exp(-t / 0.45)[:, None]
        LIB[name] = (a, onset, int(np.argmax(np.abs(a).max(axis=1))))
    return LIB[name]

cues = []
def cue(t, name, gain=1.0, align='onset'):
    cues.append((float(t), name, gain, align))

exec(open('scripts/cues.py', encoding='utf-8').read(), dict(T=T, DUR=DUR, cue=cue))

n = int(DUR * SR)
mix = np.zeros((n, 2), np.float32)
for t, name, g, align in cues:
    a, on, pk = clip(name)
    start = int(t * SR) - {'peak': pk, 'onset': on, 'end': len(a)}[align]
    a = a * GAIN.get(name, 0.3) * g
    if start < 0: a = a[-start:]; start = 0
    end = min(n, start + len(a))
    if end > start: mix[start:end] += a[:end - start]
sf.write('public/assets/sfx-mix.wav', mix, SR, subtype='FLOAT')
print(len(cues), 'cues; peak', round(float(20 * np.log10(np.abs(mix).max() + 1e-9)), 1), 'dBFS -> public/assets/sfx-mix.wav')
