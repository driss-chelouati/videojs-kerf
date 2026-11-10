# media-popover

A popover component for displaying contextual content anchored to a trigger

## Import

```ts
import '@videojs/html/ui/popover';
```

## Anatomy

```html
<button type="button" commandfor="my-popover">Open</button>
<media-popover id="my-popover">Content</media-popover>
```

## Behavior

Displays contextual content anchored to a trigger element. By default, opens on click and closes when clicking outside, pressing Escape, or when the trigger loses focus.

Set `openOnHover` to open on pointer hover instead of click. Use `delay` and `closeDelay` to control timing for hover interactions.

Popovers inside a [player container](https://videojs.org/docs/framework/html/reference/components/player-container) join its popup group. Opening one closes any other popover or root menu that is open in the same container. A popover outside the container still opens and closes normally, but it is not coordinated with that group.

The `side` and `align` props control the preferred popup placement relative to the trigger. When the preferred side overflows the positioning boundary, the popup uses the opposite side if it has more space.

`<media-popover>` is the popup. A trigger links to it through `commandfor` set to the popup’s `id`. If the popup has no `id`, it uses the element immediately before it as the trigger. It gives the popup a generated `id` and sets the trigger’s `commandfor` to that value. That element must not already target another popup through `commandfor`.

## Styling

Use [CSS custom properties](#css-custom-properties) for positioning offsets:

```css
media-popover {
  --media-popover-side-offset: 8px;
  --media-popover-align-offset: 0px;
  --media-popover-boundary-offset: 8px;
}
```

Style based on open state, rendered side, and transition phases. `data-side` reflects the rendered side and can differ from the preferred `side` prop after collision handling:

```css
media-popover[data-open] {
  display: block;
}
media-popover[data-starting-style] {
  opacity: 0;
}
media-popover[data-ending-style] {
  opacity: 0;
}
media-popover[data-side="top"] {
  transform-origin: bottom center;
}
media-popover[data-side="bottom"] {
  transform-origin: top center;
}
```

## Accessibility

The trigger receives `aria-expanded` reflecting the open state. When `modal` is set, the popup receives `aria-modal="true"`. Closing via Escape is enabled by default and can be disabled with `closeOnEscape={false}`.

## Examples

### Basic Usage

**index.html**

```html
<video-player class="video-player">
  <media-container>
    <video src="https://stream.mux.com/BV3YZtogl89mg9VcNBhhnHm02Y34zI1nlMuMQfAbl3dM/highest.mp4" autoplay muted playsinline loop></video>
    <div class="bar">
      <button type="button" commandfor="popover-demo" class="trigger">Settings</button>
      <media-popover id="popover-demo" class="media-popover">
        <div class="popup">Popover content</div>
      </media-popover>
    </div>
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

.bar {
  position: absolute;
  bottom: 10px;
  left: 10px;
}

.trigger {
  padding: 6px 16px;
  color: black;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 9999px;
  backdrop-filter: blur(10px);
}

.media-popover {
  padding: 12px 16px;
  font-size: 14px;
  color: white;
  white-space: nowrap;
  background: rgba(0, 0, 0, 0.85);
  border-radius: 8px;
  backdrop-filter: blur(10px);
}
```

**index.ts**

```ts
import '@videojs/html/video/player';
import '@videojs/html/ui/container';
import '@videojs/html/ui/popover';
```

## API Reference

### media-popover

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `align` | `'start' \| 'center' \| 'end'` | `'center'` | Alignment of the popup along the trigger's edge. |
| `boundary` | `'viewport' \| 'container' \| string & {}` | — | Boundary used to constrain the popup position. |
| `closeDelay` (attribute `close-delay`) | `number` | `0` | Delay in ms before closing after pointer leaves. |
| `closeOnEscape` (attribute `close-on-escape`) | `boolean` | `true` | Close the popup when the Escape key is pressed. |
| `closeOnOutsideClick` (attribute `close-on-outside-click`) | `boolean` | `true` | Close the popup when clicking outside the trigger and popup. |
| `defaultOpen` (attribute `default-open`) | `boolean` | `false` | Initial open state for uncontrolled usage. |
| `delay` | `number` | `300` | Delay in ms before opening on hover. |
| `modal` | `boolean \| 'trap-focus'` | `false` | - `false` (default): non-modal; background content remains interactive.<br>- `true`: modal; sets `aria-modal="true"` on the popup.<br>- `'trap-focus'`: reserved for future focus-trapping behavior. |
| `open` | `boolean` | `false` | Controlled open state. When set, the consumer is responsible for toggling. |
| `openOnHover` (attribute `open-on-hover`) | `boolean` | `false` | Open the popup on pointer hover instead of click. |
| `side` | `'top' \| 'bottom' \| 'left' \| 'right'` | `'top'` | Preferred side of the trigger for the popup. |

#### State

State is reflected as data attributes for CSS styling.

| Property | Type | Description |
| --- | --- | --- |
| `transitionStarting` | `boolean` | Whether the open transition is in progress. |
| `transitionEnding` | `boolean` | Whether the close transition is in progress. |
| `open` | `boolean` | |
| `status` | `'idle' \| 'starting' \| 'ending'` | |
| `side` | `'top' \| 'bottom' \| 'left' \| 'right'` | Preferred side of the trigger for the popup. |
| `align` | `'start' \| 'center' \| 'end'` | |
| `modal` | `boolean \| 'trap-focus'` | |

#### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-open` | — | Present when the popover is open. |
| `data-side` | `'top' \| 'bottom' \| 'left' \| 'right'` | Indicates the rendered side of the popover after collision handling. |
| `data-align` | `'start' \| 'center' \| 'end'` | Indicates how the popover is aligned relative to the specified side. |

#### CSS custom properties

| Variable | Description |
| --- | --- |
| `--media-popover-side-offset` | Distance between the popup and the trigger along the side axis. |
| `--media-popover-align-offset` | Distance between the popup and the trigger along the alignment axis. |
| `--media-popover-boundary-offset` | Minimum distance between the popup and the positioning boundary. |
| `--media-popover-anchor-width` | The anchor element's width. |
| `--media-popover-anchor-height` | The anchor element's height. |
| `--media-popover-available-width` | Available width between the trigger and the boundary edge. |
| `--media-popover-available-height` | Available height between the trigger and the boundary edge. |

#### Events

| Event | Description |
| --- | --- |
| `open-change` | Fired when the popover's open state changes. |

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
