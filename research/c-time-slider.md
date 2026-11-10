# media-time-slider

A slider component for seeking through media playback time

## Import

```ts
import '@videojs/html/ui/time-slider';
import '@videojs/html/ui/slider-track';
import '@videojs/html/ui/slider-buffer';
import '@videojs/html/ui/slider-fill';
import '@videojs/html/ui/slider-thumb';
import '@videojs/html/ui/slider-preview';
import '@videojs/html/ui/slider-thumbnail';
import '@videojs/html/ui/slider-value';
import '@videojs/html/ui/time-slider-chapters';
import '@videojs/html/ui/time-slider-chapter-title';
```

## Anatomy

```html
<media-time-slider>
  <media-slider-track>
    <media-slider-buffer></media-slider-buffer>
    <media-slider-fill></media-slider-fill>
  </media-slider-track>
  <media-slider-thumb></media-slider-thumb>
  <media-slider-preview>
    <media-time-slider-chapter-title></media-time-slider-chapter-title>
    <media-slider-value type="pointer"></media-slider-value>
  </media-slider-preview>
</media-time-slider>
```

Add `<media-time-slider-chapters>` to divide the slider track into sections. Each cue in the default `kind="chapters"` text track marks a chapter. Without chapter cues, one section covers the full slider.

```html
<media-time-slider-chapters>
  <template>
    <div>
      <media-slider-track>
        <media-slider-buffer></media-slider-buffer>
        <media-slider-fill></media-slider-fill>
      </media-slider-track>
    </div>
  </template>
</media-time-slider-chapters>
```

The required template must contain exactly one HTML root element. It remains in the light DOM and is cloned for each normalized chapter range. When no chapter cues are available, it is cloned once as a full-width, cue-less range.

## Behavior

Displays and controls the current playback position. Dragging the slider seeks the media. The fill level reflects `currentTime / duration` as a percentage, and the buffer level shows how much media has been buffered.

Value changes during drag are throttled via the `changeThrottle` prop (default 100ms) using a leading+trailing throttle to keep the UI responsive without overwhelming the media element.

Chapter cues are normalized into contiguous ranges. Any uncovered time becomes a gap range, so track geometry always spans the full duration. With no usable chapter cues, one gap range spans the entire slider. Gap ranges receive the same geometry styles but cannot be highlighted and have no chapter title.

## Styling

Use [CSS custom properties](#css-custom-properties) to style the fill, pointer, and buffer levels:

```css
media-time-slider::before {
  width: var(--media-slider-fill);
}
```

Use `data-seeking` to style during active seek operations:

```css
media-time-slider[data-seeking] {
  opacity: 0.8;
}
```

Each rendered chapter receives `data-active` while playback is inside it and `data-highlighted` while the pointer is inside an authored chapter. Its geometry and local progress are exposed through:

- `--media-slider-chapter-start`
- `--media-slider-chapter-end`
- `--media-slider-chapter-width`
- `--media-slider-chapter-fill`
- `--media-slider-chapter-buffer`

The generated fill and buffer parts also inherit the slider-level `--media-slider-fill` and `--media-slider-buffer` values. This allows every chapter to render full-width progress planes and use its chapter bounds as a clip, keeping progress transitions continuous across segments.

## Accessibility

Renders with `role="slider"` and an automatic `aria-label` that resolves to “Seek” from the active locale. Override with the `label` prop. Keyboard controls:

- Arrow Left / Arrow Right: step by `step` increment
- Page Up / Page Down: step by `largeStep` increment
- Home: seek to start
- End: seek to end

Before each keyboard seek, the current time snaps to the nearest multiple of `step`. With the default `step` of `1`, pressing Arrow Right at 12.4 seconds seeks to 13 seconds.

`<media-time-slider-chapter-title>` follows the pointer during pointer interaction. While the slider has keyboard focus, it follows the current playback position and announces chapter changes.

## Examples

Nest sub-components for full control over the slider’s DOM structure. This example includes a track, fill bar, buffer indicator, draggable thumb, and a tooltip that shows the pointed-at time.

**index.html**

```html
<video-player class="video-player">
  <media-container>
    <video src="https://stream.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/highest.mp4" autoplay muted playsinline loop></video>
    <media-time-slider class="media-time-slider">
      <media-slider-track class="media-slider-track">
        <media-slider-buffer class="media-slider-buffer"></media-slider-buffer>
        <media-slider-fill class="media-slider-fill"></media-slider-fill>
      </media-slider-track>
      <media-slider-thumb class="media-slider-thumb"></media-slider-thumb>
      <media-slider-value type="pointer" class="media-slider-value"></media-slider-value>
    </media-time-slider>
  </media-container>
</video-player>
```

**index.css**

```css
.video-player media-container {
  position: relative;
  display: block;
}

.video-player media-container video {
  width: 100%;
}

.media-time-slider {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  display: flex;
  align-items: center;
  height: 20px;
  cursor: pointer;
}

.media-slider-track {
  position: absolute;
  right: 0;
  left: 0;
  height: 4px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 9999px;
  transition: height 150ms ease;
}

.media-time-slider[data-interactive] .media-slider-track {
  height: 6px;
}

.media-slider-buffer {
  position: absolute;
  top: 0;
  left: 0;
  width: var(--media-slider-buffer);
  height: 100%;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 9999px;
}

.media-slider-fill {
  position: absolute;
  top: 0;
  left: 0;
  width: var(--media-slider-fill);
  height: 100%;
  background: white;
  border-radius: 9999px;
}

.media-slider-thumb {
  position: absolute;
  left: var(--media-slider-fill);
  width: 14px;
  height: 14px;
  background: white;
  border-radius: 50%;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
  transform: translateX(-50%) scale(0);
  transition: transform 150ms ease;
}

.media-time-slider[data-interactive] .media-slider-thumb {
  transform: translateX(-50%) scale(1);
}

.media-time-slider[data-dragging] .media-slider-thumb {
  left: var(--media-slider-pointer);
  transform: translateX(-50%) scale(1.1);
}

.media-time-slider[data-dragging] .media-slider-fill {
  width: var(--media-slider-pointer);
}

.media-slider-value {
  position: absolute;
  bottom: 100%;
  left: var(--media-slider-pointer);
  padding: 2px 6px;
  margin-bottom: 6px;
  font-size: 12px;
  color: white;
  white-space: nowrap;
  pointer-events: none;
  background: rgba(0, 0, 0, 0.8);
  border-radius: 4px;
  opacity: 0;
  transform: translateX(-50%);
  transition: opacity 150ms ease;
}

.media-time-slider[data-pointing] .media-slider-value {
  opacity: 1;
}
```

**index.ts**

```ts
import '@videojs/html/video/player';
import '@videojs/html/ui/container';
import '@videojs/html/ui/time-slider';
import '@videojs/html/ui/slider-track';
import '@videojs/html/ui/slider-buffer';
import '@videojs/html/ui/slider-fill';
import '@videojs/html/ui/slider-thumb';
import '@videojs/html/ui/slider-value';
```

### With chapters

Add a default chapters track, then provide the markup used for each chapter. The deliberate one-minute gap in this example remains visible as an unlabelled, non-highlightable segment.

**index.html**

```html
<video-player class="video-player">
  <media-container>
    <video src="https://stream.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/highest.mp4" autoplay muted playsinline loop crossorigin="anonymous">
      <track kind="chapters" src="/docs/demos/time-slider/chapters.vtt" srclang="en" default />
    </video>
    <media-time-slider class="media-time-slider">
      <media-time-slider-chapters class="media-slider-chapters">
        <template>
          <div class="media-slider-chapter">
            <media-slider-track class="media-slider-track">
              <media-slider-buffer class="media-slider-buffer"></media-slider-buffer>
              <media-slider-fill class="media-slider-fill"></media-slider-fill>
            </media-slider-track>
          </div>
        </template>
      </media-time-slider-chapters>
      <media-slider-thumb class="media-slider-thumb"></media-slider-thumb>
      <media-slider-preview class="media-slider-preview">
        <media-time-slider-chapter-title class="media-slider-chapter-title"></media-time-slider-chapter-title>
        <media-slider-value type="pointer"></media-slider-value>
      </media-slider-preview>
    </media-time-slider>
  </media-container>
</video-player>
```

**index.css**

```css
.video-player media-container {
  position: relative;
  display: block;
}

.video-player media-container video {
  width: 100%;
}

.media-time-slider {
  position: absolute;
  right: 12px;
  bottom: 8px;
  left: 12px;
  display: flex;
  align-items: center;
  height: 20px;
  color: white;
  cursor: pointer;
}

.media-slider-chapters {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}

.media-slider-chapter {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  clip-path: inset(0 calc(100% - var(--media-slider-chapter-end)) 0 var(--media-slider-chapter-start));
}

.media-slider-track {
  position: absolute;
  right: 0;
  left: 0;
  display: block;
  height: 4px;
  overflow: hidden;
  background: rgb(255 255 255 / 30%);
  border-radius: 9999px;
  transition: height 150ms ease;
}

.media-slider-chapter .media-slider-track {
  clip-path: inset(
    0 calc(100% - var(--media-slider-chapter-end) + 2px) 0 calc(var(--media-slider-chapter-start) + 2px) round 9999px
  );
}

.media-slider-chapter[data-highlighted] .media-slider-track {
  height: 7px;
}

.media-slider-buffer,
.media-slider-fill {
  position: absolute;
  inset-block: 0;
  left: 0;
  display: block;
  border-radius: inherit;
  transition: width 200ms linear;
}

.media-slider-buffer {
  width: var(--media-slider-buffer);
  background: rgb(255 255 255 / 30%);
}

.media-slider-fill {
  width: var(--media-slider-fill);
  background: white;
}

.media-time-slider[data-dragging] .media-slider-fill {
  width: var(--media-slider-pointer);
  transition-duration: 0ms;
}

.media-slider-thumb {
  position: absolute;
  top: 50%;
  left: var(--media-slider-fill);
  display: block;
  width: 12px;
  height: 12px;
  background: white;
  border-radius: 50%;
  translate: -50% -50%;
}

.media-time-slider[data-dragging] .media-slider-thumb {
  left: var(--media-slider-pointer);
}

.media-slider-preview {
  position: absolute;
  bottom: 100%;
  left: var(--media-slider-pointer);
  display: flex;
  gap: 6px;
  padding: 3px 7px;
  color: white;
  white-space: nowrap;
  pointer-events: none;
  background: rgb(0 0 0 / 80%);
  border-radius: 4px;
  opacity: 0;
  translate: -50% -4px;
}

.media-time-slider[data-pointing] .media-slider-preview,
.media-time-slider[data-interactive]:not([data-pointing]) .media-slider-preview {
  opacity: 1;
}

.media-slider-chapter-title:empty {
  display: none;
}
```

**index.ts**

```ts
import '@videojs/html/video/player';
import '@videojs/html/ui/container';
import '@videojs/html/ui/time-slider';
import '@videojs/html/ui/time-slider-chapters';
import '@videojs/html/ui/slider-track';
import '@videojs/html/ui/slider-buffer';
import '@videojs/html/ui/slider-fill';
import '@videojs/html/ui/slider-thumb';
import '@videojs/html/ui/slider-preview';
import '@videojs/html/ui/time-slider-chapter-title';
import '@videojs/html/ui/slider-value';
```

## API Reference

### media-time-slider

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `changeThrottle` (attribute `change-throttle`) | `number` | `100` | Leading+trailing throttle (ms) for `onValueChange` during drag. |
| `disabled` | `boolean` | `false` | Whether the slider is non-interactive. |
| `label` | `{ key: string; text: string } \| string \| ((state: SliderState) => Text \| string)` | `''` | Custom label for the slider. |
| `largeStep` (attribute `large-step`) | `number` | `10` | Large step increment in seconds (Page Up/Down keys). |
| `orientation` | `'horizontal' \| 'vertical'` | `'horizontal'` | Axis of slider movement. |
| `pauseOnDrag` (attribute `pause-on-drag`) | `boolean` | `false` | When true, pause playback while the user is dragging the thumb, resuming on release if it was playing before. |
| `step` | `number` | `1` | Step increment in seconds for value changes (arrow keys). |
| `thumbAlignment` (attribute `thumb-alignment`) | `'center' \| 'edge'` | `'center'` | How the thumb aligns at the track edges. `edge` constrains the thumb within track bounds. |

#### State

State is reflected as data attributes for CSS styling.

| Property | Type | Description |
| --- | --- | --- |
| `value` | `number` | Current slider value in the min–max range. |
| `fillPercent` | `number` | Fill level as a percentage (0–100), derived from value. |
| `pointerPercent` | `number` | Pointer position as a percentage of the track (0–100). |
| `dragging` | `boolean` | Whether the user is actively dragging. |
| `pointing` | `boolean` | Whether the pointer is over the slider. |
| `interactive` | `boolean` | Whether dragging, pointing, or focus is active. |
| `orientation` | `'horizontal' \| 'vertical'` | Axis of slider movement. |
| `disabled` | `boolean` | Whether the slider is non-interactive. |
| `thumbAlignment` | `'center' \| 'edge'` | How the thumb aligns at the track edges. |
| `currentTime` | `number` | Current playback position in seconds. |
| `duration` | `number` | Total duration in seconds (0 if unknown). |
| `seeking` | `boolean` | Whether a seek operation is in progress. |
| `bufferPercent` | `number` | Buffered amount as a percentage of duration (0–100). |

#### Data attributes

| Attribute | Description |
| --- | --- |
| `data-seeking` | Present when a seek operation is in progress. |

#### CSS custom properties

| Variable | Description |
| --- | --- |
| `--media-slider-fill` | Fill level percentage (0–100), representing current playback position. |
| `--media-slider-pointer` | Pointer position percentage (0–100), tracking the cursor along the slider. |
| `--media-slider-buffer` | Buffer level percentage (0–100), indicating how much media has been buffered. |

#### Events

| Event | Description |
| --- | --- |
| `drag-end` | Fired when a pointer drag ends. |
| `drag-start` | Fired when a pointer drag starts. |

### media-time-slider-chapter-title

Displays the chapter title at the current pointer or keyboard position.

### media-time-slider-chapters

Clones a light-DOM template once per normalized chapter range.

The required template must contain exactly one HTML root element. When no chapter cues are available, the template is cloned once for a full-duration range.

### media-slider-buffer

Displays the buffered range on the slider track.

### media-slider-fill

Displays the filled portion from start to the current value.

### media-slider-preview

Positioning container for preview content that tracks the pointer along the slider.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `overflow` | `'clamp' \| 'visible'` | — | How the preview handles slider boundaries. `clamp` keeps it within bounds; `visible` lets it extend past them. |

#### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-dragging` | — | Present when the user is actively dragging. |
| `data-pointing` | — | Present when the pointer is over the slider. |
| `data-interactive` | — | Present when dragging, pointing, or focus is active. |
| `data-orientation` | `'horizontal' \| 'vertical'` | Current axis of slider movement (`horizontal` or `vertical`). |
| `data-disabled` | — | Present when the slider is non-interactive. |

### media-slider-thumb

Draggable handle for setting the slider value. Receives focus and handles keyboard interaction.

#### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-dragging` | — | Present when the user is actively dragging. |
| `data-pointing` | — | Present when the pointer is over the slider. |
| `data-interactive` | — | Present when dragging, pointing, or focus is active. |
| `data-orientation` | `'horizontal' \| 'vertical'` | Current axis of slider movement (`horizontal` or `vertical`). |
| `data-disabled` | — | Present when the slider is non-interactive. |

### media-slider-track

Contains the slider's visual track and interactive hit zone.

### media-slider-value

Writes the formatted current or pointer slider value into its own text content, replacing any children.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `type` | `'current' \| 'pointer'` | — | Which slider value to display: the current position or the pointer position. |

#### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-dragging` | — | Present when the user is actively dragging. |
| `data-pointing` | — | Present when the pointer is over the slider. |
| `data-interactive` | — | Present when dragging, pointing, or focus is active. |
| `data-orientation` | `'horizontal' \| 'vertical'` | Current axis of slider movement (`horizontal` or `vertical`). |
| `data-disabled` | — | Present when the slider is non-interactive. |

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
