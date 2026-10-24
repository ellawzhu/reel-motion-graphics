# matte.py <project-dir> name:start:end [name:start:end ...]
# Cuts the speaker out of the proxy for each window -> public/assets/<name>.webm
# (VP9 with alpha). Layered ABOVE a hero title and below the cards, it makes the title
# sit behind her head. Run with:
#   uv run --with rembg --with "numba>=0.59" --with scipy --with onnxruntime python -I matte.py ...
# ~2.5 s of compute per second of footage; run it in the background.
import subprocess, os, glob, sys
from rembg import new_session, remove
from PIL import Image, ImageFilter

os.chdir(sys.argv[1])
src = 'public/assets/input-video.mp4'
sess = new_session('u2net_human_seg')
for spec in sys.argv[2:]:
    name, a, b = spec.split(':'); a, b = float(a), float(b)
    d = f'work/{name}'; os.makedirs(d, exist_ok=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(a), '-i', src, '-t', str(b - a), '-start_number', '0', f'{d}/f%05d.png'], check=True)
    for f in sorted(glob.glob(f'{d}/f*.png')):
        im = Image.open(f).convert('RGB')
        # matte at half size for speed, then upsample and feather the edge
        m = remove(im.resize((540, 960)), session=sess, only_mask=True, post_process_mask=True)
        im.putalpha(m.resize(im.size, Image.BILINEAR).filter(ImageFilter.GaussianBlur(1.5)))
        im.save(os.path.join(d, 'm' + os.path.basename(f)[1:]))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '30', '-start_number', '0', '-i', f'{d}/m%05d.png',
                    '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '8M', '-auto-alt-ref', '0', f'public/assets/{name}.webm'], check=True)
    print(name, a, b, 'done', flush=True)
subprocess.run(['rm', '-rf', 'work'])
