// place.mjs <project-dir>
// "Above-head" placement (cards.py: PLACE = 'above-head'). build.py writes public/measure.html (the page without
// scripts) and placement-input.json (each card's window, track and the highest head-top during it, from
// headtop.json). This loads measure.html in headless Chromium with the real fonts, measures every card's
// content box, and writes placement.json: a translateY (+ shrink if it can't fit) that puts each card's
// bottom edge GAP px above her head. Track-3 cards claim the slot right above the head; a track-2 card that is
// on screen at the same time stacks above it. Run build.py again afterwards to bake the transforms in.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { execSync } from 'node:child_process';
import { createRequire } from 'node:module';

// HyperFrames' own headless Chrome + the newest puppeteer-core in the npx cache (both arrive with the CLI)
const chrome = execSync('npx hyperframes browser path', { encoding: 'utf8' }).trim().split('\n').pop();
const npx = path.join(os.homedir(), '.npm', '_npx');
const pc = fs.readdirSync(npx).map((d) => path.join(npx, d, 'node_modules', 'puppeteer-core'))
  .filter((d) => fs.existsSync(path.join(d, 'package.json')))
  .sort((a, b) => JSON.parse(fs.readFileSync(path.join(b, 'package.json'))).version.localeCompare(
    JSON.parse(fs.readFileSync(path.join(a, 'package.json'))).version, undefined, { numeric: true }))[0];
const puppeteer = createRequire(path.join(pc, 'package.json'))(pc);
const proj = path.resolve(process.argv[2]);
const cards = JSON.parse(fs.readFileSync(path.join(proj, 'placement-input.json'), 'utf8'));
// TOPMIN: Ella wants graphics right above her head, never "all the way to the top"; tall cards shrink instead
const GAP = 30, TOPMIN = 170, STACKGAP = 22, MINSCALE = 0.72;

const browser = await puppeteer.launch({ executablePath: chrome, headless: true });
const page = await browser.newPage();
await page.setViewport({ width: 1080, height: 1920 });
await page.goto('file://' + path.join(proj, 'public', 'measure.html'), { waitUntil: 'load', timeout: 60000 });
await page.evaluate(() => document.fonts.ready);
await new Promise((r) => setTimeout(r, 400));
const boxes = await page.evaluate(() => {
  const out = {};
  document.querySelectorAll('.card-host').forEach((h) => {
    let top = 1e9, bot = -1e9;
    for (const el of h.children) {
      if (el.offsetHeight >= 1500) continue;          // full-frame backdrops (wipes, desk, green bg) stay put
      top = Math.min(top, el.offsetTop); bot = Math.max(bot, el.offsetTop + el.offsetHeight);
    }
    out[h.dataset.cardId] = { top, bot };
  });
  return out;
});
await browser.close();

const order = cards.slice().sort((x, y) => (y.track - x.track) || (x.a - y.a));
const placed = [], result = {};
for (const c of order) {
  const b = boxes[c.id];
  if (!b || b.top > b.bot || c.fixed) continue;
  let bottom = c.anchor - GAP;
  for (const p of placed) if (p.a < c.b && c.a < p.b) bottom = Math.min(bottom, p.top - STACKGAP);
  const height = b.bot - b.top;
  const s = bottom - height < TOPMIN ? Math.max(MINSCALE, (bottom - TOPMIN) / height) : 1;
  result[c.id] = { dy: Math.round(bottom - b.bot), s: +s.toFixed(3), ob: b.bot };
  placed.push({ a: c.a, b: c.b, top: bottom - height * s });
}
fs.writeFileSync(path.join(proj, 'placement.json'), JSON.stringify(result, null, 1));
const shrunk = Object.entries(result).filter(([, v]) => v.s < 1).map(([k, v]) => `${k}×${v.s}`);
console.log(`placed ${Object.keys(result).length} cards above her head` + (shrunk.length ? `; shrunk to fit: ${shrunk.join(', ')}` : ''));
