function initAtmosphere() {
  const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canvas = document.getElementById('atmos');
  if (!canvas || !canvas.getContext) return;
  const ctx = canvas.getContext('2d');

  const state = {
    w: 0, h: 0, dpr: 1,
    mouseX: 0, mouseY: 0,
    scrollY: 0, targetScrollY: 0,
    parallaxX: 0, parallaxY: 0, targetParallaxX: 0, targetParallaxY: 0,
    // Animation state — added for the drift/gleam/label-breath layers.
    peaks: null,              // mutable peak objects (built once per resize)
    labelSlots: null,         // mutable label positions with phase offsets
    gleam: null,              // active gleam sweep (or null when idle)
    nextGleamAt: 0,           // ms timestamp when the next gleam should trigger
    lastFrame: 0,             // last RAF timestamp (for dt calc)
    lastRender: 0,            // last canvas redraw timestamp (for 15 fps throttle)
    rafId: 0,                 // live RAF handle (0 = not looping)
    animate: false,           // master flag — set by decideMode() based on gates
  };

  // Colors read once per resize / theme change (not every frame).
  function readColors() {
    const cs = getComputedStyle(document.documentElement);
    const accent = (cs.getPropertyValue('--accent-warm').trim()) || '#C9A063';
    const ink    = (cs.getPropertyValue('--text-primary').trim()) || '#8a8a8a';
    const isLight = document.documentElement.getAttribute('data-theme') === 'light';
    return { accent, ink, isLight };
  }

  // Stable PRNG — shapes persist across draws
  function mulberry32(seed) {
    let s = seed >>> 0;
    return function() {
      s = (s + 0x6D2B79F5) >>> 0;
      let t = s;
      t = Math.imul(t ^ t >>> 15, t | 1);
      t ^= t + Math.imul(t ^ t >>> 7, t | 61);
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }

  // Procedural heightfield built from a few 2-D gaussians → gives real
  // topographic elevation contours when you sample at evenly-spaced levels
  // (like a USGS quad map). Each peak carries drift velocity + amplitude
  // LFO state so the field can mutate frame-to-frame.
  function buildPeaks(w, h) {
    const r = mulberry32(20260419);
    const n = 6 + Math.floor(r() * 3);        // 6-8 peaks/basins
    const peaks = [];
    for (let i = 0; i < n; i++) {
      const ampBase = (r() > 0.35 ? 1 : -0.6) * (0.55 + r() * 0.85);
      peaks.push({
        cx: (0.05 + r() * 0.9) * w,
        cy: (0.05 + r() * 0.9) * h,
        // Current (animated) amp — initialized to the LFO value at t=0, which
        // equals ampBase since sin(phase) is normalized below.
        amp: ampBase,
        ampBase,
        // Anisotropic — stretches to feel like ridgelines, not circles
        sx: (0.12 + r() * 0.22) * Math.min(w, h),
        sy: (0.10 + r() * 0.20) * Math.min(w, h),
        theta: r() * Math.PI,
        // Drift — gentle random-walk velocity in px/sec. Kept small so peaks
        // wander organically over tens of seconds rather than streaking.
        vx: (r() - 0.5) * 8,
        vy: (r() - 0.5) * 6,
        // Amplitude LFO — each peak breathes on its own period + phase so the
        // field ripples asynchronously, never pulsing in lockstep.
        ampLfoPeriodS: 25 + r() * 50,         // 25–75 seconds per cycle
        ampLfoPhase: r() * Math.PI * 2,
        ampLfoDepth: 0.12 + r() * 0.10,       // ±12–22% of ampBase
      });
    }
    return peaks;
  }
  function heightAt(x, y, peaks) {
    let z = 0;
    for (const p of peaks) {
      const dx = x - p.cx, dy = y - p.cy;
      const cs = Math.cos(p.theta), sn = Math.sin(p.theta);
      const u = (dx * cs + dy * sn) / p.sx;
      const v = (-dx * sn + dy * cs) / p.sy;
      z += p.amp * Math.exp(-(u*u + v*v) * 0.5);
    }
    // Low-amplitude, high-freq ripple for organic crispness (no wobble)
    z += 0.04 * Math.sin(x * 0.013 + y * 0.009);
    z += 0.03 * Math.cos(x * 0.007 - y * 0.017);
    return z;
  }

  // Marching-squares iso-line tracer over a coarse grid. Produces proper
  // topographic contours rather than concentric ellipses — i.e. real map
  // elevation lines that branch, close, and meander naturally.
  function drawContours(ctx, w, h, peaks, levels, colors) {
    const step = 14;                 // grid step in px — smaller = smoother
    const cols = Math.ceil(w / step) + 1;
    const rows = Math.ceil(h / step) + 1;
    const grid = new Float32Array(cols * rows);
    for (let j = 0; j < rows; j++) {
      for (let i = 0; i < cols; i++) {
        grid[j * cols + i] = heightAt(i * step, j * step, peaks);
      }
    }
    function get(i, j) { return grid[j * cols + i]; }
    function lerp(a, b, t) { return a + (b - a) * t; }

    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    levels.forEach((level, idx) => {
      const isIndex = (idx % 5 === 0);   // every 5th contour is an "index contour"
      ctx.strokeStyle = isIndex ? colors.accent : colors.ink;
      ctx.globalAlpha = isIndex ? colors.alphaIndex : colors.alphaMinor;
      ctx.lineWidth = isIndex ? 0.9 : 0.5;
      ctx.beginPath();
      for (let j = 0; j < rows - 1; j++) {
        for (let i = 0; i < cols - 1; i++) {
          const a = get(i, j);
          const b = get(i+1, j);
          const c = get(i+1, j+1);
          const d = get(i, j+1);
          let code = 0;
          if (a > level) code |= 1;
          if (b > level) code |= 2;
          if (c > level) code |= 4;
          if (d > level) code |= 8;
          if (code === 0 || code === 15) continue;
          const x0 = i * step, y0 = j * step;
          const x1 = x0 + step, y1 = y0 + step;
          // Interpolate crossing points on each edge
          const tA = (level - a) / (b - a || 1e-9);
          const tB = (level - b) / (c - b || 1e-9);
          const tC = (level - d) / (c - d || 1e-9);
          const tD = (level - a) / (d - a || 1e-9);
          const pA = [x0 + step * tA, y0];
          const pB = [x1,             y0 + step * tB];
          const pC = [x0 + step * tC, y1];
          const pD = [x0,             y0 + step * tD];
          function seg(p, q) {
            ctx.moveTo(p[0], p[1]);
            ctx.lineTo(q[0], q[1]);
          }
          switch (code) {
            case 1:  case 14: seg(pA, pD); break;
            case 2:  case 13: seg(pA, pB); break;
            case 4:  case 11: seg(pB, pC); break;
            case 8:  case 7:  seg(pC, pD); break;
            case 3:  case 12: seg(pB, pD); break;
            case 6:  case 9:  seg(pA, pC); break;
            case 5:  seg(pA, pD); seg(pB, pC); break;
            case 10: seg(pA, pB); seg(pC, pD); break;
          }
        }
      }
      ctx.stroke();
    });
  }

  // Survey-paper grid — clean straight lines with tick marks. Subtle; intended
  // to sit under the contours like graph paper, not curved projection lobes.
  function drawGrid(ctx, w, h, colors) {
    ctx.save();
    ctx.strokeStyle = colors.ink;
    ctx.globalAlpha = colors.alphaGrid;
    ctx.lineWidth = 0.4;
    const major = 120;     // primary grid spacing
    ctx.beginPath();
    for (let x = major; x < w; x += major) { ctx.moveTo(x, 0); ctx.lineTo(x, h); }
    for (let y = major; y < h; y += major) { ctx.moveTo(0, y); ctx.lineTo(w, y); }
    ctx.stroke();
    // Minor grid — dotted ticks every 30px along the major lines
    ctx.globalAlpha = colors.alphaGrid * 0.45;
    ctx.beginPath();
    for (let x = 0; x < w; x += 30) { ctx.moveTo(x, 0); ctx.lineTo(x, 4); }
    for (let y = 0; y < h; y += 30) { ctx.moveTo(0, y); ctx.lineTo(4, y); }
    ctx.stroke();
    ctx.restore();
  }

  // Build 4 persistent label slots — position fixed on (re)size, but the
  // elevation number re-samples from heightAt() every frame and the opacity
  // breathes on an independent period per slot.
  function buildLabelSlots(w, h) {
    const r = mulberry32(42);
    const slots = [];
    for (let k = 0; k < 4; k++) {
      slots.push({
        x: (0.40 + r() * 0.55) * w,
        y: (0.55 + r() * 0.35) * h,
        // Breath period in seconds + phase offset so labels pulse out of sync.
        breathPeriodS: 6 + r() * 4,               // 6–10 s
        breathPhase: r() * Math.PI * 2,
      });
    }
    return slots;
  }

  // Elevation labels — values re-sampled per frame so they tick with drift,
  // opacity gently breathes so the hero feels alive without distracting.
  function drawElevationLabels(ctx, w, h, peaks, slots, colors, tSec) {
    ctx.save();
    ctx.fillStyle = colors.accent;
    ctx.font = '9px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
    const base = colors.alphaLabel * 0.55;
    for (const s of slots) {
      // Breath: alpha multiplier in [0.55, 1.0] — never dims to zero, so
      // a label always stays legible but the field looks like it's breathing.
      const b = 0.55 + 0.45 * (0.5 + 0.5 * Math.sin(2 * Math.PI * tSec / s.breathPeriodS + s.breathPhase));
      ctx.globalAlpha = base * b;
      const z = heightAt(s.x, s.y, peaks);
      const elev = Math.round(1000 + z * 800);
      ctx.fillText(elev + 'm', s.x, s.y);
    }
    // Corner coordinate marker — elegant, just the survey label
    ctx.globalAlpha = colors.alphaLabel * 1.1;
    ctx.font = '10px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace';
    ctx.fillText('29°N  /  95°W', 24, h - 24);
    ctx.restore();
  }

  // Gleam sweep — a soft radial highlight that enters from one corner,
  // crosses the viewport, and fades. Triggered once every 45–90 s.
  function drawGleam(ctx, w, h, gleam, colors) {
    if (!gleam) return;
    // Progress is 0..1 over the whole sweep. Use a sin envelope for the alpha
    // so the highlight fades in, peaks in the middle, and fades out.
    const envelope = Math.sin(Math.PI * gleam.progress);
    if (envelope <= 0.001) return;
    // Interpolate position from start → end along the sweep vector.
    const x = gleam.x0 + (gleam.x1 - gleam.x0) * gleam.progress;
    const y = gleam.y0 + (gleam.y1 - gleam.y0) * gleam.progress;
    const radius = Math.max(w, h) * 0.55;
    const grad = ctx.createRadialGradient(x, y, 0, x, y, radius);
    // Peak alpha is 0.35 in light mode, softer in dark to avoid a white hotspot.
    const peakA = colors.isLight ? 0.35 : 0.22;
    grad.addColorStop(0,    `rgba(201, 160, 99, ${(peakA * envelope).toFixed(3)})`);
    grad.addColorStop(0.45, `rgba(201, 160, 99, ${(peakA * envelope * 0.35).toFixed(3)})`);
    grad.addColorStop(1,    'rgba(201, 160, 99, 0)');
    ctx.save();
    ctx.globalCompositeOperation = colors.isLight ? 'multiply' : 'screen';
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);
    ctx.restore();
  }

  // Animation gate — disabled by prefers-reduced-motion OR by narrow viewport
  // (to save mobile battery). Re-evaluated on every resize so rotating a
  // tablet into landscape or widening a window lights the animation back up.
  function decideMode() {
    state.animate = !reduce && window.innerWidth >= 480;
  }

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    state.dpr = dpr;
    state.w = window.innerWidth;
    state.h = window.innerHeight;
    canvas.width  = state.w * dpr;
    canvas.height = state.h * dpr;
    canvas.style.width  = state.w + 'px';
    canvas.style.height = state.h + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    // (Re)seed peaks + label slots for the new viewport size.
    state.peaks = buildPeaks(state.w, state.h);
    state.labelSlots = buildLabelSlots(state.w, state.h);
    decideMode();
    if (state.animate) {
      startLoop();
    } else {
      stopLoop();
      draw(0);                                   // single static render
    }
  }

  // Advance peak drift + LFOs by dt seconds. Peaks bounce off viewport edges
  // (with a small inset so centers never actually reach the border).
  function tick(dt, tSec) {
    if (!state.peaks) return;
    const insetX = 0.05 * state.w;
    const insetY = 0.05 * state.h;
    for (const p of state.peaks) {
      // Drift — gentle random-walk jitter plus damping so velocity stays bounded.
      p.vx += (Math.random() - 0.5) * 2.5 * dt;
      p.vy += (Math.random() - 0.5) * 2.5 * dt;
      p.vx *= 0.985;
      p.vy *= 0.985;
      p.cx += p.vx * dt;
      p.cy += p.vy * dt;
      // Edge bounce
      if (p.cx < insetX) { p.cx = insetX; p.vx = Math.abs(p.vx); }
      if (p.cx > state.w - insetX) { p.cx = state.w - insetX; p.vx = -Math.abs(p.vx); }
      if (p.cy < insetY) { p.cy = insetY; p.vy = Math.abs(p.vy); }
      if (p.cy > state.h - insetY) { p.cy = state.h - insetY; p.vy = -Math.abs(p.vy); }
      // Amplitude LFO — sinusoidal ±ampLfoDepth of ampBase.
      const phase = 2 * Math.PI * tSec / p.ampLfoPeriodS + p.ampLfoPhase;
      p.amp = p.ampBase * (1 + p.ampLfoDepth * Math.sin(phase));
    }
    // Gleam scheduling — trigger one, let it run, reset timer.
    if (!state.gleam && tSec * 1000 >= state.nextGleamAt) {
      // Random entry from any of the four corners; exit at the opposite.
      const corners = [
        [-0.15,  0.10,  1.15,  0.85], [ 1.15, 0.15, -0.15, 0.90],
        [ 0.10, -0.15,  0.85,  1.15], [ 0.20, 1.15,  0.90, -0.15],
      ];
      const c = corners[Math.floor(Math.random() * corners.length)];
      state.gleam = {
        progress: 0,
        durationS: 3.5 + Math.random() * 1.5,     // 3.5–5.0 s
        x0: c[0] * state.w, y0: c[1] * state.h,
        x1: c[2] * state.w, y1: c[3] * state.h,
      };
    }
    if (state.gleam) {
      state.gleam.progress += dt / state.gleam.durationS;
      if (state.gleam.progress >= 1) {
        state.gleam = null;
        state.nextGleamAt = tSec * 1000 + (45000 + Math.random() * 45000);  // 45–90 s
      }
    }
  }

  function loop(ts) {
    state.rafId = requestAnimationFrame(loop);
    // Pause on background tabs, and on any view that does not show the canvas.
    if (document.hidden) { state.lastFrame = 0; return; }
    const host = document.getElementById('atmos');
    if (host && host.dataset.idle === '1') { state.lastFrame = 0; return; }
    const now = ts || performance.now();
    if (!state.lastFrame) state.lastFrame = now;
    const dt = Math.min(0.1, (now - state.lastFrame) / 1000);   // clamp to 100ms for stability
    state.lastFrame = now;
    const tSec = now / 1000;
    tick(dt, tSec);
    // 15 fps throttle — the marching-squares pass is the expensive bit; at 15 fps
    // the motion still reads as smooth for this speed of drift and we leave 3×
    // frame budget headroom.
    if (now - state.lastRender >= 65) {
      state.lastRender = now;
      draw(tSec);
    }
  }

  function startLoop() {
    if (state.rafId) return;
    state.lastFrame = 0;
    state.lastRender = 0;
    state.nextGleamAt = performance.now() + 6000 + Math.random() * 8000;    // first gleam 6–14 s in
    state.rafId = requestAnimationFrame(loop);
  }
  function stopLoop() {
    if (state.rafId) { cancelAnimationFrame(state.rafId); state.rafId = 0; }
    state.gleam = null;
  }

  function draw(tSec) {
    const { accent, ink, isLight } = readColors();
    // Light-mode alphas bumped ~2.5x so the topographic field actually reads
    // against a near-white page. The contour ink in light mode is the
    // --text-primary charcoal, so higher alpha reads as legitimate map
    // darkness rather than a faded ghost.
    const colors = {
      accent, ink, isLight,
      alphaGrid:    isLight ? 0.18 : 0.10,
      alphaMinor:   isLight ? 0.22 : 0.12,
      alphaIndex:   isLight ? 0.44 : 0.26,
      alphaLabel:   isLight ? 0.62 : 0.40,
    };
    ctx.clearRect(0, 0, state.w, state.h);
    // Elevation levels — 18 lines spread across the field's dynamic range
    const levels = [];
    const N = 18;
    for (let i = 0; i < N; i++) levels.push(-1.4 + (i / (N - 1)) * 2.8);
    drawGrid(ctx, state.w, state.h, colors);
    drawContours(ctx, state.w, state.h, state.peaks, levels, colors);
    drawElevationLabels(ctx, state.w, state.h, state.peaks, state.labelSlots, colors, tSec || 0);
    // Gleam sits on top so it tints contours + labels briefly.
    drawGleam(ctx, state.w, state.h, state.gleam, colors);
  }

  // Subtle CSS-transform parallax (no canvas redraw)
  let rafPending = false;
  function scheduleParallax() {
    if (rafPending) return;
    rafPending = true;
    requestAnimationFrame(() => {
      rafPending = false;
      state.parallaxX += (state.targetParallaxX - state.parallaxX) * 0.10;
      state.parallaxY += (state.targetParallaxY - state.parallaxY) * 0.10;
      canvas.style.transform = `translate3d(${state.parallaxX.toFixed(2)}px, ${state.parallaxY.toFixed(2)}px, 0)`;
    });
  }

  window.addEventListener('resize', resize, { passive: true });
  if (!reduce) {
    window.addEventListener('mousemove', e => {
      state.targetParallaxX = (e.clientX / state.w - 0.5) * -8;
      state.targetParallaxY = (e.clientY / state.h - 0.5) * -6;
      scheduleParallax();
    }, { passive: true });
    window.addEventListener('scroll', () => {
      const sy = window.scrollY || window.pageYOffset || 0;
      state.targetParallaxY = (sy % 600) * -0.04;
      scheduleParallax();
    }, { passive: true });
  }
  // Re-render when theme flips — if the animation loop is running it'll pick
  // up the new colors on its next tick, but a one-shot redraw makes the flip
  // feel instant instead of waiting for the 65ms throttle.
  const themeObs = new MutationObserver(() => draw(performance.now() / 1000));
  themeObs.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  // When the tab returns from hidden, reset the dt baseline so drift doesn't
  // snap-advance by the clamped 100ms and push out the next gleam so it doesn't
  // fire immediately on return.
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && state.animate) {
      state.lastFrame = 0;
      state.nextGleamAt = performance.now() + 8000 + Math.random() * 6000;
    }
  });

  resize();
}