# Text tracks

Subtitles, captions, and chapter track state for the player store

Manages subtitles, captions, chapters, and thumbnail tracks.

A default `kind="chapters"` track can also divide the [time slider](https://videojs.org/docs/framework/html/reference/components/time-slider) into chapter ranges and label the chapter at the current interaction position.

`thumbnailsTrack` is the first `kind="metadata"` track labeled `thumbnails`, or `null` when there is none. Its `crossOrigin` reports the media component’s CORS mode, or `null` when the media is not CORS-enabled. [Thumbnail](https://videojs.org/docs/framework/html/reference/components/thumbnail) reads it to fetch sprite sheets the same way the browser fetched the track.

## Import

```ts
import { textTrackFeature } from '@videojs/html';
```

The `liveVideoFeatures` and `videoFeatures` [feature bundles](https://videojs.org/docs/framework/html/guides/presets) include this feature.

## API Reference

### State

| Property | Type | Description |
| --- | --- | --- |
| `textTrackList` | `MediaTextTrack[]` | All text tracks available on the media component. |
| `subtitlesShowing` | `boolean` | Whether a captions/subtitles track is showing. |
| `chaptersCues` | `MediaTextCue[]` | Cues from the first `kind="chapters"` track, with cue ends clamped to a finite media duration. |
| `thumbnailsTrack` | `{ cues: MediaTextCue[]; src: string \| null; crossOrigin: 'anonymous' \| 'use-credentials' \| null } \| null` | The first thumbnails track, or `null` when there is none. |

### Actions

| Action | Type | Description |
| --- | --- | --- |
| `toggleSubtitles` | `(forceShow?: boolean) => boolean` | Toggle captions/subtitles visibility. Showing enables one caption/subtitle track. A track already showing stays selected. Otherwise, selection prefers the last track shown, then a track matching the browser language, then the first available track. Returns whether a track is showing. |
| `selectSubtitlesTrack` | `(id: string \| null) => void` | Show the captions/subtitles track with `id`, or turn captions/subtitles off with `null`. |

### Selector

Pass `selectTextTrack` to [`PlayerController`](https://videojs.org/docs/framework/html/reference/api/player-controller) to subscribe to text track state. Returns `undefined` if the text tracks feature is not configured.

**captions-button.ts**

```ts
import { createPlayer, UIElement, selectTextTrack } from '@videojs/html';
import { videoFeatures } from '@videojs/html/video';

const { PlayerController } = createPlayer({ features: videoFeatures });

class CaptionsButton extends UIElement {
  readonly #textTracks = new PlayerController(this, selectTextTrack);
}
```

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
