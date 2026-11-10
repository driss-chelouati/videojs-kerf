# media-menu

A composable menu component for settings, option selection, and actions

## Import

```ts
import '@videojs/html/ui/menu';
import '@videojs/html/ui/menu-content';
import '@videojs/html/ui/menu-item';
import '@videojs/html/ui/menu-group';
import '@videojs/html/ui/menu-group-label';
import '@videojs/html/ui/menu-separator';
import '@videojs/html/ui/menu-radio-group';
import '@videojs/html/ui/menu-radio-item';
import '@videojs/html/ui/menu-checkbox-item';
import '@videojs/html/ui/menu-item-indicator';
```

## Anatomy

`<media-menu>` is the root menu and its one positioned popup. The root and nested `<media-menu-content>` elements are its direct children and share that popup.

```html
<button type="button" commandfor="settings-menu">Settings</button>

<media-menu id="settings-menu">
  <media-menu-content>
    <!-- Parent menu item that opens a submenu -->
    <media-menu-item commandfor="submenu">
      Open submenu
    </media-menu-item>

    <!-- Other parent menu items -->
    <media-menu-group>
      <media-menu-group-label></media-menu-group-label>
      <media-menu-checkbox-item>
        <media-menu-item-indicator></media-menu-item-indicator>
      </media-menu-checkbox-item>
    </media-menu-group>
    <media-menu-separator></media-menu-separator>
    <media-menu-item></media-menu-item>
  </media-menu-content>

  <!-- Sibling Content opened by the parent item -->
  <media-menu-content id="submenu">
    <media-menu-item>Back</media-menu-item>
    <media-menu-radio-group>
      <media-menu-group-label></media-menu-group-label>
      <media-menu-radio-item>
        <media-menu-item-indicator></media-menu-item-indicator>
      </media-menu-radio-item>
    </media-menu-radio-group>
  </media-menu-content>
</media-menu>
```

## Behavior

Menus open from a trigger and close when you select an item, click outside, move focus away, or press Escape. Root menus use `side` and `align` as their preferred placement. When the preferred side overflows the positioning boundary, the menu uses the opposite side if it has more space.

Root menus inside a [player container](https://videojs.org/docs/framework/html/reference/components/player-container) join its popup group. Opening one closes any other root menu or popover that is open in the same container. Submenus remain part of their root menu instead of registering separately.

To create a submenu, add another `<media-menu-content>` as a sibling, give it an `id`, and point the parent `<media-menu-item>` at it with `commandfor`.

Media option groups share their option state with the enclosing menu: the selected value, and whether the options are disabled, hidden, or available. The menu’s trigger inherits the disabled and hidden state and exposes `data-availability`, and the menu closes if its options disappear while open. See [PlaybackRateRadioGroup](https://videojs.org/docs/framework/html/reference/components/playback-rate-radio-group), [QualityRadioGroup](https://videojs.org/docs/framework/html/reference/components/quality-radio-group), [AudioTrackRadioGroup](https://videojs.org/docs/framework/html/reference/components/audio-track-radio-group), and [CaptionsRadioGroup](https://videojs.org/docs/framework/html/reference/components/captions-radio-group).

The generated radio group publishes its state to the `<media-menu>` that contains it. Add an element with `data-part="hint"` inside the parent `<media-menu-item>` and the menu writes the selected label into it:

```html
<media-menu-item commandfor="quality-menu">
  Quality
  <span data-part="hint"></span>
</media-menu-item>
```

## Styling

Use data attributes to style open state, highlighted items, selected radio items, and submenu views:

`data-highlighted` identifies the current menu item. Its value is `"pointer"` when pointer movement caused the highlight and an empty string for other highlights, including keyboard navigation and type-ahead search. Use `[data-highlighted]` to match any highlighted item or `[data-highlighted=""]` to match highlights that were not caused by pointer movement.

The root `<media-menu>` receives `data-open`, `data-side`, and `data-align`. Each `<media-menu-content>` receives menu state such as `data-open` and `data-submenu`; a content element with an open logical child receives `data-child-open`.

Every navigable item receives `data-item`. Use `[data-item]` when one rule should target regular, radio, checkbox, and submenu-trigger items together.

```css
media-menu[data-open] {
  opacity: 1;
}

media-menu-content[data-child-open] {
  translate: -100% 0;
}

media-menu-item[data-highlighted] {
  background: rgba(255, 255, 255, 0.16);
  transition: background-color 100ms ease-in-out;
}

media-menu-item[data-highlighted=""] {
  transition-duration: 0ms;
}

media-menu-radio-item[aria-checked="true"] {
  font-weight: 600;
}
```

## Accessibility

Menu content renders with `role="menu"`. Items use `menuitem`, `menuitemradio`, or `menuitemcheckbox` roles. Radio and checkbox items reflect selection with `aria-checked`.

Keyboard controls:

- Enter / Space: Select the highlighted item.
- Arrow Up / Arrow Down: Move between items.
- Arrow Right: Open a submenu.
- Arrow Left: Return to the parent menu.
- Escape: Close the root menu or return from a submenu.

Use `<media-menu-group-label>` inside grouped choices so the group receives an accessible label.

## Examples

### Basic usage

**index.html**

```html
<video-player class="video-player">
  <media-container>
    <hlsjs-video
      class="video-media"
      src="https://stream.mux.com/s41JYeqIpBMBzE4OzxDyGR2yrp2hD1CQ6gJN9SlVGDQ.m3u8"
      autoplay
      crossorigin="anonymous"
      muted
      playsinline
      loop
    >
      <track kind="captions" src="/docs/demos/captions-button/captions.vtt" srclang="en" label="English" />
      <track kind="subtitles" src="/docs/demos/captions-button/captions.vtt" srclang="es" label="Spanish" />
    </hlsjs-video>
    <div class="menu-bar">
      <button type="button" commandfor="settings-menu" class="settings-trigger">Settings</button>
      <media-menu id="settings-menu" side="top" align="end" class="menu">
        <media-menu-content class="menu-content">
          <media-menu-item commandfor="quality-menu" class="menu-item">
            <span>Quality</span>
            <span class="menu-value">
              <span data-part="hint"></span>
              <span aria-hidden="true">›</span>
            </span>
          </media-menu-item>
          <media-menu-item commandfor="audio-menu" class="menu-item">
            <span>Audio</span>
            <span class="menu-value">
              <span data-part="hint"></span>
              <span aria-hidden="true">›</span>
            </span>
          </media-menu-item>
          <media-menu-item commandfor="speed-menu" class="menu-item">
            <span>Speed</span>
            <span class="menu-value">
              <span data-part="hint"></span>
              <span aria-hidden="true">›</span>
            </span>
          </media-menu-item>
          <media-menu-item commandfor="captions-menu" class="menu-item">
            <span>Captions</span>
            <span class="menu-value">
              <span data-part="hint"></span>
              <span aria-hidden="true">›</span>
            </span>
          </media-menu-item>
          <media-menu-item class="menu-item">Copy link</media-menu-item>
        </media-menu-content>
        <media-menu-content id="quality-menu" class="menu-panel">
          <media-menu-item class="menu-back">
            <span aria-hidden="true">‹</span>
            Quality
          </media-menu-item>
          <media-quality-radio-group class="menu-group">
            <template>
              <media-menu-radio-item class="menu-item">
                <span>
                  <span data-part="label"></span>
                  <sup data-part="tier" class="menu-tier"></sup>
                </span>
                <span data-part="badge" class="menu-badge"></span>
                <media-menu-item-indicator force-mount class="menu-indicator">✓</media-menu-item-indicator>
              </media-menu-radio-item>
            </template>
          </media-quality-radio-group>
        </media-menu-content>
        <media-menu-content id="audio-menu" class="menu-panel">
          <media-menu-item class="menu-back">
            <span aria-hidden="true">‹</span>
            Audio
          </media-menu-item>
          <media-audio-track-radio-group class="menu-group">
            <template>
              <media-menu-radio-item class="menu-item">
                <span data-part="label"></span>
                <media-menu-item-indicator force-mount class="menu-indicator">✓</media-menu-item-indicator>
              </media-menu-radio-item>
            </template>
          </media-audio-track-radio-group>
        </media-menu-content>
        <media-menu-content id="speed-menu" class="menu-panel">
          <media-menu-item class="menu-back">
            <span aria-hidden="true">‹</span>
            Speed
          </media-menu-item>
          <media-playback-rate-radio-group class="menu-group">
            <template>
              <media-menu-radio-item class="menu-item">
                <span data-part="label"></span>
                <media-menu-item-indicator force-mount class="menu-indicator">✓</media-menu-item-indicator>
              </media-menu-radio-item>
            </template>
          </media-playback-rate-radio-group>
        </media-menu-content>
        <media-menu-content id="captions-menu" class="menu-panel">
          <media-menu-item class="menu-back">
            <span aria-hidden="true">‹</span>
            Captions
          </media-menu-item>
          <media-captions-radio-group class="menu-group">
            <template>
              <media-menu-radio-item class="menu-item">
                <span data-part="label"></span>
                <media-menu-item-indicator force-mount class="menu-indicator">✓</media-menu-item-indicator>
              </media-menu-radio-item>
            </template>
          </media-captions-radio-group>
        </media-menu-content>
      </media-menu>
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

.video-media {
  width: 100%;
}

.menu-bar {
  position: absolute;
  right: 10px;
  bottom: 10px;
}

.settings-trigger {
  padding: 6px 16px;
  color: black;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.75);
  border: 1px solid rgba(255, 255, 255, 0.35);
  border-radius: 9999px;
  backdrop-filter: blur(10px);
}

.menu {
  --media-menu-side-offset: 8px;
  --menu-transition-duration: 220ms;
  position: relative;
  box-sizing: border-box;
  width: var(--media-menu-width);
  min-width: 180px;
  max-width: var(--media-menu-available-width, var(--media-popover-available-width, none));
  height: var(--media-menu-height);
  max-height: var(--media-menu-available-height, var(--media-popover-available-height, none));
  padding: 6px;
  overflow: hidden;
  overscroll-behavior: none;
  font-size: 14px;
  color: white;
  background: rgba(0, 0, 0, 0.88);
  border-radius: 8px;
  backdrop-filter: blur(10px);
  transition-timing-function: ease-in-out;
  transition-duration: var(--menu-transition-duration);
  transition-property: width, height, opacity, filter;
}

.menu-content,
.menu-panel {
  position: absolute;
  inset: 0;
  display: grid;
  gap: 2px;
  padding: 6px;
  overflow: auto;
  overscroll-behavior: none;
  outline: none;
  translate: 0 0;
  transition-timing-function: ease-in-out;
  transition-duration: var(--menu-transition-duration);
  transition-property: translate, filter;
}

.menu-content[data-child-open] {
  filter: blur(8px);
  translate: -100% 0;
}

.menu-panel[data-submenu] {
  z-index: 1;
}

.menu-panel[data-submenu][data-starting-style],
.menu-panel[data-submenu][data-ending-style] {
  overflow: hidden;
  pointer-events: none;
  filter: blur(8px);
  translate: 100% 0;
}

.menu-item,
.menu-back {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 32px;
  padding: 0 10px;
  font: inherit;
  color: inherit;
  cursor: pointer;
  background: none;
  border: 0;
  border-radius: 6px;
}

.menu-item[data-highlighted],
.menu-back:hover {
  background: rgba(255, 255, 255, 0.16);
}

.menu-back {
  gap: 8px;
  justify-content: flex-start;
}

.menu-item[data-availability="unavailable"] {
  display: none;
}

.menu-value {
  display: inline-flex;
  gap: 8px;
  align-items: center;
  color: rgba(255, 255, 255, 0.72);
}

.menu-value [aria-hidden] {
  font-size: 18px;
  line-height: 1;
}

.menu-back [aria-hidden] {
  font-size: 18px;
  line-height: 1;
  color: rgba(255, 255, 255, 0.72);
}

.menu-group {
  display: grid;
  gap: 2px;
}

.menu-tier {
  margin-left: 2px;
  font-size: 10px;
}

.menu-badge {
  margin-left: auto;
  color: rgba(255, 255, 255, 0.72);
}

.menu-indicator {
  opacity: 0;
}

media-menu-radio-item[aria-checked="true"] .menu-indicator {
  opacity: 1;
}
```

**index.ts**

```ts
import '@videojs/html/video/player';
import '@videojs/html/ui/container';
import '@videojs/html/media/hlsjs-video';
import '@videojs/html/ui/menu';
import '@videojs/html/ui/menu-content';
import '@videojs/html/ui/menu-item';
import '@videojs/html/ui/menu-radio-item';
import '@videojs/html/ui/menu-item-indicator';
import '@videojs/html/ui/quality-radio-group';
import '@videojs/html/ui/audio-track-radio-group';
import '@videojs/html/ui/playback-rate-radio-group';
import '@videojs/html/ui/captions-radio-group';
```

## API Reference

### media-menu

Root menu state and positioned popup. Content pages are direct children.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `align` | `'start' \| 'center' \| 'end'` | `'start'` | Alignment along the trigger's edge. Root menus only. |
| `boundary` | `'viewport' \| 'container' \| string & {}` | — | Boundary used to constrain the root menu popup. |
| `closeOnEscape` (attribute `close-on-escape`) | `boolean` | `true` | Close the menu when Escape is pressed at root level. |
| `closeOnOutsideClick` (attribute `close-on-outside-click`) | `boolean` | `true` | Close the menu when clicking outside. Root menus only. |
| `defaultOpen` (attribute `default-open`) | `boolean` | `false` | Initial open state (uncontrolled). |
| `open` | `boolean` | `false` | Controlled open state. |
| `side` | `'top' \| 'bottom' \| 'left' \| 'right'` | `'bottom'` | Preferred side of the trigger for the menu. Root menus only. |

#### State

State is reflected as data attributes for CSS styling.

| Property | Type | Description |
| --- | --- | --- |
| `transitionStarting` | `boolean` | Whether the open transition is in progress. |
| `transitionEnding` | `boolean` | Whether the close transition is in progress. |
| `open` | `boolean` | |
| `status` | `'idle' \| 'starting' \| 'ending'` | |
| `side` | `'top' \| 'bottom' \| 'left' \| 'right' \| undefined` | Preferred side of the trigger for the menu. Root menus only. |
| `align` | `'start' \| 'center' \| 'end' \| undefined` | |
| `isSubmenu` | `boolean` | Whether this menu is nested inside another menu's content. |

#### CSS custom properties

| Variable | Description |
| --- | --- |
| `--media-popover-side-offset` | Distance between the popup and the trigger along the side axis. |
| `--media-popover-align-offset` | Distance between the popup and the trigger along the alignment axis. |
| `--media-popover-boundary-offset` | Minimum distance between the popup and the positioning boundary. |
| `--media-popover-anchor-width` | Width of the trigger, set by popup positioning. |
| `--media-popover-anchor-height` | Height of the trigger, set by popup positioning. |
| `--media-menu-width` | Width of the active menu panel (px). |
| `--media-menu-height` | Height of the active menu panel (px). |
| `--media-menu-available-width` | Width available within the positioning boundary (px). |
| `--media-menu-available-height` | Height available within the positioning boundary (px). |

#### Events

| Event | Description |
| --- | --- |
| `open-change` | Fired before the menu's open state changes. Cancel the event to prevent the change. |

### media-menu-checkbox-item

Menu item that toggles `checked` when activated and leaves the menu open. The element itself takes `role="menuitemcheckbox"`.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `checked` | `boolean` | — | Whether the item is currently checked. |
| `disabled` | `boolean` | — | Whether the item is disabled. |

#### Data attributes

| Attribute | Description |
| --- | --- |
| `data-item` | Present on all navigable item types: Item, RadioItem, CheckboxItem, and the Trigger when acting as a submenu trigger inside a parent menu. Use `[data-item]` as a shared selector to target all item types at once. |
| `data-highlighted` | Present when the item is highlighted. Set to `pointer` when pointer movement caused the highlight; otherwise empty. |

#### Events

| Event | Description |
| --- | --- |
| `checked-change` | Fired when the checked state changes. |

### media-menu-content

One accessible menu page. Root and nested pages are sibling children of `<media-menu>`.

#### Events

| Event | Description |
| --- | --- |
| `open-change` | |

### media-menu-group

Groups related menu items; the element itself takes `role="group"`. A `<media-menu-group-label>` child names the group unless it already has an `aria-label` or `aria-labelledby`.

### media-menu-group-label

Non-interactive label that names its enclosing `<media-menu-group>` or `<media-menu-radio-group>`.

### media-menu-item

Menu action; the element itself takes `role="menuitem"`. Activation fires a cancelable `select` event and then closes the menu, unless `commandfor` names a nested `<media-menu-content>` page to open instead.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `disabled` | `boolean` | — | Whether the item is disabled. |

#### Data attributes

| Attribute | Description |
| --- | --- |
| `data-item` | Present on all navigable item types: Item, RadioItem, CheckboxItem, and the Trigger when acting as a submenu trigger inside a parent menu. Use `[data-item]` as a shared selector to target all item types at once. |
| `data-highlighted` | Present when the item is highlighted. Set to `pointer` when pointer movement caused the highlight; otherwise empty. |

### media-menu-item-indicator

Decorative checked-state mark inside a menu item, hidden from assistive technology. It stays `hidden` unless `checked` or `force-mount` is set; option radio groups set `checked` on the indicators in the items they generate.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `checked` | `boolean` | — | Whether the indicator is currently shown. Typically bound to the parent item's checked state. |
| `forceMount` (attribute `force-mount`) | `boolean` | — | When `true`, renders even when unchecked (useful for animating out). Defaults to `false`. |

### media-menu-radio-group

Group of mutually exclusive `<media-menu-radio-item>` children; the element itself takes `role="group"`.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `value` | `string` | — | The currently selected value. |

#### Events

| Event | Description |
| --- | --- |
| `value-change` | Fired when the selected value changes. |

### media-menu-radio-item

Menu item that selects its `value` in the enclosing `<media-menu-radio-group>` and closes the menu. The element itself takes `role="menuitemradio"`, checked while its value matches the group's.

#### Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `disabled` | `boolean` | — | Whether the item is disabled. |
| `value` | `string` | — | The value this item represents. |

#### Data attributes

| Attribute | Description |
| --- | --- |
| `data-item` | Present on all navigable item types: Item, RadioItem, CheckboxItem, and the Trigger when acting as a submenu trigger inside a parent menu. Use `[data-item]` as a shared selector to target all item types at once. |
| `data-highlighted` | Present when the item is highlighted. Set to `pointer` when pointer movement caused the highlight; otherwise empty. |

### media-menu-separator

Visual divider between groups of menu items; the element itself takes `role="separator"`.

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
