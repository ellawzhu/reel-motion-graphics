// NEUTRAL COLORS starter timeline. Calm: float-ins (no bounce), sparkles, one yellow circle wipe per section.
floatIn(H('nTitle', '.n-title'), T.howlearn);
floatIn('#nPill', T.howlearn + 1.2, { rotation: -8 });
tl.to(H('nTitle', '> *'), { autoAlpha: 0, duration: 0.4 }, T.bg - 0.4);
iris('#iris1', T.bg - 0.45, 0.1);                       // section change = butter-yellow wipe
twinkle(H('nStep', '.sparkles i'), T.chinese, T.math);
floatIn(H('nStep', '.n-step'), T.chinese + 0.2);
tl.to(H('nStep', '> *'), { autoAlpha: 0, duration: 0.4 }, T.math - 0.4);
floatIn(H('nCard', '.n-card'), T.seattle - 0.3);
[['#nr1', T.seattle - 0.1], ['#nr2', T.seattle + 0.4], ['#nr3', T.before17]].forEach(([s, t]) => floatIn(s, t, { x: -20, y: 0 }));
tl.to(H('nCard', '.n-card'), { autoAlpha: 0, y: 20, duration: 0.35 }, T.math - 0.35);
floatIn(H('nComment', '.n-card'), T.math + 0.2);
type('#nType', 'You were young… 你那时还小', T.young, 12);
tl.to(H('nComment', '.n-card'), { autoAlpha: 0, duration: 0.35 }, T.reality - 0.35);
