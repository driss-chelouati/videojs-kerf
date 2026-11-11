// Behaviour for the frame every site page shares. The markup itself is written into the HTML at build time
// (frame-markup.ts, through the Vite plugin), so this only wires the controls.
import { ArrowRight, Monitor, Smartphone, Tablet, createIcons } from 'lucide';

// Icons drawn after load (the device label); everything else is inline in the HTML already.
export const paintIcons = () =>
  createIcons({ icons: { ArrowRight, Monitor, Smartphone, Tablet }, attrs: { 'stroke-width': 1.75, 'aria-hidden': 'true' } });

const store = {
  set: (k: string, v: string) => {
    try {
      localStorage.setItem(k, v);
    } catch {
      /* private mode: the page still works, it just forgets */
    }
  },
};

export function siteIsDark(): boolean {
  const t = document.documentElement.dataset.theme;
  return t ? t === 'dark' : !matchMedia('(prefers-color-scheme: light)').matches;
}

export function mountFrame(): void {
  const root = document.documentElement;

  document.querySelector('[data-dismiss]')?.addEventListener('click', () => {
    root.dataset.announce = 'hidden';
    store.set('kerf-announce', 'hidden');
  });

  document.querySelector('[data-theme-toggle]')?.addEventListener('click', () => {
    root.dataset.theme = siteIsDark() ? 'light' : 'dark';
    store.set('kerf-site-theme', root.dataset.theme);
    document.dispatchEvent(new CustomEvent('kerf:theme'));
  });

  const keysBtn = document.querySelector<HTMLButtonElement>('[data-keys]');
  const keys = document.getElementById('keys');
  if (!keysBtn || !keys) return;
  const setKeys = (open: boolean) => {
    keys.hidden = !open;
    keysBtn.setAttribute('aria-expanded', String(open));
  };
  keysBtn.addEventListener('click', () => setKeys(keys.hidden === true));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !keys.hidden) {
      setKeys(false);
      keysBtn.focus();
    }
  });
  document.addEventListener('pointerdown', (e) => {
    if (!keys.hidden && !(e.target as Element).closest('.pop-wrap')) setKeys(false);
  });
}
