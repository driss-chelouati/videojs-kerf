// Build-time markup for the frame every site page shares (announcement, top bar, footer), and inline Lucide icons.
// Vite writes it into the HTML, so the first paint already has the whole frame: no flash when moving between pages.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import * as lucide from 'lucide';

const here = (f: string) => fileURLToPath(new URL(`./apps/preview/src/site/${f.replace('./', '')}`, import.meta.url));
const lockup = readFileSync(here('./kerf-lockup.svg'), 'utf8').trim();
const videojsLogo = readFileSync(here('./videojs-logo.svg'), 'utf8').trim();

type Node = [string, Record<string, string | number>, Node[]?];

const pascal = (name: string) => name.replace(/(^|-)([a-z0-9])/g, (_, __, c: string) => c.toUpperCase());

export function icon(name: string): string {
  const node = (lucide as unknown as Record<string, Node>)[pascal(name)];
  if (!node) throw new Error(`Unknown Lucide icon: ${name}`);
  const draw = ([tag, attrs, children = []]: Node): string =>
    `<${tag} ${Object.entries(attrs)
      .map(([k, v]) => `${k}="${v}"`)
      .join(' ')}>${children.map(draw).join('')}</${tag}>`;
  const [, attrs, children = []] = node;
  const a = { ...attrs, 'stroke-width': 1.75, class: `lucide lucide-${name}`, 'aria-hidden': 'true' };
  return draw(['svg', a, children]);
}

/** Replaces every `<i data-lucide="name"></i>` with the icon's SVG. */
export const inlineIcons = (html: string) => html.replace(/<i data-lucide="([a-z0-9-]+)"><\/i>/g, (_, n: string) => icon(n));

const SHORTCUTS: [string, string][] = [
  ['Space or K', 'Play or pause'],
  ['← →', 'Seek 5 seconds'],
  ['J L', 'Seek 10 seconds'],
  ['↑ ↓', 'Volume'],
  ['M', 'Mute'],
  ['C', 'Captions'],
  ['F', 'Fullscreen'],
  ['< >', 'Speed'],
  ['0 to 9', 'Jump to 0 to 90 %'],
];

const keys = SHORTCUTS.map(
  ([k, v]) =>
    `<dt>${k
      .split(' ')
      .map((x) => (x === 'or' || x === 'to' ? `<span>${x}</span>` : `<kbd>${x.replace('<', '&lt;').replace('>', '&gt;')}</kbd>`))
      .join('')}</dt><dd>${v}</dd>`,
).join('');

// Runs in <head> before the first paint: the saved theme and the dismissed announcement never flash.
const boot = `<script>(function(){try{var t=localStorage.getItem('kerf-site-theme');if(t==='light'||t==='dark')document.documentElement.dataset.theme=t;if(localStorage.getItem('kerf-announce')==='hidden')document.documentElement.dataset.announce='hidden'}catch(e){}})()</script>`;

export function frameHead(): string {
  return boot;
}

export function frameTop(page: 'player' | 'design'): string {
  const end =
    page === 'player'
      ? `<button class="btn btn--quiet" type="button" aria-expanded="false" aria-controls="drawer" data-customize>${icon('sliders-horizontal')}<span>Customize</span></button>`
      : `<a class="btn btn--quiet" href="./index.html"><span>Try the player</span>${icon('arrow-right')}</a>`;
  return `
    <div class="announce" id="announce">
      <p><span class="announce-mark" aria-hidden="true"></span>Kerf is an entry to the Video.js 10 Skins Challenge.
      ${page === 'player' ? `<a href="./design.html">Read the design notes${icon('arrow-right')}</a>` : `<a href="./index.html">Play the film${icon('arrow-right')}</a>`}</p>
      <button class="icon-btn icon-btn--sm" type="button" aria-label="Dismiss" data-dismiss>${icon('x')}</button>
    </div>
    <header class="topbar">
      <a class="brand" href="./index.html" aria-label="Kerf, home">${lockup}</a>
      <nav class="pillnav" aria-label="Pages">
        <a href="./index.html"${page === 'player' ? ' aria-current="page"' : ''}>Player</a>
        <a href="./design.html"${page === 'design' ? ' aria-current="page"' : ''}>Design</a>
      </nav>
      <div class="topbar-end">
        <div class="pop-wrap">
          <button class="icon-btn" type="button" aria-label="Keyboard shortcuts" aria-expanded="false" aria-controls="keys" data-keys>${icon('keyboard')}</button>
          <div class="pop" id="keys" role="dialog" aria-label="Keyboard shortcuts" hidden>
            <p class="pop-title">Keyboard</p>
            <dl>${keys}</dl>
          </div>
        </div>
        <button class="icon-btn" type="button" aria-label="Switch theme" data-theme-toggle>${icon('sun-moon')}</button>
        ${end}
      </div>
    </header>`;
}

export function frameFoot(): string {
  return `
    <footer class="foot">
      <a class="foot-brand" href="./index.html" aria-label="Kerf">${lockup}</a>
      <p class="foot-line">A Video.js 10 skin by <a href="https://drisschelouati.dev" target="_blank" rel="noopener">Driss Chelouati</a>. Film: the Sparvek launch, by Orvio. Apache 2.0.</p>
      <a class="powered" href="https://videojs.org" target="_blank" rel="noopener"><span>Powered by</span><span class="vjs-logo" role="img" aria-label="Video.js">${videojsLogo}</span></a>
    </footer>`;
}
