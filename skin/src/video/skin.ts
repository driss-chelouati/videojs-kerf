import './skin.css';
import '@videojs/html/i18n';
import '@videojs/html/ui/container';
import '@videojs/html/ui/poster';
import '@videojs/html/ui/error-dialog';
import '@videojs/html/ui/dialog-backdrop';
import '@videojs/html/ui/dialog-popup';
import '@videojs/html/ui/dialog-title';
import '@videojs/html/ui/dialog-description';
import '@videojs/html/ui/dialog-close';
import '@videojs/html/ui/controls';
import '@videojs/html/ui/controls-group';
import '@videojs/html/ui/buffering-indicator';
import '@videojs/html/ui/controls-content';
import '@videojs/html/ui/tooltip-group';
import '@videojs/html/ui/tooltip';
import '@videojs/html/ui/tooltip-label';
import '@videojs/html/ui/tooltip-shortcut';
import '@videojs/html/ui/fullscreen-button';
import '@videojs/html/ui/play-button';
import '@videojs/html/ui/time-slider';
import '@videojs/html/ui/time-slider-chapters';
import '@videojs/html/ui/slider-track';
import '@videojs/html/ui/slider-buffer';
import '@videojs/html/ui/slider-fill';
import '@videojs/html/ui/slider-thumb';
import '@videojs/html/ui/slider-preview';
import '@videojs/html/ui/slider-thumbnail';
import '@videojs/html/ui/slider-value';
import '@videojs/html/ui/time-slider-chapter-title';
import '@videojs/html/ui/mute-button';
import '@videojs/html/ui/volume-popover';
import '@videojs/html/ui/volume-slider';
import '@videojs/html/ui/time-group';
import '@videojs/html/ui/time';
import '@videojs/html/ui/time-separator';
import '@videojs/html/ui/captions-button';
import '@videojs/html/ui/menu';
import '@videojs/html/ui/menu-content';
import '@videojs/html/ui/menu-item';
import '@videojs/html/ui/quality-radio-group';
import '@videojs/html/ui/menu-radio-item';
import '@videojs/html/ui/menu-item-indicator';
import '@videojs/html/ui/playback-rate-radio-group';
import '@videojs/html/ui/captions-radio-group';
import '@videojs/html/ui/hotkey';
import '@videojs/html/ui/gesture';
import '@videojs/html/ui/status-announcer';
import '@videojs/html/ui/volume-indicator';
import '@videojs/html/ui/volume-indicator-value';
import '@videojs/html/ui/status-indicator';
import '@videojs/html/ui/status-indicator-value';
import '@videojs/html/ui/seek-indicator';
import '@videojs/html/ui/seek-indicator-value';
import { registerIcons } from '@videojs/html/icons';
import {
  captionsOffIcon,
  captionsOnIcon,
  checkIcon,
  chevronIcon,
  fullscreenEnterIcon,
  fullscreenExitIcon,
  gearIcon,
  pauseIcon,
  playIcon,
  qualityIcon,
  restartIcon,
  seekIcon,
  speedIcon,
  spinnerIcon,
  volumeHighIcon,
  volumeLowIcon,
  volumeOffIcon,
} from '@videojs/html/icons/default';

// Kerf draws the official Video.js solid set (the Default skin's icons) under its own family name.
registerIcons('kerf', {
  'captions-off': captionsOffIcon,
  'captions-on': captionsOnIcon,
  check: checkIcon,
  chevron: chevronIcon,
  'fullscreen-enter': fullscreenEnterIcon,
  'fullscreen-exit': fullscreenExitIcon,
  gear: gearIcon,
  pause: pauseIcon,
  play: playIcon,
  quality: qualityIcon,
  restart: restartIcon,
  seek: seekIcon,
  speed: speedIcon,
  spinner: spinnerIcon,
  'volume-high': volumeHighIcon,
  'volume-low': volumeLowIcon,
  'volume-off': volumeOffIcon,
});

// The frame keeps a hairline of progress while the controls are sunk. The rail sits outside the time slider, so it
// reads the media's own progress: one capturing listener for every Kerf player on the page.
if (typeof document !== 'undefined') {
  const track = (event: Event) => {
    const media = event.target as HTMLMediaElement;
    const skin = media.closest?.('.kerf') as HTMLElement | null;
    if (!skin || !media.duration) return;
    skin.style.setProperty('--kerf-progress', `${(media.currentTime / media.duration) * 100}%`);
  };
  for (const type of ['timeupdate', 'durationchange', 'seeked']) document.addEventListener(type, track, true);
}
