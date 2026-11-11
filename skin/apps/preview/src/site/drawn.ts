// @ts-nocheck
// Static drawings of the Kerf skin for the design page (anatomy, exploded view), ported from the approved board.
// Every live state on the site is the real skin; these are labelled drawings.
import * as V from '@videojs/html/icons/default';

const KI: Record<string, string> = Object.fromEntries(
  Object.entries(V)
    .filter(([, v]) => typeof v === 'string')
    .map(([k, v]) => [k.replace(/Icon$/, ''), (v as string).replace(/ width="18" height="18"/, '')]),
);
const D = 46;
const CH: [number, number, string][] = [[0, 10, 'The sameness'], [10, 17, 'Art direction'], [17, 28, 'The cast'], [28, 33, 'Every page'], [33, 46, 'Your turn']];
const I = (n: string) => KI[n];
const fmt = (s: number) => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
const clamp = (v: number, a = 0, b = 1) => Math.max(a, Math.min(b, v));

export function player(o: any): string {
  const t = o.t ?? 21, buf = o.buf ?? Math.min(D, t + 8), ptr = o.scrub ? o.scrub.t : null;
  const segs = CH.map(([s, e]) => {
    const f = clamp((t - s) / (e - s)), b = clamp((buf - s) / (e - s));
    const p = ptr != null && ptr > t ? clamp((ptr - s) / (e - s)) : 0;
    const hl = ptr != null && ptr >= s && ptr < e;
    return `<div class="k-ch${hl ? ' hl' : ''}" style="flex:${e - s} 1 0"><i class="buf" style="width:${b * 100}%"></i>${p ? `<i class="ptr" style="width:${p * 100}%"></i>` : ''}<i class="fill" style="width:${f * 100}%"></i></div>`;
  }).join('');
  const btn = (cls, icon, extra = '') => `<span class="k-btn ${cls}" data-b="${cls.split(' ')[0]}">${I(icon)}${extra}</span>`;
  const hov = o.hov || '', foc = o.focus || '';
  const st = k => (hov === k ? ' hov' : '') + (foc === k ? ' focus' : '');
  const playing = !!o.playing;
  const bar = `
    <div class="k-bar"><span class="vc r"></span>
      ${btn('play' + st('play') + (o.err ? ' dis' : ''), playing ? 'pause' : 'play')}
      <div class="k-seek${ptr != null ? ' pointing' : ''}">
        <div class="k-track">${segs}</div>
        ${ptr != null ? `<span class="k-hair" style="left:${ptr / D * 100}%"></span>` : ''}
        <span class="k-thumb${foc === 'thumb' ? ' focus' : ''}" style="left:${t / D * 100}%"></span>
      </div>
      ${btn('mute' + st('mute') + (o.vol != null ? ' hov' : ''), o.muted ? 'volumeOff' : 'volumeHigh')}
      ${btn('cc' + st('cc') + (o.cc ? ' on' : ''), o.cc ? 'captionsOn' : 'captionsOff')}
      ${btn('gear' + st('gear') + (o.menu ? ' hov' : ''), 'gear')}
      ${btn('fs' + st('fs'), o.fs ? 'fullscreenExit' : 'fullscreenEnter')}
    </div>`;
  const timetab = o.scrub ? '' : `<div class="k-timetab"><span class="vc l"></span><b>${fmt(t)}</b><span class="of">/ ${fmt(D)}</span><span class="fl br"></span></div>`;
  let pops = '';
  if (o.scrub) {
    const pw = o.ratio === '9/16' ? 96 : (o.w < 560 ? 156 : 196);
    const ph = o.ratio === '9/16' ? Math.round(pw * 16 / 9) : Math.round(pw * 9 / 16);
    const ch = CH.find(c => o.scrub.t >= c[0] && o.scrub.t < c[1]);
    pops += `<div class="k-tab k-preview" data-x="${o.scrub.t / D}" style="width:${pw + 12}px"><span class="fl bl"></span><span class="fl br"></span>
      <img src="${o.scrub.img}" style="width:${pw}px;height:${ph}px" alt="">
      <div class="meta">${o.ratio === '9/16' ? `<span style="color:inherit;font-weight:500">${fmt(o.scrub.t)}</span>` : `<b>${ch[2]}</b><span>${fmt(o.scrub.t)}</span>`}</div></div>`;
  }
  if (o.vol != null) pops += `<div class="k-tab k-vol" data-anchor="mute"><span class="fl bl"></span><span class="fl br"></span><span class="pct">${o.vol}</span><div class="vt"><i style="height:${o.vol}%"></i><b style="bottom:${o.vol}%"></b></div></div>`;
  if (o.tip) pops += `<div class="k-tab k-tip" data-anchor="${o.tip.b}"><span class="fl bl"></span><span class="fl br"></span>${o.tip.text}<kbd>${o.tip.key}</kbd></div>`;
  if (o.menu === 'main') pops += `<div class="k-tab k-menu"><span class="vc r"></span><span class="fl bl"></span>
      ${o.w < 560 ? `<div class="k-mi"><span class="ic">${I('captionsOff')}</span>Captions<span class="hint">Off</span><span class="chev">${I('chevron')}</span></div>` : ''}
      <div class="k-mi hl${o.kbItem ? ' kb' : ''}"><span class="ic">${I('speed')}</span>Speed<span class="hint">1.25×</span><span class="chev">${I('chevron')}</span></div>
      ${o.w >= 560 ? `<div class="k-mi"><span class="ic">${I('captionsOn')}</span>Captions<span class="hint">English</span><span class="chev">${I('chevron')}</span></div>` : ''}
      <div class="k-mi"><span class="ic">${I('quality')}</span>Quality<span class="hint">Auto, 1080p</span><span class="chev">${I('chevron')}</span></div></div>`;
  if (o.menu === 'speed') pops += `<div class="k-tab k-menu"><span class="vc r"></span><span class="fl bl"></span>
      <div class="mh">${I('chevron')}Speed</div>
      <div class="k-rates">${['0.5×', '0.75×', '1×', '1.25×', '1.5×', '2×'].map(v => `<span class="${v === '1.25×' ? 'sel kb' : ''}">${v}</span>`).join('')}</div></div>`;
  if (o.err) pops += `<div class="k-tab k-err" data-center><span class="fl bl"></span><span class="fl br"></span>
      <b class="k-err-t">Something went wrong.</b><p>The film could not load. Check the connection, then press play again.</p>
      <div class="acts"><span class="pri">OK</span></div></div>`;
  const status = o.status ? `<div class="k-status"><span class="fl tl"></span><span class="fl tr"></span>${I(o.status.icon)}<b style="font-weight:500">${o.status.text}</b>${o.status.of ? `<span class="of">${o.status.of}</span>` : ''}</div>` : '';
  const big = o.poster ? `<div class="k-big play">${I('play')}</div>` : o.loading ? `<div class="k-big spin">${I('spinner')}</div>` : '';
  const cap = o.capText ? `<div class="k-cap${o.hidden ? ' low' : ''}"><span>${o.capText}</span></div>` : '';
  return `<div aria-hidden="true" class="kd${o.hidden ? ' hidden' : ''}${o.poster ? ' poster' : ''}" data-theme="${o.theme || 'dark'}"${o.fs ? ' data-fs' : ''} style="width:${o.w}px;${o.accent ? `--media-accent-color:${o.accent};` : ''}${o.radius ? `--media-border-radius:${o.radius}px;` : ''}">
    <div class="k-win" style="aspect-ratio:${o.ratio || '16/9'}">
      <img class="k-media" src="${o.img}" alt="">
      ${o.loading || o.err ? '<div class="k-dim"></div>' : ''}
      ${big}${status}
      <div class="k-controls"${o.hidden ? ' data-hidden' : ''}>${timetab}${bar}${pops}</div>
      ${cap}
    </div>
    <div class="k-rail"><i style="width:${t / D * 100}%"></i></div>
  </div>`;
}

export function place(root: ParentNode): void {
  root.querySelectorAll<HTMLElement>('.kd').forEach(k => {
    const win = k.querySelector<HTMLElement>('.k-win')!, W = win.clientWidth;
    k.querySelectorAll<HTMLElement>('.k-tab').forEach(tab => {
      const tw = tab.offsetWidth;
      let x = null;
      if (tab.dataset.anchor) { const b = k.querySelector<HTMLElement>(`[data-b="${tab.dataset.anchor}"]`)!; x = b.offsetLeft + b.offsetWidth / 2; }
      if (tab.dataset.x) { const s = k.querySelector<HTMLElement>('.k-seek')!; x = s.offsetLeft + s.offsetWidth * +tab.dataset.x; }
      if (tab.hasAttribute('data-center')) x = W / 2;
      if (x != null) tab.style.left = Math.round(clamp(x - tw / 2, 14, W - tw - 14)) + 'px';
    });
  });
}

export function geoSvg(): string {
  // Bottom-left corner of the player at 1 px = 1 unit, y down; the frame's bottom edge is y = 100.
  const chip = (x: number, y: number, t: string, anchor = 'start') => {
    const w = t.length * 2.1 + 3.6, x0 = anchor === 'end' ? x - w : x;
    return `<g><rect x="${x0}" y="${y - 3.7}" width="${w}" height="7" rx="1.8" fill="#fff" stroke="rgb(20 20 22 / .12)" stroke-width=".25"/><text x="${x0 + 1.6}" y="${y + 1.1}" font-size="3.5" font-family="Geist Mono, monospace" font-weight="500" fill="#141416">${t}</text></g>`;
  };
  const lead = (x1: number, y1: number, x2: number, y2: number) => `<path d="M${x1},${y1} L${x2},${y2}" stroke="#141416" stroke-width=".3"/><circle cx="${x2}" cy="${y2}" r=".9" fill="#141416"/>`;
  return `<svg viewBox="-34 -8 196 124" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" aria-label="Notch geometry">
    <defs><pattern id="dots" width="3" height="3" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r=".45" fill="rgb(20 20 22 / .14)"/></pattern></defs>
    <path d="M0,-8 H162 V100 H20 A20,20 0 0 1 0,80 Z" fill="#141416"/>
    <path d="M6,-8 V0 A14,14 0 0 0 20,14 H92 A10,10 0 0 1 102,24 V34 A10,10 0 0 0 112,44 H162 V-8 Z" fill="#d4f53c"/>
    <path d="M6,-8 V0 A14,14 0 0 0 20,14 H92 A10,10 0 0 1 102,24 V34 A10,10 0 0 0 112,44 H162 V-8 Z" fill="url(#dots)"/>
    <rect x="6" y="50" width="44" height="44" rx="14" fill="rgb(255 255 255 / .08)" stroke="rgb(255 255 255 / .5)" stroke-width=".35" stroke-dasharray="1.2 1.2"/>
    <g transform="translate(19 63)" style="color:#f5f5f3">${KI.play.replace('<svg', '<svg width="18" height="18"')}</g>
    <text x="14" y="32.3" font-size="5.2" font-family="Geist, sans-serif" font-weight="500" fill="#f5f5f3">0:21 <tspan fill="rgb(245 245 243 / .62)">/ 0:46</tspan></text>
    <rect x="62" y="69" width="100" height="6" rx="3" fill="rgb(255 255 255 / .14)"/>
    <rect x="62" y="69" width="44" height="6" rx="3" fill="#d4f53c"/>
    <rect x="104" y="62" width="4" height="20" rx="2" fill="#f5f5f3" stroke="#141416" stroke-width="3" paint-order="stroke"/>
    <circle cx="20" cy="80" r="20" fill="none" stroke="rgb(212 245 60 / .55)" stroke-width=".35" stroke-dasharray="1 1"/>
    <circle cx="20" cy="0" r="14" fill="none" stroke="#141416" stroke-width=".35" stroke-dasharray="1 1"/>
    <circle cx="112" cy="34" r="10" fill="none" stroke="#141416" stroke-width=".35" stroke-dasharray="1 1"/>
    <circle cx="92" cy="24" r="10" fill="none" stroke="#141416" stroke-width=".35" stroke-dasharray="1 1"/>
    <path d="M0,58 H6" stroke="#d4f53c" stroke-width=".5"/><path d="M0,56 V60 M6,56 V60" stroke="#d4f53c" stroke-width=".4"/>
    ${lead(-8, 92, 5.9, 94.1)}${chip(-8.5, 92, 'outer r 20', 'end')}
    ${lead(-8, 58, 0, 58)}${chip(-8.5, 58, 'frame 6', 'end')}
    ${lead(-8, 6, 10.1, 9.9)}${chip(-8.5, 6, 'picture r 14', 'end')}
    ${lead(124, 22, 104.9, 28.9)}${lead(124, 22, 98.9, 19.9)}${chip(124.5, 22, 'r 10 + r 10')}
    ${lead(28, 108, 28, 94)}${chip(28.5, 108, 'target 44, r 14')}
  </svg>`;
}
