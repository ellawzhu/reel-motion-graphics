// ── helpers ──
const H = (id, s) => `[data-card-id="${id}"] ${s || ''}`.trim();
const q = (s) => document.querySelector(s);
// rise in, hold, drop out — the default card lifecycle
function inOut(sel, a, b, from) {
  tl.fromTo(sel, Object.assign({ autoAlpha: 0, y: 60, scale: 0.94 }, from || {}),
    { autoAlpha: 1, y: 0, x: 0, scale: 1, rotation: 0, duration: 0.5, ease: 'back.out(1.4)' }, a);
  tl.to(sel, { autoAlpha: 0, y: -40, scale: 0.97, duration: 0.3, ease: 'power2.in' }, b - 0.3);
}
function pop(sel, at, from) {
  tl.fromTo(sel, Object.assign({ autoAlpha: 0, scale: 0.6, y: 20 }, from || {}),
    { autoAlpha: 1, scale: 1, y: 0, x: 0, rotation: 0, duration: 0.42, ease: 'back.out(2)' }, at);
}
// like pop, but the element takes no space until it lands, so its card grows with it
function grow(sel, at, from, disp) {
  tl.set(sel, { display: 'none' }, 0);
  tl.set(sel, { display: disp || 'flex' }, at);
  pop(sel, at, from);
}
function type(sel, text, at, cps) {
  const o = { n: 0 };
  const ch = Array.from(text);
  tl.to(o, { n: ch.length, duration: ch.length / (cps || 18), ease: 'none',
    onUpdate() { q(sel).textContent = ch.slice(0, Math.round(o.n)).join(''); } }, at);
}
function blink(sel, a, b) {
  const n = Math.max(1, Math.floor((b - a) / 0.5));
  for (let i = 0; i < n; i++) tl.set(sel, { opacity: i % 2 ? 1 : 0 }, a + i * 0.5);
}
// serif hero word: letters rise from a blur, staggered (reel 1 "I DIDN'T EDIT")
function heroIn(sel, at) {
  tl.fromTo(sel, { autoAlpha: 0, y: 80, filter: 'blur(18px)' }, { autoAlpha: 1, y: 0, filter: 'blur(0px)', duration: 0.7, ease: 'power3.out' }, at);
}
function heroOut(sel, at) { tl.to(sel, { autoAlpha: 0, y: -60, filter: 'blur(14px)', duration: 0.35, ease: 'power2.in' }, at - 0.35); }


// ── neutral-colors helpers ──
// butter-yellow circle wipe: grows from a point to full frame, holds, then collapses (reference reel's transition)
function iris(sel, at, hold, x, y) {
  const c = `${x || 50}% ${y || 50}%`;
  tl.fromTo(sel, { clipPath: `circle(0% at ${c})` }, { clipPath: `circle(75% at ${c})`, duration: 0.45, ease: 'power3.in' }, at);
  tl.to(sel, { clipPath: `circle(0% at ${c})`, duration: 0.45, ease: 'power3.out' }, at + 0.45 + (hold || 0.15));
}
// sparkles twinkle in, staggered, then shimmer while the header holds
function twinkle(sel, at, until) {
  tl.fromTo(sel, { autoAlpha: 0, scale: 0 }, { autoAlpha: 1, scale: 1, duration: 0.35, stagger: 0.12, ease: 'back.out(3)' }, at);
  const n = Math.max(1, Math.floor(((until || at + 2) - at - 0.6) / 0.8));
  for (let i = 0; i < n; i++) tl.to(sel, { scale: i % 2 ? 1 : 0.6, duration: 0.4, stagger: 0.1, ease: 'sine.inOut' }, at + 0.6 + i * 0.8);
}
// gentle rise for overlays in the neutral look (no overshoot bounce)
function floatIn(sel, at, from) {
  tl.fromTo(sel, Object.assign({ autoAlpha: 0, y: 30 }, from || {}), { autoAlpha: 1, y: 0, x: 0, rotation: 0, duration: 0.55, ease: 'power3.out' }, at);
}

// ── classic-calligraphy helpers ──
// handwriting: reveal each line left→right like a pen writing it (≈ 11 chars/s, the reel's writing pace)
function writeOn(sel, at, cps) {
  const el = q(sel); const n = el ? Array.from(el.textContent).length : 10;
  const d = Math.max(0.4, n / (cps || 11));
  tl.fromTo(sel, { clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0% 0 0)', duration: d, ease: 'none' }, at);
  return at + d;
}
// slow editorial fade (no movement) for lockups and notes
function softIn(sel, at, d) { tl.fromTo(sel, { autoAlpha: 0 }, { autoAlpha: 1, duration: d || 0.8, ease: 'sine.out' }, at); }
function softOut(sel, at, d) { tl.to(sel, { autoAlpha: 0, duration: d || 0.6, ease: 'sine.in' }, at - (d || 0.6)); }
