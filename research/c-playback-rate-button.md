# media-playback-rate-button

A button that cycles through playback speed rates

## Import

```ts
import '@videojs/html/ui/playback-rate-button';
```

## Anatomy

```html
<media-playback-rate-button></media-playback-rate-button>
```

## Behavior

Cycles through the player’s playback rates on click, in the order they are listed. The default list is `[0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]`; see the [playback rate feature](https://videojs.org/docs/framework/html/reference/api/feature-playback-rate) to set your own for the whole player, or set `rates` on the button to give it its own list. After the last rate, it wraps back to the first. If the current rate isn’t in the list (e.g., set programmatically), the button jumps to the next rate greater than the current one.

When `commandfor` is set, activation opens the linked playback-rate menu instead of cycling through rates. Use this mode when the button is the trigger for a `<media-menu>` that contains playback-rate options.

When the media’s playback rate is unavailable or unsupported, such as on an embed that takes no speed command, the element receives the native `hidden` attribute and ignores activation.

## Styling

| Attribute | Values | Description |
| --- | --- | --- |
| `data-rate` | Number | Current playback rate |
| `data-availability` | `"available"` \| `"unavailable"` \| `"unsupported"` | Whether the media can change its playback rate |
| `data-hidden` | Present / absent | Present on the HTML element while playback rate is unavailable or unsupported |

Display the current rate using the `data-rate` attribute:

```css
media-playback-rate-button::after {
  content: attr(data-rate) "\00D7";
}
```

## Accessibility

Renders a `<button>` with an automatic `aria-label` of `"Playback rate, {rate}"` (e.g., `"Playback rate, 1.5"`). Its tooltip shows `"Playback rate"` without the value. Override both with the `label` prop. Keyboard activation: Enter / Space.

In menu-trigger mode, the button behaves as a menu trigger and reflects menu state through the trigger attributes.

## Examples

### Basic Usage

**index.html**

```html
<video-player class="video-player">
  <media-container>
    <video src="https://stream.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/highest.mp4" autoplay muted playsinline loop></video>
    <media-playback-rate-button class="media-playback-rate-button"> </media-playback-rate-button>
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

.media-playback-rate-button {
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

.media-playback-rate-button::after {
  content: attr(data-rate) "\00D7";
}
```

**index.ts**

```ts
import '@videojs/html/video/player';
import '@videojs/html/ui/container';
import '@videojs/html/ui/playback-rate-button';
```

## API Reference

### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `disabled` | `boolean` | `false` | Whether the button is disabled. |
| `label` | `{ key: string; text: string } \| string \| ((state: PlaybackRateButtonState) => Text \| string)` | `''` | Custom label for the button. |
| `rates` | `readonly number[] \| string` | `[]` | Rates to cycle through, in order, in place of the player's `defaultPlaybackRates`. HTML takes a space-separated list, such as `rates="1 1.5 2"`. |

### State

State is reflected as data attributes for CSS styling.

| Property | Type | Description |
| --- | --- | --- |
| `label` | `{ key: string; text: string } \| string` | |
| `rate` | `number` | |
| `availability` | `'available' \| 'unavailable' \| 'unsupported'` | Whether the media can change its playback rate. |
| `hidden` | `boolean` | Whether the button is hidden because the media has no playback rate to change. |

### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-rate` | `number` | Current playback rate. |
| `data-availability` | `'available' \| 'unavailable' \| 'unsupported'` | Indicates playback rate availability (`available`, `unavailable`, `unsupported`). |
| `data-hidden` | — | Present when the button is hidden because the media has no playback rate to change. |

### CSS custom properties

| Variable | Description |
| --- | --- |
| `--media-playback-rate-length` | Characters in the current rate as text, such as `4` for `1.75`. Lets a skin size the label to fit the button. |

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
