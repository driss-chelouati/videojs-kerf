import '@videojs/html/video/player';
import '@/video/skin';
import skinTemplate from '@/video/skin.html?raw';

// What the preview plays: the Sparvek launch film, served from `apps/preview/public/media`.
// `?film=916` plays the 9:16 cut. Swap to Mux (with its storyboard.vtt) once the playback ID exists.
const FILM = new URLSearchParams(location.search).get('film') === '916' ? '916' : '169';
const SRC = `./media/sparvek-${FILM}.mp4`;
const POSTER = `./media/poster-${FILM}.jpg`;
const TRACKS = [
  '<track kind="chapters" label="Chapters" srclang="en" src="./media/chapters.vtt" default>',
  '<track kind="captions" label="English" srclang="en" src="./media/captions-en.vtt">',
  `<track kind="metadata" label="thumbnails" src="./media/storyboard-${FILM}.vtt" default>`,
].join('');

const MEDIA_PLACEHOLDER = '<!-- Add a compatible media component here. -->';

export function createPlayer(): HTMLElement {
  const player = document.createElement('video-player');
  player.setAttribute('poster', POSTER);

  player.innerHTML = skinTemplate.replace(
    MEDIA_PLACEHOLDER,
    `<video src="${SRC}" playsinline preload="auto">${TRACKS}</video>`
  );

  return player;
}
