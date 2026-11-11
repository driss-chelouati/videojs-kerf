import { mountFrame, paintIcons } from './frame';
import { geoSvg, place, player } from './drawn';

mountFrame();

const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const $ = (id: string) => document.getElementById(id)!;
const put = (id: string, html: string) => $(id).insertAdjacentHTML('beforeend', html);

// ------------------------------------------------------------------ the drawn players (ported from the approved board)
const fit = (el: HTMLElement) => Math.round(el.clientWidth);

function render() {
  for (const id of ['hero-player', 'scrub', 'menu', 'layer-1', 'layer-2', 'layer-3']) {
    $(id).querySelectorAll('.kd, .num.pin').forEach((n) => n.remove());
  }
  put('hero-player', player({ w: fit($('hero-player')), img: './stills/w21.jpg', t: 21.4, buf: 31 }));
  put('scrub', player({ w: fit($('scrub')), img: './stills/w19.jpg', t: 19.4, buf: 27, playing: true, scrub: { t: 28.5, img: './stills/w27.jpg' } }));
  put('menu', player({ w: fit($('menu')), img: './stills/w11.jpg', t: 11.6, buf: 22, menu: 'main', cc: true }));

  const sw = $('states').clientWidth;
  const w = sw < 760 ? sw : Math.round((sw - 2 * 28) / 3);
  const states: [Record<string, unknown>, string, string][] = [
    [{ img: './stills/w25.6.jpg', t: 25.6, hidden: true, playing: true }, 'Playing', 'The controls sink; the frame keeps a 2 px rail of progress.'],
    [{ img: './stills/w23.2.jpg', t: 0, buf: 6, poster: true, hidden: true }, 'Ready', 'The picture stays whole until you reach for it; the play tile waits in its frame.'],
    [{ img: './stills/w30.jpg', t: 30.2, buf: 30.4, loading: true, playing: true }, 'Loading', 'The official spinner in the same tile.'],
    [{ img: './stills/w19.jpg', t: 19.3, vol: 72, playing: true }, 'Volume', 'A vertical slider rises from mute.'],
    [{ img: './stills/w43.jpg', t: 41.5, buf: 46, menu: 'speed', playing: true }, 'Speed', 'Six rates as chips; keyboard focus on the chosen one.'],
    [{ img: './stills/w12.4.jpg', t: 12.4, buf: 20, focus: 'thumb', status: { icon: 'seek', text: '+5 s', of: '0:12' }, playing: true }, 'Keyboard seek', 'Focus on the blade; feedback hangs from the top edge.'],
    [{ img: './stills/w36.jpg', t: 34.6, cc: true, capText: 'Your turn.', playing: true, tip: { b: 'mute', text: 'Mute', key: 'M' }, hov: 'mute' }, 'Captions and tooltip', 'Captions on the frame colour, the tooltip from its button.'],
    [{ img: './stills/w27.jpg', t: 27.2, hov: 'play', focus: 'fs' }, 'Hover and focus', 'Play takes the accent; the focus ring is ink with a cut.'],
    [{ img: './stills/w30.jpg', t: 8, buf: 9, err: true }, 'Error', 'The error rises from the band like everything else.'],
  ];
  $('states').innerHTML = states
    .map(([o, name, d], i) => `<figure class="cell tilt" style="--i:${i % 3}">${player({ w, ...o })}<figcaption><b>${name}.</b> ${d}</figcaption></figure>`)
    .join('');

  const phw = $('phones').clientWidth;
  const pw = phw < 760 ? Math.min(360, phw) : Math.min(340, Math.round((phw - 2 * 28) / 3));
  const phones: [Record<string, unknown>, string, string][] = [
    [{ ratio: '9/16', img: './stills/p21.jpg', t: 21.2, buf: 30, cc: true, capText: 'Odile, sales intake.' }, '9:16 cut', 'Captions on.'],
    [{ ratio: '9/16', img: './stills/p25.jpg', t: 25.2, buf: 33, playing: true, scrub: { t: 21.2, img: './stills/p21.jpg' } }, 'Scrubbing', 'A portrait storyboard frame.'],
    [{ img: './stills/w11.jpg', t: 11.2, buf: 19, menu: 'main' }, '16:9 at phone width', 'Captions move into settings.'],
  ];
  $('phones').innerHTML = phones
    .map(([o, n, d], i) => `<figure class="cell tilt" style="--i:${i}">${player({ w: pw, ...o })}<figcaption><b>${n}.</b> ${d}</figcaption></figure>`)
    .join('');

  // Exploded view: the same drawing, split into its three layers by CSS.
  const lw = Math.min(760, Math.round(innerWidth * (innerWidth < 760 ? 0.86 : 0.58)));
  const base = { w: lw, img: './stills/w21.jpg', t: 21.4, buf: 31, scrub: { t: 28.5, img: './stills/w27.jpg' }, status: { icon: 'seek', text: '+5 s', of: '0:26' } };
  for (const id of ['layer-1', 'layer-2', 'layer-3']) put(id, player(base));

  requestAnimationFrame(() => {
    place(document);
    pins();
    document.querySelectorAll('.cell').forEach((el) => io.observe(el));
  });
}

function pins() {
  const host = $('hero-player');
  const k = host.querySelector<HTMLElement>('.kd');
  if (!k) return;
  const hr = host.getBoundingClientRect();
  const at = (el: Element | null | undefined, fx: number, fy: number, n: number) => {
    if (!el) return;
    const r = el.getBoundingClientRect();
    host.insertAdjacentHTML('beforeend', `<span class="num pin" style="left:${r.left - hr.left + r.width * fx}px;top:${r.top - hr.top + r.height * fy}px">${n}</span>`);
  };
  at(k, 0.985, 0.035, 1);
  at(k.querySelector('.k-timetab'), 0.5, -0.5, 2);
  at(k.querySelector('.k-bar'), 0.62, 0.95, 3);
  at(k.querySelectorAll('.k-ch')[1], 0, -1.6, 4);
  at(k.querySelector('.k-thumb'), 0.5, -0.65, 5);
  at(k.querySelector('[data-b="gear"]'), 0.5, -0.25, 6);
}

// ------------------------------------------------------------------ reveal on entry
const io = new IntersectionObserver(
  (entries) => {
    for (const e of entries)
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
  },
  { rootMargin: '0px 0px -10% 0px' },
);
document.querySelectorAll('.sec, .thinking, .closer').forEach((el) => io.observe(el));

render();
let rw = innerWidth;
addEventListener('resize', () => {
  if (Math.abs(innerWidth - rw) > 40) {
    rw = innerWidth;
    render();
  }
});

$('geo').innerHTML = geoSvg();

// ------------------------------------------------------------------ the design thinking lights up word by word as you read
document.querySelectorAll<HTMLElement>('.reveal-text p').forEach((p) => {
  p.innerHTML = p.textContent!.split(/(\s+)/).map((w) => (w.trim() ? `<span class="w">${w}</span>` : w)).join('');
});

// ------------------------------------------------------------------ tilt and spotlight follow the pointer (fine pointers only)
if (!reduce && matchMedia('(hover: hover) and (pointer: fine)').matches) {
  let current: HTMLElement | null = null;
  document.addEventListener('pointermove', (e) => {
    const t = (e.target as Element).closest<HTMLElement>('.tilt');
    if (current && current !== t) {
      current.classList.remove('is-tilting');
      current = null;
    }
    if (!t) return;
    current = t;
    const r = t.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width;
    const y = (e.clientY - r.top) / r.height;
    t.classList.add('is-tilting');
    t.style.setProperty('--rx', `${(0.5 - y) * 5}deg`);
    t.style.setProperty('--ry', `${(x - 0.5) * 7}deg`);
    t.style.setProperty('--mx', `${x * 100}%`);
    t.style.setProperty('--my', `${y * 100}%`);
  });
}
