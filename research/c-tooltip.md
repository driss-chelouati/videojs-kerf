# media-tooltip

A tooltip component for displaying contextual labels on hover and focus

## Import

```ts
import '@videojs/html/ui/tooltip';
import '@videojs/html/ui/tooltip-group';
import '@videojs/html/ui/tooltip-label';
import '@videojs/html/ui/tooltip-shortcut';
```

## Anatomy

```html
<media-tooltip-group>
  <button commandfor="my-tooltip">Hover me</button>
  <media-tooltip id="my-tooltip">
    <media-tooltip-label>Label text</media-tooltip-label>
    <media-tooltip-shortcut>K</media-tooltip-shortcut>
  </media-tooltip>
</media-tooltip-group>
```

## Behavior

Displays a short label anchored to a trigger element. Opens after a configurable `delay` (default 600ms) on hover or immediately on focus. Closes when the pointer leaves or focus moves away, with an optional `closeDelay`.

The `side` and `align` props control the preferred placement relative to the trigger. When the preferred side overflows the positioning boundary, the tooltip uses the opposite side if it has more space. Positioning uses CSS Anchor Positioning where supported, with a JavaScript measurement fallback.

The `<media-tooltip>` element is the popup itself. Link it to a trigger using the `commandfor` attribute on any button, pointing to the tooltip’s `id`. The element discovers its trigger automatically and manages open/close state and positioning. Wrap tooltip trigger/popup pairs in `<media-tooltip-group>` to coordinate timing — the group’s `delay`, `close-delay`, and `timeout` attributes control shared timing for all contained tooltips.

Tooltips inside a [player container](https://videojs.org/docs/framework/html/reference/components/player-container) also observe its popup group. By default, a tooltip does not open—or closes if already open—while a menu or popover attached to the same trigger is open. Set `sticky` when the tooltip should remain visible with that trigger’s popup.

`<media-tooltip-group>` coordinates tooltip delay timing only; it does not replace the container’s popup group.

## Styling

Use [CSS custom properties](#css-custom-properties) for positioning offsets:

```css
media-tooltip {
  --media-tooltip-side-offset: 8px;
  --media-tooltip-align-offset: 0px;
  --media-tooltip-boundary-offset: 8px;
}
```

Style based on open state, rendered side, and transition phases. `data-side` reflects the rendered side and can differ from the preferred `side` prop after collision handling:

```css
media-tooltip[data-open] {
  display: block;
}
media-tooltip[data-starting-style] {
  opacity: 0;
}
media-tooltip[data-ending-style] {
  opacity: 0;
}
media-tooltip[data-side="top"] {
  transform-origin: bottom center;
}
media-tooltip[data-side="bottom"] {
  transform-origin: top center;
}
```

## Accessibility

Tooltips are visual-only, supplementary labels. The popup renders with `role="presentation"` and is not referenced by the trigger with `aria-describedby`. Give the trigger its own accessible name instead of relying on tooltip content. Built-in media buttons already expose a state-aware `aria-label`, and their tooltips reuse that translated label. Tooltips still open on focus so keyboard users who can see the label receive the same visual hint.

## Examples

### Basic Usage

**index.html**

```html
<div class="demo">
  <button type="button" commandfor="tooltip-demo" class="trigger">Hover me</button>
  <media-tooltip id="tooltip-demo" class="media-tooltip"> Tooltip content </media-tooltip>
</div>
```

**index.css**

```css
.demo {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
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

.media-tooltip {
  --media-tooltip-side-offset: 8px;
  padding: 4px 10px;
  font-size: 13px;
  color: white;
  white-space: nowrap;
  pointer-events: none;
  background: rgba(0, 0, 0, 0.85);
  border-radius: 6px;
  backdrop-filter: blur(10px);
}
```

**index.ts**

```ts
import '@videojs/html/ui/tooltip';
```

### Grouping

Wrap tooltip trigger/popup pairs in `<media-tooltip-group>` to coordinate timing. The group’s `delay`, `close-delay`, and `timeout` attributes control shared timing for all contained tooltips.

**index.html**

```html
<media-tooltip-group class="demo">
  <button type="button" commandfor="tooltip-play" class="trigger">Play</button>
  <media-tooltip id="tooltip-play" class="media-tooltip">Play video</media-tooltip>

  <button type="button" commandfor="tooltip-mute" class="trigger">Mute</button>
  <media-tooltip id="tooltip-mute" class="media-tooltip">Mute audio</media-tooltip>

  <button type="button" commandfor="tooltip-fullscreen" class="trigger">Fullscreen</button>
  <media-tooltip id="tooltip-fullscreen" class="media-tooltip">Enter fullscreen</media-tooltip>
</media-tooltip-group>
```

**index.css**

```css
.demo {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}

.trigger {
  padding: 6px 16px;
  color: black;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
}

.media-tooltip {
  --media-tooltip-side-offset: 8px;
  padding: 4px 10px;
  font-size: 13px;
  color: white;
  white-space: nowrap;
  pointer-events: none;
  background: rgba(0, 0, 0, 0.85);
  border-radius: 6px;
  backdrop-filter: blur(10px);
}
```

**index.ts**

```ts
import '@videojs/html/ui/tooltip';
import '@videojs/html/ui/tooltip-group';
```

## API Reference

### media-tooltip-group

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `closeDelay` (attribute `close-delay`) | `number` | — | Default close delay in ms for tooltips in this group. |
| `delay` | `number` | — | Default open delay in ms for tooltips in this group. |
| `timeout` | `number` | — | Duration in ms after a tooltip closes during which the next tooltip opens instantly. |

### media-tooltip

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `align` | `'start' \| 'center' \| 'end'` | `'center'` | Alignment of the tooltip along the trigger's edge. |
| `boundary` | `'viewport' \| 'container' \| string & {}` | — | Boundary used to constrain the tooltip position. |
| `closeDelay` (attribute `close-delay`) | `number` | `0` | Delay in ms before closing after pointer leaves. |
| `defaultOpen` (attribute `default-open`) | `boolean` | `false` | Initial open state for uncontrolled usage. |
| `delay` | `number` | `600` | Delay in ms before opening on hover. |
| `disabled` | `boolean` | `false` | When true, the tooltip is disabled and will not open. |
| `disableHoverablePopup` (attribute `disable-hoverable-popup`) | `boolean` | `true` | When true, hovering the popup does not keep it open. |
| `open` | `boolean` | `false` | Controlled open state. |
| `side` | `'top' \| 'bottom' \| 'left' \| 'right'` | `'top'` | Preferred side of the trigger for the tooltip. |
| `sticky` | `boolean` | `false` | Whether the tooltip stays open when another popup opens from its trigger. |

#### State

State is reflected as data attributes for CSS styling.

| Property | Type | Description |
| --- | --- | --- |
| `transitionStarting` | `boolean` | Whether the open transition is in progress. |
| `transitionEnding` | `boolean` | Whether the close transition is in progress. |
| `open` | `boolean` | Whether the tooltip is currently visible. |
| `status` | `'idle' \| 'starting' \| 'ending'` | Current phase of the transition lifecycle. |
| `side` | `'top' \| 'bottom' \| 'left' \| 'right'` | Preferred side of the trigger for the tooltip. |
| `align` | `'start' \| 'center' \| 'end'` | How the tooltip is aligned relative to the specified side. |

#### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-open` | — | Present when the tooltip is open. |
| `data-side` | `'top' \| 'bottom' \| 'left' \| 'right'` | Indicates the rendered side of the tooltip after collision handling. |
| `data-align` | `'start' \| 'center' \| 'end'` | Indicates how the tooltip is aligned relative to the specified side. |

#### CSS custom properties

| Variable | Description |
| --- | --- |
| `--media-tooltip-side-offset` | Distance between the popup and the trigger along the side axis. |
| `--media-tooltip-align-offset` | Distance between the popup and the trigger along the alignment axis. |
| `--media-tooltip-boundary-offset` | Minimum distance between the popup and the positioning boundary. |
| `--media-tooltip-anchor-width` | The anchor element's width. |
| `--media-tooltip-anchor-height` | The anchor element's height. |
| `--media-tooltip-available-width` | Available width between the trigger and the boundary edge. |
| `--media-tooltip-available-height` | Available height between the trigger and the boundary edge. |

#### Events

| Event | Description |
| --- | --- |
| `open-change` | Fired when the tooltip's open state changes. |

### media-tooltip-label

Label region inside `media-tooltip`; parent syncs text from the trigger when linked to a media button.

#### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-open` | — | Present when the tooltip is open. |
| `data-side` | `'top' \| 'bottom' \| 'left' \| 'right'` | Indicates the rendered side of the tooltip after collision handling. |
| `data-align` | `'start' \| 'center' \| 'end'` | Indicates how the tooltip is aligned relative to the specified side. |

### media-tooltip-shortcut

Shortcut hint inside `media-tooltip`. CSS skins: `class="media-tooltip__kbd"`; Tailwind skins: `class` from `popup.tooltipShortcut`.

#### Data attributes

| Attribute | Type | Description |
| --- | --- | --- |
| `data-open` | — | Present when the tooltip is open. |
| `data-side` | `'top' \| 'bottom' \| 'left' \| 'right'` | Indicates the rendered side of the tooltip after collision handling. |
| `data-align` | `'start' \| 'center' \| 'end'` | Indicates how the tooltip is aligned relative to the specified side. |

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
