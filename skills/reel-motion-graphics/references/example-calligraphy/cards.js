// CLASSIC CALLIGRAPHY starter timeline. Slow fades, handwriting written on, nothing bounces.
softIn(H('cTitle', '.c-lockup'), T.howlearn, 1.0);
softOut(H('cTitle', '.c-lockup'), T.bg, 0.8);
softIn(H('cBook', '.c-desk'), T.bg, 0.5); softIn(H('cBook', '.c-book'), T.bg, 0.5);
let w = writeOn('#h1', T.bg + 0.5);
writeOn('#h1z', w);
writeOn('#h2', T.chinese); writeOn('#h3', T.seattle); w = writeOn('#h4', T.before17); writeOn('#h4z', w);
w = writeOn('#h5', T.age31); writeOn('#h5z', w);
softOut(H('cBook', '> *'), T.math, 0.6);
softIn(H('cNote', '.c-note'), T.env, 0.8);
softOut(H('cNote', '.c-note'), T.reality, 0.6);
