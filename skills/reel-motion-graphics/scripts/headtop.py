# headtop.py <project-dir>
# Writes <project>/headtop.json: the y (in 1080x1920 px) of the top of her head, once per second, for the
# "above-head" placement (cards.py: PLACE = 'above-head'). Mattes a small frame per second with
# u2net_human_seg, keeps the largest person blob, and takes the first row where the blob is at least 12% of
# the frame wide, so a raised hand or a strand of hair doesn't count as the head. ~3-4 min per 20 min of video.
# Run: uv run --with rembg --with "numba>=0.59" --with scipy --with onnxruntime python -I headtop.py <project>
import json, os, subprocess, sys
import numpy as np
from rembg import new_session, remove
from PIL import Image
from scipy import ndimage

os.chdir(sys.argv[1])
W, H = 270, 480
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', 'public/assets/input-video.mp4', '-vf', f'fps=1,scale={W}:{H}',
                      '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
frames = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
sess = new_session('u2net_human_seg')
tops = []
for i, f in enumerate(frames):
    m = np.asarray(remove(Image.fromarray(f), session=sess, only_mask=True)) > 128
    lab, n = ndimage.label(m)
    if n:
        big = lab == (np.argmax(np.bincount(lab.ravel())[1:]) + 1)
        rows = np.where(big.sum(1) >= 0.12 * W)[0]
        tops.append(round(float(rows[0]) * 1920 / H, 1) if len(rows) else None)
    else:
        tops.append(None)
    if i % 120 == 0: print(f'{i}/{len(frames)} s', flush=True)
# fill gaps (no person found) from neighbours
for i, v in enumerate(tops):
    if v is None:
        near = [tops[j] for j in range(max(0, i - 3), min(len(tops), i + 4)) if tops[j] is not None]
        tops[i] = min(near) if near else 600.0
json.dump(tops, open('headtop.json', 'w'))
a = np.array(tops); print(f'{len(a)} s: head top p5 {np.percentile(a,5):.0f} median {np.median(a):.0f} p95 {np.percentile(a,95):.0f}')
