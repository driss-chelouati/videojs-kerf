// Mounts a Kerf player for the site. The skin itself lives in src/ and knows nothing about this page.
import '@videojs/html/video/player';
import '@videojs/html/media/mux-video';
import '@/video/skin';
import skinTemplate from '@/video/skin.html?raw';

export const MUX_ID = 'apPvzS00gRVMtAxQGteBC01g69UrLlRgty3oaLGDYwOog';
export type Film = '169' | '916';

const TEXT_TRACKS =
  '<track kind="chapters" label="Chapters" srclang="en" src="./media/chapters.vtt" default>' +
  '<track kind="captions" label="English" srclang="en" src="./media/captions-en.vtt">';

function media(film: Film): string {
  if (film === '169') {
    return `<mux-video src="https://stream.mux.com/${MUX_ID}.m3u8" playsinline crossorigin="anonymous" preload="auto">${TEXT_TRACKS}</mux-video>`;
  }
  return `<video src="./media/sparvek-916.mp4" playsinline preload="auto">${TEXT_TRACKS}<track kind="metadata" label="thumbnails" src="./media/storyboard-916.vtt" default></video>`;
}

export function poster(film: Film): string {
  return film === '169' ? `https://image.mux.com/${MUX_ID}/thumbnail.webp?time=20.6&width=1600` : './media/poster-916.jpg';
}

export function createKerf(film: Film): HTMLElement {
  const i18n = document.createElement('media-i18n');
  const player = document.createElement('video-player');
  player.setAttribute('poster', poster(film));
  player.setAttribute('default-playback-rates', '0.5 0.75 1 1.25 1.5 2');
  player.innerHTML = skinTemplate.replace('<!-- Add a compatible media component here. -->', media(film));
  i18n.append(player);
  return i18n;
}

export type Chapter = { start: number; end: number; title: string };

export async function loadChapters(): Promise<Chapter[]> {
  const text = await fetch('./media/chapters.vtt').then((r) => r.text());
  const toS = (t: string) => t.split(':').reduce((a, v) => a * 60 + parseFloat(v), 0);
  return text
    .split(/\n\n+/)
    .map((block) => block.trim().split('\n'))
    .filter((lines) => lines[0]?.includes('-->'))
    .map(([times, title]) => {
      const [a, b] = times.split('-->').map((s) => toS(s.trim()));
      return { start: a, end: b, title: title.trim() };
    });
}
