// ── intro: green cold open, then the green wipes up to reveal the room ──
heroIn(H('intro', '#introZ'), 0.0);
heroIn(H('intro', '#introA'), 0.05);
tl.fromTo(H('intro', '#introB'), { autoAlpha: 0, x: 60 }, { autoAlpha: 1, x: 0, duration: 0.6, ease: 'power3.out' }, 0.7);
tl.fromTo(H('intro', '#introbg'), { clipPath: 'inset(0% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 100% 0%)', duration: 0.55, ease: 'power3.inOut' }, T.today - 0.5);
heroOut(H('intro', '#introA'), T.today); heroOut(H('intro', '#introZ'), T.today); heroOut(H('intro', '#introB'), T.today);

// ── magazine cover ──
tl.fromTo(H('cover', '#coverK'), { autoAlpha: 0, y: -20 }, { autoAlpha: 1, y: 0, duration: 0.4 }, T.today);
tl.fromTo(H('cover', '#coverR'), { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: 'power3.inOut' }, T.today + 0.1);
// letters of AFFILIATE assemble on "huge announcement"
heroIn(H('cover', '#coverA'), T.huge);
tl.fromTo(H('cover', '#coverB'), { autoAlpha: 0, y: 30, rotation: -6 }, { autoAlpha: 1, y: 0, rotation: -4, duration: 0.5, ease: 'back.out(2)' }, T.program);
pop(H('cover', '#coverBar'), T.program + 0.3, { x: -60 });
heroIn(H('cover', '#coverZ'), T.program + 0.2);
tl.to(H('cover', '#coverA'), { scale: 1.06, duration: T.thinking - T.huge, ease: 'none' }, T.huge);
['#coverK', '#coverR', '#coverA', '#coverB', '#coverZ', '#coverBar'].forEach((s) => heroOut(H('cover', s), T.thinking));

// ── genesis chat bar ──
inOut(H('genesis', '.chat'), T.genesis, T.latest);
type('#genT', 'why start an affiliate program?', T.genesis + 0.4, 20);
type('#genZ', '为什么要做带货推广计划？', T.genesis + 2.1, 8);
blink(H('genesis', '.caret'), T.genesis, T.latest);

// ── course card ──
inOut(H('course', '.gcard'), T.latest, T.acclaim, { rotation: -3, y: 120 });
pop(H('course', '.pill'), T.latest + 0.9);
tl.fromTo(H('course', '.thumb'), { rotation: -8, scale: 0.8 }, { rotation: 0, scale: 1, duration: 0.6, ease: 'back.out(2)' }, T.latest + 0.15);

// ── 5 stars, then real reviews drop onto a pile ──
tl.fromTo(H('acclaim', '.star'), { autoAlpha: 0, scale: 0, rotation: -90 }, { autoAlpha: 1, scale: 1, rotation: 0, duration: 0.4, ease: 'back.out(2.5)', stagger: 0.09 }, T.acclaim);
const revAt = (i) => T.acclaim + 0.55 + i * 1.25;
[[0, -3], [-16, 2.5], [14, -2], [-10, 3], [8, -1]].forEach(([x, r], i) => {
  tl.fromTo(`#rev${i}`, { autoAlpha: 0, x: x, y: -160, rotation: r * 3, scale: 1.08 },
    { autoAlpha: 1, x: x, y: i * 14, rotation: r, scale: 1, duration: 0.45, ease: 'back.out(1.6)' }, revAt(i));
  // the covered card keeps only its edge in the pile, so no half-hidden text peeks out
  if (i) tl.to(`#rev${i - 1} > *`, { opacity: 0, duration: 0.2 }, revAt(i) + 0.2);
});
tl.to([H('acclaim', '.center-block'), H('acclaim', '.pile')], { autoAlpha: 0, y: -40, duration: 0.3 }, T.newstore - 0.3);

// ── stores ──
inOut('#oldS', T.oldstore - 0.6, T.simple, { x: -80, rotation: -4 });
tl.to('#oldX', { scaleX: 1, rotation: -12, duration: 0.35, ease: 'power3.out' }, T.scratch - 0.3);
tl.to('#oldS', { opacity: 0.55, scale: 0.94, duration: 0.3 }, T.scratch);
inOut('#newS', T.scratch - 0.5, T.simple, { x: 80, rotation: 4 });

// ── simple ──
heroIn(H('simple', '.display'), T.simple);
heroOut(H('simple', '.display'), T.iflike);

// ── who can join ──
inOut(H('who', '.gcard'), T.iflike, T.gostore);
grow('#who1', T.enrolled); grow('#who2', T.friends);
grow('#who3', T.friends + 2.2, { x: -30 });

// ── phone walkthrough ──
inOut(H('howto', '.phone'), T.gostore - 0.2, T.videos, { x: -120, rotation: -6 });
tl.set(['#phDet', '#phSheet', '#phToast'], { autoAlpha: 0 }, 0);
const cur = H('howto', '.cursor');
tl.fromTo(cur, { autoAlpha: 0, x: 420, y: 560 }, { autoAlpha: 1, x: 150, y: 210, duration: 0.7, ease: 'power3.inOut' }, T.product - 0.8);
tl.to(cur, { scale: 0.8, duration: 0.08, yoyo: true, repeat: 1 }, T.product - 0.05);
tl.fromTo('#phDet', { autoAlpha: 0, x: 380 }, { autoAlpha: 1, x: 0, duration: 0.4, ease: 'power3.out' }, T.product + 0.1);
tl.to(cur, { x: 265, y: 430, duration: 0.6, ease: 'power3.inOut' }, T.icon - 0.65);
tl.to(cur, { scale: 0.8, duration: 0.08, yoyo: true, repeat: 1 }, T.icon - 0.05);
tl.fromTo('#phIcon', { scale: 1 }, { scale: 1.35, duration: 0.15, yoyo: true, repeat: 1 }, T.icon);
tl.fromTo('#phSheet', { autoAlpha: 0, y: 300 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: 'power3.out' }, T.icon + 0.35);
tl.to(cur, { x: 180, y: 560, duration: 0.6, ease: 'power3.inOut' }, T.asaff - 0.7);
tl.to(cur, { scale: 0.8, duration: 0.08, yoyo: true, repeat: 1 }, T.asaff + 1.2);
tl.to('#phSheet', { autoAlpha: 0, y: 300, duration: 0.35, ease: 'power2.in' }, T.yourpage - 0.4);
tl.fromTo('#phToast', { autoAlpha: 0, y: -40 }, { autoAlpha: 1, y: 0, duration: 0.4, ease: 'back.out(2)' }, T.yourpage);
tl.to(cur, { autoAlpha: 0, duration: 0.2 }, T.yourpage);
const stepT = [T.gostore, T.product, T.icon, T.yourpage];
stepT.forEach((s, i) => {
  pop(`#st${i + 1}`, s, { x: 60, scale: 0.9 });
  if (i) tl.to(`#st${i}`, { opacity: 0.45, duration: 0.3 }, s);
});
tl.to(H('howto', '.steps'), { autoAlpha: 0, x: 60, duration: 0.3 }, T.videos - 0.3);

// ── share chips ──
pop('#shK', T.videos - 0.2);
pop('#ch1', T.videos, { rotation: -8 }); pop('#ch2', T.posts, { rotation: 8 }); pop('#ch3', T.live, { rotation: -5 });
tl.to([H('share', '.chips'), '#shK'], { autoAlpha: 0, y: -30, duration: 0.3 }, T.point - 0.3);

// ── why: four reasons building ──
inOut(H('why', '.gcard'), T.point, T.oneperson);
[T.outlet, T.cut, T.thanks, T.word].forEach((s, i) => grow(`#why${i + 1}`, s, { x: -40, scale: 0.95 }));

// ── 24-hour clock counting down ──
inOut(H('clock', '.clockbox'), T.oneperson, T.friendsjoin);
(function () {
  const o = { s: 86400 };
  tl.to(o, { s: 86400 - 47, duration: T.friendsjoin - T.h24, ease: 'none', onUpdate() {
    const v = Math.round(o.s), h = Math.floor(v / 3600), m = Math.floor((v % 3600) / 60), s = v % 60;
    q('#clk').textContent = [h, m, s].map((x) => String(x).padStart(2, '0')).join(':');
  } }, T.h24);
})();

// ── friends multiplying around "me" ──
const pos = [[150, 20], [640, 20], [20, 190], [770, 180], [250, 220], [560, 230], [0, 40], [790, 30], [130, 140], [660, 120]];
pop(H('friends', '.av.me'), T.friendsjoin);
document.querySelectorAll(H('friends', '.av.f')).forEach((el, i) => {
  gsap.set(el, { left: pos[i][0], top: pos[i][1] });
  pop(el, T.friendsjoin + 0.5 + i * 0.12);
});
pop('#dlab', T.friendsjoin + 1.8, { rotation: -8 });
pop('#dK', T.friendsjoin + 0.3);
tl.to('#dK', { autoAlpha: 0, duration: 0.3 }, T.brandnew - 0.3);
tl.to(H('friends', '#dots'), { autoAlpha: 0, y: -30, duration: 0.3 }, T.brandnew - 0.3);

// ── incentives ──
pop('#inK', T.brandnew);
heroIn('#inT', T.incent - 0.3);
tl.to(H('incent', '.center-block'), { autoAlpha: 0, y: -30, duration: 0.3 }, T.currently - 0.3);

// ── 30% hero behind her ──
tl.fromTo('#p30K', { autoAlpha: 0, y: -20 }, { autoAlpha: 1, y: 0, duration: 0.4 }, T.currently);
heroIn('#p30N', T.p30 - 0.7);
(function () {
  const o = { v: 0 };
  tl.to(o, { v: 30, duration: 1.0, ease: 'power3.out', onUpdate() { q('#p30V').textContent = Math.round(o.v); } }, T.p30 - 0.6);
})();
tl.fromTo('#p30C', { autoAlpha: 0, y: 30, rotation: -5 }, { autoAlpha: 1, y: 0, rotation: -4, duration: 0.5, ease: 'back.out(2)' }, T.p30 + 0.5);
tl.to('#p30N', { scale: 1.08, duration: 0.18, yoyo: true, repeat: 1, ease: 'power2.out' }, T.everyone);
['#p30K', '#p30N', '#p30C'].forEach((s) => heroOut(s, T.evenif));

// ── follow pill ──
inOut(H('follow', '.follow'), T.evenif, T.p30b, { y: 80 });
const fc = H('follow', '.cursor');
tl.fromTo(fc, { autoAlpha: 0, x: 200, y: 220 }, { autoAlpha: 1, x: 0, y: 0, duration: 0.6, ease: 'power3.inOut' }, T.followme - 0.7);
tl.to(fc, { y: -60, duration: 0.25, ease: 'power2.out' }, T.followme - 0.1);
tl.to('#fBtn', { scale: 0.9, duration: 0.08, yoyo: true, repeat: 1 }, T.followme + 0.15);
tl.set('#fTxt', { textContent: 'Following ✓ · 已关注' }, T.followme + 0.2);
tl.to('#fBtn', { backgroundColor: '#d9b45a', color: '#0e1a14', duration: 0.2 }, T.followme + 0.2);

// ── deadline ──
inOut(H('deadline', '.gcard'), T.p30b, T.five);
tl.to('#dlFill', { scaleX: 0.72, duration: 1.4, ease: 'power3.inOut' }, T.endyear);
pop('#dlLeft', T.twomonths - 0.2);

// ── 5 FREE hero behind her ──
tl.fromTo('#fvK', { autoAlpha: 0, y: -20 }, { autoAlpha: 1, y: 0, duration: 0.4 }, T.five);
heroIn('#fvN', T.five);
heroIn('#fvZ', T.five + 0.6);
tl.fromTo('#fvC', { autoAlpha: 0, y: 30, rotation: -5 }, { autoAlpha: 1, y: 0, rotation: -3, duration: 0.5, ease: 'back.out(2)' }, T.five + 1.0);
['#fvK', '#fvN', '#fvC', '#fvZ'].forEach((s) => heroOut(s, T.wayslot));

// ── how to win a slot ──
inOut(H('slot', '.gcard'), T.wayslot, T.top5);
[T.h_follow, T.h_comment, T.h_post, T.h_tag].forEach((s, i) => {
  grow(`#sl${i + 1}`, s, { x: -40, scale: 0.95 });
  tl.fromTo(`#sl${i + 1} .tick`, { scale: 0 }, { scale: 1, duration: 0.3, ease: 'back.out(3)' }, s + 0.25);
});
grow('#slBot', T.h_bot, { rotation: -4 }, 'block');

// ── top 5 ──
pop('#t5R', T.top5, { rotation: -6 });
pop('#t5Q', T.promote);
tl.to(H('top5', '.center-block'), { autoAlpha: 0, y: -30, duration: 0.3 }, T.onlyfive - 0.3);

// ── refund flow ──
pop('#rfK', T.onlyfive);
pop('#rf1', T.sample - 0.3);
tl.fromTo('#rfA1', { scaleX: 0 }, { scaleX: 1, duration: 0.4 }, T.twosales - 0.4);
pop('#rf2', T.twosales);
tl.fromTo('#rfA2', { scaleX: 0 }, { scaleX: 1, duration: 0.4 }, T.refunded - 0.3);
pop('#rf3', T.refunded, { rotation: 6 });
pop('#rfEq', T.forfree + 0.5);
tl.to(H('refund', '.eq b:last-of-type'), { scale: 1.2, duration: 0.15, yoyo: true, repeat: 1 }, T.made30 + 0.3);
tl.to(['#rfK', H('refund', '.flow'), '#rfEq'], { autoAlpha: 0, y: -30, duration: 0.3 }, T.wins - 0.3);

// ── everybody wins (behind her) ──
heroIn('#wnZ', T.wins + 0.3);
heroIn('#wnA', T.wins);
tl.fromTo('#wnB', { autoAlpha: 0, y: 30, rotation: -6 }, { autoAlpha: 1, y: 0, rotation: -4, duration: 0.45, ease: 'back.out(2)' }, T.wins + 0.5);
heroOut('#wnA', T.basic); heroOut('#wnZ', T.basic); heroOut('#wnB', T.basic);

// ── group chat ──
inOut(H('group', '.gchat'), T.group - 0.3, T.golive, { y: 100 });
grow('#gb1', T.talkabout, { x: -40 }, 'block'); grow('#gb2', T.kindposts, { x: 40 }, 'block');
grow('#gb3', T.kindvideos, { x: -40 }, 'block'); grow('#gb4', T.yourideas, { x: 40 }, 'block');

// ── live ──
inOut(H('live', '.livebox'), T.golive, T.giveback);
tl.to('#lvP', { scale: 1.08, duration: 0.5, yoyo: true, repeat: 3, ease: 'sine.inOut' }, T.golive + 0.5);
pop('#lvH', T.nothing, { rotation: -4 });

// ── give back ──
heroIn(H('giveback', '.center-block'), T.giveback);
pop('#gbH', T.giveback + 2.2, { rotation: -4 });
tl.to(H('giveback', '.center-block'), { autoAlpha: 0, y: -30, duration: 0.3 }, T.seeyou - 0.3);

// ── see you ──
inOut(H('seeyou', '.cbox'), T.seeyou, T.steps);
grow('#sy1', T.commentsec, { x: -40 }); grow('#sy2', T.groupchat, { x: -40 });

// ── RedNote eligibility ──
inOut(H('rednote', '.gcard'), T.steps, T.letmeknow);
grow('#rn1', T.steps + 0.6, { x: -40 }); grow('#rn2', T.rednote + 1.0, { x: -40 });
grow('#rn3', T.instantly, { x: -40 }); grow('#rn4', T.followers, { x: -40 });

// ── end CTA ──
tl.fromTo(H('end', '.cta'), { autoAlpha: 0, y: 60 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: 'back.out(1.6)' }, T.letmeknow);
type('#endT', 'I qualified! 我开通啦！', T.letmeknow + 0.5, 12);
blink(H('end', '.caret'), T.letmeknow, T.end);

