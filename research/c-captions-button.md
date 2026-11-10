# media-captions-button

Accessible captions toggle button with availability detection and state reflection

## Import

```ts
import '@videojs/html/ui/captions-button';
```

## Anatomy

```html
<media-captions-button></media-captions-button>
```

## Behavior

Toggles captions and subtitles on and off. The button checks the media’s text track list for tracks with `kind="captions"` or `kind="subtitles"`.

When none are present, the element receives the native `hidden` attribute. The raw state remains available as `data-availability`.

An explicitly disabled button with caption tracks stays visible and focusable with `aria-disabled="true"` and `data-disabled`, but does not toggle captions.

When `menu-for` is set to a menu’s `id` and multiple caption or subtitle tracks are available, activation opens the linked captions menu instead of toggling captions directly.

## Styling

Style the button based on active state:

```css
media-captions-button[data-active] .icon-on { display: inline; }
media-captions-button:not([data-active]) .icon-off { display: inline; }
```

Style an explicitly disabled, available button:

```css
media-captions-button[data-disabled] {
  cursor: not-allowed;
  opacity: 0.5;
}
```

The button hides automatically when no caption tracks are available. No availability selector or extra hiding CSS is required.

## Accessibility

Renders a `<button>` with an automatic `aria-label`: “Disable captions” when active, “Enable captions” when inactive. Override with the `label` prop. Keyboard activation: Enter / Space.

In menu-trigger mode, the button behaves as a menu trigger and reflects menu state through the trigger attributes.

## Examples

### Basic Usage

**index.html**

```html
<video-player class="video-player">
  <media-container>
    <video src="https://stream.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/highest.mp4" autoplay muted playsinline loop>
      <track kind="captions" src="/docs/demos/captions-button/captions.vtt" srclang="en" label="English" />
    </video>
    <media-captions-button class="media-captions-button">
      <span class="active">Captions Off</span>
      <span class="inactive">Captions On</span>
    </media-captions-button>
  </media-container>
</video-player>
```

**index.css**

```css
.video-player media-container {
  position: relative;
}

.video-player media-container video {
  width: 100%;
}

.media-captions-button {
  position: absolute;
  bottom: 10px;
  left: 10px;
  padding-block: 8px;
  padding-inline: 20px;
  color: black;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 9999px;
  backdrop-filter: blur(10px);
}

.media-captions-button .active {
  display: none;
}
.media-captions-button .inactive {
  display: none;
}
.media-captions-button[data-active] .active {
  display: inline;
}
.media-captions-button:not([data-active]) .inactive {
  display: inline;
}
```

**index.ts**

```ts
import '@videojs/html/video/player';
import '@videojs/html/ui/container';
import '@videojs/html/ui/captions-button';
```

## API Reference

### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `disabled` | `boolean` | `false` | Whether the button is disabled. |
| `label` | `{ key: string; text: string } \| string \| ((state: CaptionsButtonState) => Text \| string)` | `''` | Custom label for the button. |

### State

State is reflected as data attributes for CSS styling.

| Property | Type | Description |
| --- | --- | --- |
| `subtitlesShowing` | `boolean` | Whether a captions/subtitles track is showing. |
| `label` | `{ key: string; text: string } \| string` | |
| `availability` | `'available' \| 'unavailable'` | Whether caption/subtitle tracks are present. |
| `disabled` | `boolean` | Non-interactive but still focusable (mirrors `aria-disabled`). |
| `hidden` | `boolean` | Whether the button is hidden because no caption tracks are present. |

### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-active` | — | Present when captions are enabled. |
| `data-availability` | `'available' \| 'unavailable'` | Indicates captions availability (`available` or `unavailable`). |
| `data-disabled` | — | Present when the button is non-interactive (mirrors `aria-disabled`). |
| `data-hidden` | — | Present when the button is hidden because no caption tracks are present. |

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
