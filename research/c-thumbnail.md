# media-thumbnail

Time-based thumbnail preview component for timeline scrubbing and hover previews

## Quick Start: Video Track

`<media-thumbnail>` can read thumbnail cues directly from your video track. Add a `<track>` with `kind="metadata"` and `label="thumbnails"` to your media component.

[Mux](https://www.mux.com/?utm_source=videojs&utm_campaign=vjs10&utm_content=docs-content) provides this as `storyboard.vtt`:

`https://image.mux.com/{PLAYBACK_ID}/storyboard.vtt`

That track is cross-origin, and a cross-origin `<track>` only loads when the media component is CORS-enabled:

```html
<video src="video.mp4" crossorigin="anonymous">
  <track
    kind="metadata"
    label="thumbnails"
    src="https://image.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/storyboard.vtt"
    default
  />
</video>
<media-thumbnail time="12"></media-thumbnail>
```

A same-origin track needs none of this.

## Import

```ts
import '@videojs/html/ui/thumbnail';
```

## Anatomy

```html
<media-thumbnail>
  <img alt="" decoding="async" />
</media-thumbnail>
```

## Behavior

The thumbnail root resolves an image for the current `time`, owns `src` and `srcset` on it, and reports its loading lifecycle.

The `<img>` child is optional: leave it out and `<media-thumbnail>` draws an image of its own in its shadow DOM; supply one to replace it and compose overlays or loading indicators beside it. Any `crossorigin`, `loading`, or `fetchpriority` the supplied image already carries is yours and wins over the element’s own attributes; the rest are filled in.

Supported source formats:

- Text track: `<track kind="metadata" label="thumbnails" src="...vtt">`
- JSON array: `{ url, startTime, endTime? }[]`
- JSON sprite array: `{ url, startTime, endTime?, width, height, coords }[]`

Text-track mode needs an enclosing player element because it reads track state from the player store. JSON modes (`thumbnails` property) work without a player.

The component picks the latest thumbnail whose `startTime` is less than or equal to the current `time`, then scales/clips sprite tiles to fill CSS min/max constraints while preserving aspect ratio. Tiles scale up as well as down, so a preview whose `max-width` grows — a container query widening it in fullscreen, say — grows with it.

### Cross-origin images

Leave `crossOrigin` unset and the thumbnail follows the media component. A cross-origin thumbnail `<track>` only loads when the media is CORS-enabled, so the images its cues point at are fetched with that same mode. Skins get this for free, with nothing to thread through.

Opt out to fetch them without CORS:

```ts
const thumbnail = document.querySelector('media-thumbnail');
thumbnail.crossOrigin = null;
```

Leaving the `crossorigin` attribute off is not the opt out. An absent attribute means “follow the media component”; only the property set to `null` opts out.

An empty value does not opt out either. The [CORS settings attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin) reads anything other than `use-credentials` as Anonymous, so it is a value like any other.

Thumbnails you supply through `thumbnails` never inherit, since they need not be related to the media component at all. Set `crossOrigin` yourself when those images need it.

## Styling

Use state data attributes for pure CSS styling:

```css
media-thumbnail[data-hidden] {
  display: none;
}

media-thumbnail[data-loading] {
  opacity: 0.6;
}

media-thumbnail[data-error] {
  outline: 1px solid #ef4444;
}
```

The image the element draws is exposed as a part. An `<img>` you supply is an ordinary child, so style it as a descendant:

```css
media-thumbnail::part(image),
media-thumbnail > img {
  border-radius: 4px;
}
```

The element clips to the selected tile while the image inside spans the whole sprite sheet, so anything after the image in flow lands past the clip edge. Position the element and lay overlays over it:

```css
media-thumbnail {
  position: relative;
}

media-thumbnail > .overlay {
  position: absolute;
  inset: 0;
}
```

## Accessibility

`<media-thumbnail>` is decorative by default (`aria-hidden="true"`). It is intended for visual preview UX (for example, timeline hover previews) rather than primary accessible content.

## Examples

### Text Track (VTT)

**index.html**

```html
<section class="demo">
  <video-player>
    <media-container>
      <video class="media" src="https://stream.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/highest.mp4" preload="auto" muted playsinline crossorigin="anonymous">
        <track kind="metadata" label="thumbnails" src="https://image.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/storyboard.vtt" default />
      </video>
      <media-thumbnail class="media-thumbnail" time="12"></media-thumbnail>
    </media-container>
  </video-player>
</section>
```

**index.css**

```css
.demo {
  position: relative;
  display: block;
  max-width: 280px;
}

.media {
  position: absolute;
  width: 1px;
  height: 1px;
  pointer-events: none;
  opacity: 0;
}

.media-thumbnail {
  display: block;
  width: auto;
  min-width: 0;
  max-width: 240px;
}

.media-thumbnail[data-hidden] {
  display: none;
}
```

**index.ts**

```ts
import '@videojs/html/video/player';
import '@videojs/html/ui/container';
import '@videojs/html/ui/thumbnail';
```

### JSON Array

**index.html**

```html
<media-thumbnail class="html-thumbnail-json" time="12" style="max-width: 240px"></media-thumbnail>
```

**index.ts**

```ts
import '@videojs/html/ui/thumbnail';

type DemoThumbnailImage = {
  url: string;
  startTime: number;
  endTime?: number;
};

type ThumbnailDemoElement = HTMLElement & { thumbnails?: DemoThumbnailImage[] };

const initializedDemos = new WeakSet<ThumbnailDemoElement>();

function initializeDemos(): void {
  document.querySelectorAll<ThumbnailDemoElement>('.html-thumbnail-json').forEach((thumbnail) => {
    if (initializedDemos.has(thumbnail)) return;

    initializedDemos.add(thumbnail);
    thumbnail.thumbnails = [
      {
        url: 'https://image.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/thumbnail.jpg?time=0',
        startTime: 0,
        endTime: 10,
      },
      {
        url: 'https://image.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/thumbnail.jpg?time=10',
        startTime: 10,
        endTime: 20,
      },
      {
        url: 'https://image.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/thumbnail.jpg?time=20',
        startTime: 20,
      },
    ];
  });
}

initializeDemos();
document.addEventListener('astro:page-load', initializeDemos);
```

### JSON Sprite Array

**index.html**

```html
<media-thumbnail class="html-thumbnail-json-sprite" time="12" style="max-width: 240px"></media-thumbnail>
```

**index.ts**

```ts
import '@videojs/html/ui/thumbnail';

type DemoThumbnailImage = {
  url: string;
  startTime: number;
  endTime?: number;
  width?: number;
  height?: number;
  coords?: { x: number; y: number };
};

type ThumbnailDemoElement = HTMLElement & { thumbnails?: DemoThumbnailImage[] };

const initializedDemos = new WeakSet<ThumbnailDemoElement>();

function initializeDemos(): void {
  document.querySelectorAll<ThumbnailDemoElement>('.html-thumbnail-json-sprite').forEach((thumbnail) => {
    if (initializedDemos.has(thumbnail)) return;

    initializedDemos.add(thumbnail);
    thumbnail.thumbnails = [
      {
        url: 'https://image.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/storyboard.jpg',
        startTime: 0,
        endTime: 10,
        width: 284,
        height: 160,
        coords: { x: 0, y: 0 },
      },
      {
        url: 'https://image.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/storyboard.jpg',
        startTime: 10,
        endTime: 20,
        width: 284,
        height: 160,
        coords: { x: 284, y: 0 },
      },
      {
        url: 'https://image.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/storyboard.jpg',
        startTime: 20,
        width: 284,
        height: 160,
        coords: { x: 568, y: 0 },
      },
    ];
  });
}

initializeDemos();
document.addEventListener('astro:page-load', initializeDemos);
```

## API Reference

### media-thumbnail

`<media-thumbnail>` — resolves and sizes a time-based thumbnail into an image.

The element owns `src` and `srcset` on the active image. Left empty, it draws an image of its own in its shadow root. Supply an `<img>` child instead — `<media-thumbnail time="12"><img alt=""></media-thumbnail>` — to compose overlays or loading indicators beside the image the element controls. Any `crossorigin`, `loading`, or `fetchpriority` the child already carries wins over the element's own; the rest are filled in. Inside a skin, an `<img slot="thumbnail">` of yours replaces the one the skin carries.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `thumbnails` | `ThumbnailImage[]` | — | Pre-parsed thumbnail images — bypasses the automatic `<track>` detection. |
| `time` | `number` | — | Time in seconds to display the thumbnail for. |

#### State

State is reflected as data attributes for CSS styling.

| Property | Type | Description |
| --- | --- | --- |
| `loading` | `boolean` | The thumbnail image is loading. |
| `error` | `boolean` | The thumbnail image failed to load. |
| `hidden` | `boolean` | Whether the component is hidden because no thumbnail is available and it is not loading. |

#### Data attributes

| Attribute | Description |
| --- | --- |
| `data-loading` | |
| `data-error` | |
| `data-hidden` | |

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
