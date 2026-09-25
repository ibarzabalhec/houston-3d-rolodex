/* The intro reel. Five seconds on a 120 beats-a-minute grid, drawn on one
   canvas from a market's `reel` block (reel.py), which the build reads from the
   same records the page renders. The page plays it first (see the note on #reel
   in the template); intro/ holds a standalone copy for video.

   RolodexReel(canvas, data, {colors}) returns {ready, play, finish, stop,
   renderAt, resize}. render(t) draws any frame from t alone, so frames can be
   captured and scrubbed. Colours come from the page's own tokens, so the reel
   follows the theme and the market's accent. */
window.RolodexReel = function (cv, D, opt) {
"use strict";
opt = opt || {};
const P = opt.colors || {};
function hex(v, d){ v = String(v || '').trim();
  if (/^#[0-9a-f]{6}$/i.test(v)) return v;
  if (/^#[0-9a-f]{3}$/i.test(v)) return '#' + v.slice(1).split('').map(c => c + c).join('');
  return d; }
function mixHex(a, b, k){
  const A = parseInt(a.slice(1), 16), B = parseInt(b.slice(1), 16);
  const ch = s => [(s >> 16) & 255, (s >> 8) & 255, s & 255];
  const x = ch(A), y = ch(B);
  return '#' + x.map((v, i) => Math.round(v + (y[i] - v) * k).toString(16).padStart(2, '0')).join('');
}
/* ground, ink and accent from the page. The flood is the ink colour; what sits on
   it is the paper colour, so a dark theme floods light and the reel still reads. */
const C = {paper: hex(P.paper, '#FFFFFF'), paper2: hex(P.paper2, '#FAFAFA'), paper3: hex(P.paper3, '#F0F0F0'),
  ink: hex(P.ink, '#111111'), ink2: hex(P.ink2, '#3D3D3D'), ink3: hex(P.ink3, '#6B6B6B'),
  rule: hex(P.rule, '#E4E4E4'), acc: hex(P.acc, '#FF4F00')};
C.night = C.ink; C.light = C.paper;
C.dgrey = mixHex(C.night, C.light, .25); C.lgrey = mixHex(C.night, C.light, .62); C.track = mixHex(C.night, C.light, .14);

const DUR = 5.0;
const HITS = [0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5];   // the strong beats
const SANS = 'Archivo, "Helvetica Neue", Arial, sans-serif';
const MONO = '"IBM Plex Mono", ui-monospace, Menlo, monospace';
const ctx = cv.getContext('2d');
let W = 0, H = 0, DPR = 1, L = null;

const clamp = (v, a, b) => v < a ? a : v > b ? b : v;
const seg = (t, a, b) => clamp((t - a) / (b - a), 0, 1);
const lerp = (a, b, k) => a + (b - a) * k;
const E = {
  outExpo: k => k >= 1 ? 1 : 1 - Math.pow(2, -10 * k),
  outCubic: k => 1 - Math.pow(1 - k, 3),
  inCubic: k => k * k * k,
  inOutCubic: k => k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2,
  outBack: k => { const c1 = 1.5, c3 = c1 + 1; return 1 + c3 * Math.pow(k - 1, 3) + c1 * Math.pow(k - 1, 2); }
};
function rng(seed){ return () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
  t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const fmt = n => Number(n).toLocaleString('en-US');
const font = (w, px, fam) => w + ' ' + px + 'px ' + (fam || SANS);

function wrap(text, max, f){
  ctx.font = f; const words = text.split(' '), out = []; let cur = '';
  for (const w of words){ const t = cur ? cur + ' ' + w : w;
    if (ctx.measureText(t).width > max && cur){ out.push(cur); cur = w; } else cur = t; }
  if (cur) out.push(cur); return out;
}

/* ---------- layout, from the frame's size ---------- */
function layout(){
  const m = Math.round(Math.max(16, Math.min(W, H) * 0.06));
  const S = {m}, narrow = W < 640, N = D.n;
  S.cs = clamp(Math.round(W * 0.0115), 11, 15);
  S.bf = Math.round(Math.min(H * 0.2, W * 0.16));

  /* the hook: the permit count, cropped by the frame; two lines on a tall screen */
  const hs = fmt(D.permits), two = H / W > 1.3 && hs.includes(',');
  const parts = two ? [hs.slice(0, hs.indexOf(',') + 1), hs.slice(hs.indexOf(',') + 1)] : [hs];
  ctx.font = font(800, 100);
  const w100 = Math.max(...parts.map(q => ctx.measureText(q).width));
  let fs = 100 * (W * (two ? 1.04 : 1.08)) / w100;
  fs = two ? Math.min(fs, H * 0.6 / 1.64) : Math.min(fs, H * 0.62);
  S.hfs = fs; ctx.font = font(800, fs);
  S.hx = (W - w100 * fs / 100) / 2;
  const b1 = two ? H / 2 - fs * 0.05 : H * 0.5 + fs * 0.36;
  S.lines = parts.map((q, j) => ({q, b: b1 + j * fs * 0.82}));
  S.hb = S.lines[S.lines.length - 1].b;
  S.chars = [];
  for (const ln of S.lines){ let x = S.hx; for (const ch of ln.q){ const w = ctx.measureText(ch).width; S.chars.push({ch, x, w, b: ln.b}); x += w; } }
  S.cap1 = wrap(('Single-family homes permitted · ' + D.place + ' · ' + D.permits_year).toUpperCase(),
                W - 2 * m, font(600, S.cs, MONO));
  S.src1 = ('Source: ' + D.permits_source).toUpperCase();

  /* one point per firm, sampled from the hook's own glyphs by farthest-point sampling */
  const oc = document.createElement('canvas'); oc.width = Math.max(1, Math.ceil(W)); oc.height = Math.max(1, Math.ceil(H));
  const o = oc.getContext('2d'); o.fillStyle = '#000'; o.font = font(800, fs); o.textBaseline = 'alphabetic';
  for (const ln of S.lines) o.fillText(ln.q, S.hx, ln.b);
  const img = o.getImageData(0, 0, oc.width, oc.height).data;
  const step = Math.max(3, Math.round(fs / 45)), pts = [];
  for (let yy = 0; yy < oc.height; yy += step) for (let xx = 0; xx < oc.width; xx += step)
    if (img[(yy * oc.width + xx) * 4 + 3] > 140) pts.push([xx, yy]);
  const pick = [];
  if (pts.length){
    const dmin = new Float64Array(pts.length).fill(Infinity);
    let cur = 0; for (let i = 1; i < pts.length; i++) if (pts[i][0] < pts[cur][0]) cur = i;
    for (let k = 0; k < N; k++){
      pick.push(pts[cur]); let best = -1, bi = 0;
      for (let i = 0; i < pts.length; i++){
        const dx = pts[i][0] - pts[cur][0], dy = pts[i][1] - pts[cur][1], d = dx * dx + dy * dy;
        if (d < dmin[i]) dmin[i] = d; if (dmin[i] > best){ best = dmin[i]; bi = i; }
      }
      cur = bi;
    }
  }
  while (pick.length < N) pick.push([W / 2, H / 2]);
  S.rs = Math.max(2, step * 0.9);

  /* the roster grid, shaped to the frame: an exact rectangle when the count has
     one that fits, else the nearest shape with a short last row */
  const gx0 = m, gx1 = W - m, gy0 = narrow ? H * 0.3 : H * 0.34, gy1 = H - m * 1.5;
  const asp = (gx1 - gx0) / (gy1 - gy0);
  let best = null;
  for (let c = 1; c <= N; c++){
    const r = Math.ceil(N / c), empty = c * r - N; if (empty >= c) continue;
    const sc = Math.abs(Math.log((c / r) / asp)) + 1.5 * empty / N;
    if (!best || sc < best.sc) best = {c, r, sc};
  }
  const cell = Math.min((gx1 - gx0) / best.c, (gy1 - gy0) / best.r);
  const ox = (gx0 + gx1) / 2 - cell * best.c / 2, oy = (gy0 + gy1) / 2 - cell * best.r / 2;
  S.rg = cell * 0.27;
  const slots = [];
  for (let i = 0; i < N; i++){ const col = i % best.c, row = Math.floor(i / best.c);
    slots.push({x: ox + cell * (col + .5), y: oy + cell * (row + .5), col, row}); }
  const byX = pick.slice().sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const order = slots.map((s, i) => i).sort((a, b) => slots[a].col - slots[b].col || slots[a].row - slots[b].row);
  const Q = new Array(N); order.forEach((si, k) => { Q[si] = {x: byX[k][0], y: byX[k][1]}; });

  /* homes closed a year, log scale; the builders that publish a figure stack on it */
  const ax0 = m, ax1 = W - m, lo = Math.log(20), hi = Math.log(8000);
  S.ax = v => ax0 + (Math.log(v) - lo) / (hi - lo) * (ax1 - ax0);
  S.base = H * 0.8; S.bandTop = H * 0.47;
  S.ra = Math.min(S.rg, (ax1 - ax0) / 52);
  const pubs = D.firms.map((f, i) => ({i, v: f.v})).filter(p => p.v).sort((a, b) => a.v - b.v);
  const placed = [], A = {};
  for (const p of pubs){
    /* stack upward past any dot it overlaps; the tolerance stops a dot that
       sits exactly one step above another from being moved there forever */
    const x = S.ax(p.v), step = 2 * S.ra + 2; let y = S.base - S.ra - 2, moved = true, guard = 0;
    while (moved && guard++ < 400){ moved = false;
      for (const q of placed){ if (Math.hypot(q.x - x, q.y - y) < step - 0.01){ y = Math.min(y - 0.01, q.y - step); moved = true; } } }
    placed.push({x, y}); A[p.i] = {x, y};
  }
  S.focus = {x: (S.ax(D.band[0]) + S.ax(D.band[1])) / 2 + (narrow ? W * 0.12 : 0), y: S.base - H * 0.16};

  /* the last frame: the wordmark, its dot, the title printed line by line */
  ctx.font = font(700, 100);
  const we = ctx.measureText('ROLODEX').width / 100 - 0.14;
  S.wf = Math.round(Math.min(W * 0.2, H * 0.22, (W - 2 * m) / (we + 0.62)));
  S.ww = we * S.wf;
  S.tf = Math.round(clamp(S.wf * 0.3, 16, 44));
  const tl = [];
  D.title.forEach((line, j) => { for (const l of wrap(line, W - 2 * m, font(j ? 700 : 400, S.tf))) tl.push({l, b: j > 0}); });
  S.tl = tl;
  const blockH = S.wf * 0.78 + S.tf * 0.9 + tl.length * S.tf * 1.22;
  S.wy = Math.round(H / 2 - blockH / 2 + S.wf * 0.74);
  S.wx = m;
  S.dot = {x: S.wx + S.ww + S.wf * 0.235, y: S.wy - S.wf * 0.58, r: S.wf * 0.115};
  S.ty = S.wy + S.wf * 0.28 + S.tf * 1.2;

  let ti = 0, di = 0; const r = rng(7);
  S.F = D.firms.map((f, i) => Object.assign({}, f, {G: slots[i], Q: Q[i], A: A[i] || null,
    stag: slots[i].col / Math.max(1, best.c - 1) * 0.7 + r() * 0.3,
    ti: f.tr ? ti++ : -1, di: f.dec ? di++ : -1}));
  return S;
}

/* ---------- camera ---------- */
function kick(t, upto){ let k = 0; for (const h of HITS){ if (upto !== undefined && h > upto) continue;
  if (t >= h && t < h + .35) k += Math.exp(-(t - h) / .07); } return k; }
function cam(t){
  const push = E.inOutCubic(seg(t, 1.5, 2.05)), whip = E.outExpo(seg(t, 2.5, 2.72)), p = push * (1 - whip);
  let s = lerp(1, 1.2, p);
  const fx = lerp(W / 2, L.focus.x, p), fy = lerp(H / 2, L.focus.y, p);
  let r = lerp(0, -0.045, seg(t, 1.5, 1.52)) * (1 - E.outCubic(seg(t, 1.5, 1.95))) * (1 - whip);
  r += 0.03 * (1 - E.outExpo(seg(t, 2.5, 2.75))) * (t >= 2.5 ? 1 : 0);
  s *= 1 + 0.018 * kick(t, 4.0);
  return {s, fx, fy, r};
}
function apply(c, x, y){
  const dx = (x - c.fx) * c.s, dy = (y - c.fy) * c.s, cs = Math.cos(c.r), sn = Math.sin(c.r);
  return {x: W / 2 + dx * cs - dy * sn, y: H / 2 + dx * sn + dy * cs};
}
function withCam(c, fn){ ctx.save(); ctx.translate(W / 2, H / 2); ctx.rotate(c.r); ctx.scale(c.s, c.s); ctx.translate(-c.fx, -c.fy); fn(); ctx.restore(); }

/* ---------- a firm's dot at time t ---------- */
function dotAt(f, t){
  if (t < 0.75) return null;
  let x, y, r, a = 1, col = C.ink, hollow = false;
  if (t < 1.0) return {x: f.Q.x, y: f.Q.y, r: L.rs * E.outCubic(seg(t, .75, .9)), a, col};
  const d2 = f.stag * .12, k2 = E.outBack(seg(t, 1.0 + d2, 1.3 + d2));
  x = lerp(f.Q.x, f.G.x, k2); y = lerp(f.Q.y, f.G.y, k2); r = lerp(L.rs, L.rg, clamp(k2, 0, 1));
  if (t < 1.5) return {x, y, r, a, col};
  if (t < 2.5){
    const d3 = f.stag * .1, k3 = E.inOutCubic(seg(t, 1.5 + d3, 1.92 + d3));
    if (f.A){
      x = lerp(f.G.x, f.A.x, k3); y = lerp(f.G.y, f.A.y, k3); r = lerp(L.rg, L.ra, k3);
      if (k3 > .6){ if (f.fit === 'partial') col = C.ink3; else if (f.fit === 'fail') hollow = true; }
    } else { a = 1 - k3; y += k3 * H * .06; r *= 1 - .45 * k3; }
    return {x, y, r, a, col, hollow};
  }
  const d4 = f.stag * .08, k4 = E.outExpo(seg(t, 2.5 + d4, 2.74 + d4));
  if (f.A){ x = lerp(f.A.x, f.G.x, k4); y = lerp(f.A.y, f.G.y, k4); r = lerp(L.ra, L.rg, k4); }
  else { x = f.G.x; y = f.G.y; r = L.rg * E.outBack(k4); a = clamp(k4 * 1.4, 0, 1); }
  col = C.dgrey;
  if (t >= 3.0 && t < 4.0 && f.tr){
    const k = seg(t, 3.0 + f.ti * .018, 3.07 + f.ti * .018);
    if (k > 0){ col = C.acc; r *= 1 + .45 * Math.sin(Math.PI * k) + .12; }
  }
  if (t >= 3.5 && t < 4.0){
    const i = Math.floor((t - 3.5) / .125), t0 = 3.5 + i * .125;
    if (f.cat === i){ col = C.light; a = 1; r *= 1 + .3 * Math.sin(Math.PI * seg(t, t0, t0 + .07)); }
    else { col = C.dgrey; a = .3; }
  }
  if (t >= 4.0){
    col = C.dgrey;
    if (f.dec){ const k = seg(t, 4.0 + f.di * .0028, 4.05 + f.di * .0028); if (k > 0){ col = C.light; r *= 1 + .3 * Math.sin(Math.PI * k); } }
  }
  if (t >= 4.25){
    const d = f.stag * .1, k = E.inCubic(seg(t, 4.25 + d, 4.47 + d));
    if (k >= 1) return null;
    x = lerp(x, L.dot.x, k); y = lerp(y, L.dot.y, k); r = lerp(r, L.dot.r * .7, k);
    if (k > .35) col = C.acc;
  }
  return {x, y, r, a, col, hollow};
}

/* ---------- pieces ---------- */
function flood(t){
  /* the flood prints in layers from the bottom, each pass the other way; it lifts from the top */
  const n = 8, lh = H / n;
  for (let k = 0; k < n; k++){
    const y = H - (k + 1) * lh, ltr = k % 2 === 0;
    const kin = E.inOutCubic(seg(t, 2.47 + k * .026, 2.56 + k * .026));
    const kout = E.inOutCubic(seg(t, 4.25 + (n - 1 - k) * .022, 4.33 + (n - 1 - k) * .022));
    if (kin <= 0 || kout >= 1) continue;
    let x0, x1;
    if (kout > 0){ if (ltr){ x0 = W * kout; x1 = W; } else { x0 = 0; x1 = W * (1 - kout); } }
    else if (ltr){ x0 = 0; x1 = W * kin; } else { x0 = W * (1 - kin); x1 = W; }
    ctx.fillStyle = C.night; ctx.fillRect(x0, y - .5, x1 - x0, lh + 1);
    const head = kout > 0 ? (ltr ? x0 : x1) : (ltr ? x1 : x0);
    if ((kin > 0 && kin < 1) || (kout > 0 && kout < 1)){ ctx.fillStyle = C.acc; ctx.fillRect(head - 2, y - .5, 4, lh + 1); }
  }
}
const night = t => t >= 2.56 && t < 4.44;

function spaced(s, x, y, em){
  const px = parseFloat(ctx.font.match(/(\d+(?:\.\d+)?)px/)[1]), sp = px * em;
  if ('letterSpacing' in ctx){ ctx.letterSpacing = sp + 'px'; ctx.fillText(s, x, y); ctx.letterSpacing = '0px'; return; }
  for (const ch of s){ ctx.fillText(ch, x, y); x += ctx.measureText(ch).width + sp; }
}

function hook(t){
  if (t >= .97) return;
  const fade = 1 - seg(t, .75, .95);
  ctx.save(); ctx.globalAlpha = fade; ctx.fillStyle = C.ink; ctx.font = font(800, L.hfs); ctx.textBaseline = 'alphabetic';
  L.chars.forEach((c, j) => {
    const k = E.outExpo(seg(t, j * .032 - .05, j * .032 + .15));
    if (k <= 0) return;
    const sc = lerp(1.45, 1, k), dy = lerp(H * .07, 0, k);
    ctx.save(); ctx.globalAlpha = fade * clamp(k * 3, 0, 1);
    ctx.translate(c.x + c.w / 2, c.b - L.hfs * .36 + dy); ctx.scale(sc, sc);
    ctx.fillText(c.ch, -c.w / 2, L.hfs * .36); ctx.restore();
  });
  const ry = Math.min(H - L.m * 2.6, L.hb + L.m * .9), kr = E.inOutCubic(seg(t, .18, .4));
  ctx.fillStyle = C.ink; ctx.fillRect(L.m, ry, (W - 2 * L.m) * kr, 2);
  if (kr > 0 && kr < 1){ ctx.fillStyle = C.acc; ctx.fillRect(L.m + (W - 2 * L.m) * kr - 3, ry - 2, 6, 6); }
  ctx.font = font(600, L.cs, MONO); ctx.fillStyle = C.ink; ctx.textBaseline = 'top';
  const all = L.cap1.join('\n'), shown = Math.floor(all.length * seg(t, .28, .6));
  let used = 0; L.cap1.forEach((line, j) => {
    const n = clamp(shown - used, 0, line.length); used += line.length + 1;
    spaced(line.slice(0, n), L.m, ry + L.cs * 1.1 + j * L.cs * 1.5, .1);
  });
  if (t > .5){ ctx.fillStyle = C.ink3; ctx.font = font(500, Math.max(10, L.cs - 2), MONO);
    ctx.globalAlpha = fade * seg(t, .5, .6); spaced(L.src1, L.m, ry + L.cs * 1.1 + L.cap1.length * L.cs * 1.5 + 4, .08); }
  ctx.restore();
}

/* the big figure in the top-left slot: in on its beat with a punch, out on the next with a cut */
function big(t, t0, t1, text, col, label, lcol){
  if (t < t0 || t >= t1) return;
  const k = E.outExpo(seg(t, t0, t0 + .16)), sz = L.bf, y = L.m + sz * .74;
  ctx.save();
  ctx.beginPath(); ctx.rect(0, 0, L.m + W * k, H); ctx.clip();
  ctx.translate(L.m, y); const sc = lerp(1.08, 1, k) * (1 + .02 * kick(t)); ctx.scale(sc, sc);
  ctx.fillStyle = col; ctx.font = font(800, sz); ctx.textBaseline = 'alphabetic'; ctx.fillText(text, 0, 0);
  ctx.restore();
  if (label){
    ctx.save(); ctx.fillStyle = lcol; ctx.font = font(600, L.cs, MONO); ctx.textBaseline = 'top';
    ctx.globalAlpha = seg(t, t0 + .05, t0 + .14);
    wrap(label.toUpperCase(), W - 2 * L.m, font(600, L.cs, MONO)).forEach((l, j) => spaced(l, L.m, y + sz * .16 + j * L.cs * 1.5, .1));
    ctx.restore();
  }
}

function axis(t){
  if (t < 1.95 || t >= 2.6) return;
  const k = seg(t, 2.0, 2.2), k2 = seg(t, 2.08, 2.3), a = 1 - seg(t, 2.5, 2.58);
  ctx.save(); ctx.globalAlpha = a;
  const x0 = L.ax(D.band[0]), x1 = L.ax(D.band[1]), x2 = L.ax(D.band2[1]);
  const top = L.bandTop, bh = L.base - L.bandTop;
  ctx.fillStyle = C.paper3; ctx.fillRect(x0, top, (x1 - x0) * E.inOutCubic(k), bh);
  ctx.fillStyle = C.paper2; ctx.fillRect(x2 - (x2 - x1) * E.inOutCubic(k2), top, (x2 - x1) * E.inOutCubic(k2), bh);
  if (k > 0 && k < 1){ ctx.fillStyle = C.acc; ctx.fillRect(x0 + (x1 - x0) * E.inOutCubic(k) - 2, top, 4, bh); }
  ctx.fillStyle = C.ink; ctx.fillRect(L.m, L.base, (W - 2 * L.m) * E.outExpo(seg(t, 1.95, 2.15)), 1.5);
  ctx.font = font(500, Math.max(10, L.cs - 1), MONO); ctx.fillStyle = C.ink3; ctx.textBaseline = 'top'; ctx.textAlign = 'center';
  ctx.globalAlpha = a * seg(t, 2.05, 2.15);
  for (const v of [25, 100, 400, 1500, 6000]) ctx.fillText(fmt(v), L.ax(v), L.base + 8);
  ctx.textAlign = 'left'; ctx.restore();
}

function dots(t){
  const c = cam(t), cp = cam(t - 1 / 60);
  for (const f of L.F){
    const d = dotAt(f, t); if (!d || d.r <= 0 || d.a <= 0) continue;
    const p = apply(c, d.x, d.y), r = d.r * c.s;
    const dp = dotAt(f, t - 1 / 60), q = dp ? apply(cp, dp.x, dp.y) : p;
    ctx.globalAlpha = d.a;
    const len = Math.hypot(p.x - q.x, p.y - q.y);
    if (d.hollow){
      ctx.strokeStyle = C.ink; ctx.lineWidth = Math.max(1.25, r * .28); ctx.fillStyle = C.paper;
      ctx.beginPath(); ctx.arc(p.x, p.y, Math.max(.5, r - ctx.lineWidth / 2), 0, Math.PI * 2); ctx.fill(); ctx.stroke();
    } else if (len > 1.5){
      ctx.strokeStyle = d.col; ctx.lineCap = 'round'; ctx.lineWidth = r * 2;
      ctx.beginPath(); ctx.moveTo(q.x, q.y); ctx.lineTo(p.x, p.y); ctx.stroke();
    } else {
      ctx.fillStyle = d.col; ctx.beginPath(); ctx.arc(p.x, p.y, r, 0, Math.PI * 2); ctx.fill();
    }
  }
  ctx.globalAlpha = 1;
}

/* four kinds of firm, one per eighth note, each lighting its own dots */
function catsBeat(t){
  if (t < 3.5 || t >= 4.0 || !D.cats.length) return;
  const i = clamp(Math.floor((t - 3.5) / .125), 0, D.cats.length - 1), c = D.cats[i];
  ctx.font = font(800, 100); const sz = Math.min(L.bf, 100 * (W - 2 * L.m) / ctx.measureText(c.label).width);
  const t0 = 3.5 + i * .125, k = E.outExpo(seg(t, t0, t0 + .06)), y = L.m + L.bf * .74;
  ctx.save(); ctx.fillStyle = C.light; ctx.font = font(800, sz); ctx.textBaseline = 'alphabetic';
  ctx.translate(L.m + lerp(-sz * .15, 0, k) * (i % 2 ? -1 : 1), y); ctx.fillText(c.label, 0, 0); ctx.restore();
  ctx.save(); ctx.fillStyle = C.lgrey; ctx.font = font(600, L.cs, MONO); ctx.textBaseline = 'top';
  spaced((c.n + ' of ' + D.n).toUpperCase(), L.m, y + L.bf * .16, .1); ctx.restore();
}

function finale(t){
  if (t < 4.5) return;
  const k = E.outExpo(seg(t, 4.5, 4.66));
  ctx.save(); ctx.fillStyle = C.ink; ctx.font = font(700, L.wf); ctx.textBaseline = 'alphabetic';
  ctx.beginPath(); ctx.rect(L.wx - 4, 0, (L.ww + L.wf) * k + 4, H); ctx.clip();
  if ('letterSpacing' in ctx) ctx.letterSpacing = (-.02 * L.wf) + 'px';
  ctx.fillText('ROLODEX', L.wx + lerp(-L.wf * .2, 0, k), L.wy);
  if ('letterSpacing' in ctx) ctx.letterSpacing = '0px';
  ctx.restore();
  const kd = seg(t, 4.5, 4.64), pop = kd < 1 ? E.outBack(kd) : 1;
  ctx.fillStyle = C.acc; ctx.beginPath(); ctx.arc(L.dot.x, L.dot.y, L.dot.r * pop, 0, Math.PI * 2); ctx.fill();
  L.tl.forEach((ln, j) => {
    const t0 = 4.6 + j * .075, kk = E.inOutCubic(seg(t, t0, t0 + .13));
    if (kk <= 0) return;
    ctx.save(); ctx.font = font(ln.b ? 700 : 400, L.tf); ctx.fillStyle = ln.b ? C.ink : C.ink2; ctx.textBaseline = 'alphabetic';
    const w = ctx.measureText(ln.l).width + 2, y = L.ty + j * L.tf * 1.22, ltr = j % 2 === 0;
    ctx.beginPath(); ctx.rect(ltr ? L.wx : L.wx + w * (1 - kk), y - L.tf, w * kk, L.tf * 1.35); ctx.clip();
    ctx.fillText(ln.l, L.wx, y); ctx.restore();
    if (kk < 1){ ctx.fillStyle = C.acc; ctx.fillRect((ltr ? L.wx + w * kk : L.wx + w * (1 - kk)) - 2, y - L.tf * .85, 4, L.tf * 1.05); }
  });
  ctx.save(); ctx.globalAlpha = seg(t, 4.85, 4.98); ctx.fillStyle = C.ink3; ctx.font = font(600, Math.max(10, L.cs - 1), MONO);
  ctx.textBaseline = 'alphabetic'; spaced(('Prepared by ' + D.by).toUpperCase(), L.m, H - L.m - 4, .12); ctx.restore();
}

function progress(t){
  if (t >= 4.55) return;
  const a = 1 - seg(t, 4.4, 4.55), y = H - 3, nt = night(t);
  ctx.save(); ctx.globalAlpha = a;
  ctx.fillStyle = nt ? C.track : C.rule; ctx.fillRect(0, y, W, 3);
  ctx.fillStyle = nt ? C.lgrey : C.ink; ctx.fillRect(0, y, W * t / DUR, 3);
  for (const h of HITS){ ctx.fillRect(W * h / DUR - .5, y - 4, 1, 4); }
  ctx.restore();
}

function render(t){
  if (!L) return;
  t = clamp(t, 0, DUR);
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  ctx.fillStyle = C.paper; ctx.fillRect(0, 0, W, H);
  withCam(cam(t), () => axis(t));
  flood(t);
  hook(t);
  dots(t);
  big(t, 1.0, 1.5, fmt(D.n), C.ink, 'Firms screened', C.ink);
  big(t, 2.0, 2.5, D.band[0] + ' to ' + D.band[1], C.ink, 'Homes closed a year · one or two printers', C.ink);
  big(t, 3.0, 3.5, String(D.track), C.acc, 'Have paid for a new building method', C.light);
  catsBeat(t);
  big(t, 4.0, 4.25, String(D.dec), C.light, 'of ' + D.n + ' with a decision-maker named', C.light);
  finale(t);
  progress(t);
}

/* ---------- playback ---------- */
let raf = 0, t0 = 0, speed = 1, last = DUR, playing = false, onEnd = null;
function size(){
  const b = cv.getBoundingClientRect();
  W = Math.max(1, b.width || innerWidth); H = Math.max(1, b.height || innerHeight); DPR = Math.min(devicePixelRatio || 1, 2);
  cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
  L = layout();
}
function frame(now){
  if (!t0) t0 = now;
  last = (now - t0) / 1000 * speed;
  render(last);
  if (last < DUR){ raf = requestAnimationFrame(frame); }
  else { playing = false; const f = onEnd; onEnd = null; if (f) f(); }
}
const fonts = ['400 40px Archivo', '700 40px Archivo', '800 40px Archivo', '600 12px "IBM Plex Mono"', '500 12px "IBM Plex Mono"'];
const ready = Promise.race([
  Promise.all(fonts.map(f => (document.fonts && document.fonts.load) ? document.fonts.load(f) : null)).catch(() => null),
  new Promise(r => setTimeout(r, 800))
]).then(() => { size(); render(0); return api; });

const api = {
  ready, DUR,
  play(sp, done){ cancelAnimationFrame(raf); speed = sp || 1; onEnd = done || null; t0 = 0; playing = true; raf = requestAnimationFrame(frame); },
  finish(){ cancelAnimationFrame(raf); playing = false; last = DUR; render(DUR); },
  stop(){ cancelAnimationFrame(raf); playing = false; onEnd = null; },
  renderAt(t){ cancelAnimationFrame(raf); playing = false; last = t; render(t); },
  resize(){ size(); if (!playing) render(last); },
  get playing(){ return playing; }
};
return api;
};
