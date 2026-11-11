import { mountFrame, paintIcons } from './frame';
import { createKerf, loadChapters, type Chapter, type Film } from './media';

mountFrame();

type State = {
  size: 'desktop' | 'tablet' | 'phone';
  film: Film;
  surface: 'dark' | 'light' | 'auto';
  accent: string;
  radius: number;
  motion: boolean;
  captions: boolean;
};

const DEFAULTS: State = { size: 'desktop', film: '169', surface: 'dark', accent: '#d4f53c', radius: 20, motion: false, captions: false };
const DEVICES = {
  desktop: { max: 2400, viewport: 0, label: 'Desktop', icon: 'monitor' },
  tablet: { max: 720, viewport: 768, label: 'Tablet', icon: 'tablet' },
  phone: { max: 358, viewport: 390, label: 'Phone', icon: 'smartphone' },
} as const;

const app = document.getElementById('app')!;
const form = document.getElementById('controls') as HTMLFormElement;
const drawer = document.getElementById('drawer')!;
const slot = document.getElementById('player-slot')!;
const device = document.getElementById('device')!;
const deviceLabel = document.getElementById('device-label')!;
const stage = document.querySelector<HTMLElement>('.stage')!;
const customize = document.querySelector<HTMLButtonElement>('[data-customize]')!;

// ------------------------------------------------------------------ state, kept in the URL so a setup can be shared
function readState(): State {
  const h = new URLSearchParams(location.hash.slice(1));
  const s = { ...DEFAULTS };
  if (h.get('size') && h.get('size')! in DEVICES) s.size = h.get('size') as State['size'];
  // A portrait phone opens on the 9:16 cut: it fills the screen. The switch stays in Customize.
  if (h.get('film') === '916' || (!h.get('film') && matchMedia('(max-width: 860px) and (orientation: portrait)').matches)) s.film = '916';
  if (h.get('film') === '169') s.film = '169';
  if (['dark', 'light', 'auto'].includes(h.get('surface') ?? '')) s.surface = h.get('surface') as State['surface'];
  if (/^[0-9a-f]{6}$/i.test(h.get('accent') ?? '')) s.accent = `#${h.get('accent')!.toLowerCase()}`;
  const r = Number(h.get('radius'));
  if (r >= 8 && r <= 32) s.radius = r;
  s.motion = h.get('motion') === 'reduce';
  s.captions = h.get('captions') === 'on';
  return s;
}

function writeState(s: State) {
  const h = new URLSearchParams();
  for (const k of ['size', 'surface', 'radius'] as const) if (s[k] !== DEFAULTS[k]) h.set(k, String(s[k]));
  if (s.film !== initialFilm) h.set('film', s.film);
  if (s.accent !== DEFAULTS.accent) h.set('accent', s.accent.slice(1));
  if (s.motion) h.set('motion', 'reduce');
  if (s.captions) h.set('captions', 'on');
  history.replaceState(null, '', h.toString() ? `#${h}` : location.pathname);
}

let state = readState();
const initialFilm = state.film;

function syncForm(s: State) {
  for (const k of ['size', 'film', 'surface'] as const) {
    const el = form.querySelector<HTMLInputElement>(`input[name="${k}"][value="${s[k]}"]`);
    if (el) el.checked = true;
  }
  const preset = form.querySelector<HTMLInputElement>(`input[name="accent"][value="${s.accent}"]`);
  form.querySelectorAll<HTMLInputElement>('input[name="accent"]').forEach((i) => (i.checked = i === preset));
  const custom = form.querySelector<HTMLInputElement>('input[name="custom"]')!;
  custom.closest('label')!.classList.toggle('is-on', !preset);
  if (!preset) custom.value = s.accent;
  custom.closest<HTMLElement>('label')!.style.setProperty('--sw', custom.value);
  (form.elements.namedItem('radius') as HTMLInputElement).value = String(s.radius);
  paintRange(s.radius);
  (form.elements.namedItem('motion') as HTMLInputElement).checked = s.motion;
  (form.elements.namedItem('captions') as HTMLInputElement).checked = s.captions;
}

function paintRange(r: number) {
  (form.elements.namedItem('radius') as HTMLInputElement).style.setProperty('--pct', `${((r - 8) / 24) * 100}%`);
}

// ------------------------------------------------------------------ colour helpers
function luminance(hex: string) {
  const c = [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16) / 255).map((v) => (v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4));
  return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
}
const contrast = (a: string, b: string) => {
  const [x, y] = [luminance(a), luminance(b)].sort((m, n) => n - m);
  return (x + 0.05) / (y + 0.05);
};
const inkOn = (hex: string) => (contrast(hex, '#141416') >= contrast(hex, '#ffffff') ? '#141416' : '#ffffff');

// ------------------------------------------------------------------ the player
let player: HTMLElement | null = null;
let kerf: HTMLElement | null = null;
let mountedFilm: Film | null = null;

function mount(film: Film, resumeAt = 0) {
  slot.replaceChildren();
  player = createKerf(film);
  slot.append(player);
  mountedFilm = film;
  kerf = null;
  const wait = () => {
    kerf = slot.querySelector<HTMLElement>('.kerf');
    if (!kerf) return requestAnimationFrame(wait);
    applyPlayer(state);
    if (resumeAt) mediaEl()?.addEventListener('loadedmetadata', () => (mediaEl()!.currentTime = resumeAt), { once: true });
  };
  wait();
}

const mediaEl = () => slot.querySelector<HTMLMediaElement>('mux-video, video');

function applyPlayer(s: State) {
  if (!kerf) return;
  kerf.dataset.surface = s.surface;
  kerf.style.setProperty('--media-accent-color', s.accent);
  kerf.style.setProperty('--media-accent-text-color', inkOn(s.accent));
  kerf.style.setProperty('--media-border-radius', `${s.radius}px`);
  if (s.motion) kerf.dataset.motion = 'reduce';
  else delete kerf.dataset.motion;
  const m = mediaEl();
  const tracks = m?.textTracks;
  if (tracks) for (const t of Array.from(tracks)) if (t.kind === 'captions') t.mode = s.captions ? 'showing' : 'disabled';
}

// ------------------------------------------------------------------ sizing: the player fits the stage, never the other way round
const compact = matchMedia('(max-width: 860px)');

function fit() {
  // On a phone screen the player simply takes the stage; the size switch only means something on a large screen.
  const d = compact.matches ? DEVICES.desktop : DEVICES[state.size];
  const ratio = state.film === '916' ? 9 / 16 : 16 / 9;
  const r = stage.getBoundingClientRect();
  const gutter = compact.matches ? 16 : 48;
  // Room for the stage padding, the one-line film bar and the device guide. Constants, so the player's width never
  // feeds back into its own height.
  const reserved = compact.matches ? 36 : 48 + 22 + 36 + (d.viewport ? 62 : 0);
  const byW = r.width - gutter * 2;
  const byH = (r.height - reserved) * ratio;
  const w = Math.max(140, Math.floor(Math.min(d.max, byW, byH)));
  stage.toggleAttribute('data-narrow', w < 640);
  stage.style.setProperty('--player-w', `${w}px`);
  stage.style.setProperty('--ratio', state.film === '916' ? '9 / 16' : '16 / 9');
  device.dataset.device = state.size;
  const vw = d.viewport ? Math.min(d.viewport, byW + 8) : 0;
  stage.style.setProperty('--viewport-w', vw ? `${vw}px` : '0px');
  deviceLabel.innerHTML = `<i data-lucide="${d.icon}"></i><span>${d.label}</span><span class="mono">${d.viewport ? `${d.viewport} px viewport, ` : ''}${w} px player</span>`;
  paintIcons();
}
const ro = new ResizeObserver(fit);
ro.observe(stage);
compact.addEventListener('change', fit);

// ------------------------------------------------------------------ the code a host product would write
function code(s: State) {
  const attrs = [`class="media-skin kerf"`, `data-theme="kerf"`, `data-preset="video"`];
  if (s.surface !== 'dark') attrs.push(`data-surface="${s.surface}"`);
  if (s.motion) attrs.push(`data-motion="reduce"`);
  const t = (x: string, c: string) => `<span class="t-${c}">${x}</span>`;
  return [
    `${t('/* your stylesheet */', 'c')}`,
    `${t('.kerf', 's')} {`,
    `  ${t('--media-accent-color', 'p')}: ${t(s.accent, 'v')};`,
    `  ${t('--media-border-radius', 'p')}: ${t(`${s.radius}px`, 'v')};`,
    `}`,
    ``,
    `${t('<!-- the skin root in your markup -->', 'c')}`,
    `${t('&lt;media-container', 's')}`,
    ...attrs.map((a) => `  ${t(a.split('=')[0], 'p')}=${t(a.split('=')[1], 'v')}`),
    `${t('&gt;', 's')}`,
  ].join('\n');
}

// ------------------------------------------------------------------ apply everything
function apply(s: State, opts: { remount?: boolean } = {}) {
  state = s;
  writeState(s);
  document.documentElement.style.setProperty('--accent', s.accent);
  document.documentElement.style.setProperty('--accent-ink', inkOn(s.accent));
  document.getElementById('accent-out')!.textContent = s.accent.toUpperCase();
  document.getElementById('radius-out')!.textContent = `${s.radius} = ${s.radius - 6} + 6`;
  const lightFrame = s.surface === 'light' || (s.surface === 'auto' && matchMedia('(prefers-color-scheme: light)').matches);
  document.getElementById('accent-note')!.hidden = !(lightFrame && contrast(s.accent, '#fdfdfc') < 3);
  document.getElementById('code')!.innerHTML = code(s);
  if (opts.remount || mountedFilm !== s.film) mount(s.film, mediaEl()?.currentTime ?? 0);
  else applyPlayer(s);
  fit();
}

form.addEventListener('input', (e) => {
  const el = e.target as HTMLInputElement;
  const next = { ...state };
  if (el.name === 'custom') {
    next.accent = el.value;
    el.closest<HTMLElement>('label')!.style.setProperty('--sw', el.value);
    form.querySelectorAll<HTMLInputElement>('input[name="accent"]').forEach((i) => (i.checked = false));
    el.closest('label')!.classList.add('is-on');
  } else if (el.name === 'accent') {
    next.accent = el.value;
    form.querySelector('.swatch-custom')!.classList.remove('is-on');
  } else if (el.name === 'radius') next.radius = Number(el.value);
  else if (el.name === 'motion') next.motion = el.checked;
  else if (el.name === 'captions') next.captions = el.checked;
  else if (el.name === 'film') {
    // The 9:16 cut is a phone film: it opens at phone size, and the size switch stays free afterwards.
    next.film = el.value as Film;
    next.size = next.film === '916' ? 'phone' : 'desktop';
    form.querySelector<HTMLInputElement>(`input[name="size"][value="${next.size}"]`)!.checked = true;
  } else if (el.name === 'size' || el.name === 'surface') (next as Record<string, unknown>)[el.name] = el.value;
  apply(next);
});

form.addEventListener('reset', (e) => {
  e.preventDefault();
  syncForm(DEFAULTS);
  apply({ ...DEFAULTS });
});

form.querySelector('[data-copy]')!.addEventListener('click', async (e) => {
  const btn = e.currentTarget as HTMLButtonElement;
  const text = document.getElementById('code')!.textContent ?? '';
  try {
    await navigator.clipboard.writeText(text);
    btn.querySelector('span')!.textContent = 'Copied';
  } catch {
    const range = document.createRange();
    range.selectNodeContents(document.getElementById('code')!);
    getSelection()?.removeAllRanges();
    getSelection()?.addRange(range);
    btn.querySelector('span')!.textContent = 'Selected';
  }
  setTimeout(() => (btn.querySelector('span')!.textContent = 'Copy'), 1600);
});

// ------------------------------------------------------------------ the drawer pushes the stage, it never covers it
function setDrawer(open: boolean, focus = true) {
  app.dataset.drawer = open ? 'open' : 'closed';
  customize.setAttribute('aria-expanded', String(open));
  drawer.toggleAttribute('inert', !open);
  if (open && focus) form.querySelector<HTMLElement>('input:checked')?.focus({ preventScroll: true });
  if (!open && focus) customize.focus();
}
customize.addEventListener('click', () => setDrawer(app.dataset.drawer !== 'open'));
drawer.querySelector('[data-close]')!.addEventListener('click', () => setDrawer(false));
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && app.dataset.drawer === 'open' && drawer.contains(document.activeElement)) setDrawer(false);
});
// Keep the stage re-fitting while the drawer slides.
app.addEventListener('transitionrun', () => {
  const t0 = performance.now();
  const tick = () => {
    fit();
    if (performance.now() - t0 < 600) requestAnimationFrame(tick);
  };
  tick();
});

// ------------------------------------------------------------------ chapters under the player seek the film
loadChapters().then((chapters: Chapter[]) => {
  const list = document.getElementById('chapters')!;
  const fmt = (t: number) => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, '0')}`;
  list.innerHTML = chapters
    .map((c, i) => `<li><button type="button" data-t="${c.start}"><span class="mono">${String(i + 1).padStart(2, '0')}</span>${c.title}<span class="mono dim">${fmt(c.start)}</span></button></li>`)
    .join('');
  list.addEventListener('click', (e) => {
    const b = (e.target as Element).closest<HTMLButtonElement>('button[data-t]');
    const m = mediaEl();
    if (!b || !m) return;
    m.currentTime = Number(b.dataset.t) + 0.05;
    m.play().catch(() => {});
  });
  const mark = () => {
    const m = mediaEl();
    if (!m) return;
    const now = m.currentTime;
    list.querySelectorAll<HTMLButtonElement>('button').forEach((b, i) => {
      const on = now >= chapters[i].start && now < chapters[i].end;
      b.toggleAttribute('data-current', on);
    });
  };
  document.addEventListener('timeupdate', mark, true);
});

syncForm(state);
setDrawer(matchMedia('(min-width: 1180px)').matches && location.hash.length > 1, false);
fit();
apply(state, { remount: true });
// Size changes animate only after the first paint, so the player loads at its final size.
requestAnimationFrame(() => requestAnimationFrame(() => document.body.classList.add('is-ready')));
