import '@videojs/html/video/player';
import '@videojs/html/media/mux-video';
import '@/video/skin';
import skinTemplate from '@/video/skin.html?raw';

// What the preview plays: the Sparvek launch film. The 16:9 cut streams from Mux (public playback ID); the 9:16 cut
// (`?film=916`) plays from `apps/preview/public/media` until it is on Mux too.
const MUX_ID = 'apPvzS00gRVMtAxQGteBC01g69UrLlRgty3oaLGDYwOog';
const FILM = new URLSearchParams(location.search).get('film') === '916' ? '916' : '169';
const TEXT_TRACKS =
  '<track kind="chapters" label="Chapters" srclang="en" src="./media/chapters.vtt" default>' +
  '<track kind="captions" label="English" srclang="en" src="./media/captions-en.vtt">';
const POSTER = FILM === '169' ? `https://image.mux.com/${MUX_ID}/thumbnail.webp?time=20.6&width=1920` : './media/poster-916.jpg';
const MEDIA =
  FILM === '169'
    ? `<mux-video src="https://stream.mux.com/${MUX_ID}.m3u8" playsinline crossorigin="anonymous">${TEXT_TRACKS}</mux-video>`
    : `<video src="./media/sparvek-916.mp4" playsinline preload="auto">${TEXT_TRACKS}<track kind="metadata" label="thumbnails" src="./media/storyboard-916.vtt" default></video>`;

const MEDIA_PLACEHOLDER = '<!-- Add a compatible media component here. -->';

export function createPlayer(): HTMLElement {
  const player = document.createElement('video-player');
  player.setAttribute('poster', POSTER);

  player.innerHTML = skinTemplate.replace(
    MEDIA_PLACEHOLDER,
    MEDIA
  );

  return player;
}
