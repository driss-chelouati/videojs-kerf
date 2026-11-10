# Icons

The SVG icon sets used by the packaged skins, as React components, SVG strings, and the media-icon element

The icons the packaged skins render. Skin source added with the [Shadcn registry](https://videojs.org/docs/guides/installation/shadcn?framework=html) imports its icons from these modules, and your own controls can use them too.

Each icon is available as an SVG string and by name through the `<media-icon>` element.

## Import

Register `<media-icon>`:

```ts
import "@videojs/html/icons/element";
```

Or import SVG strings:

```ts
import { playIcon } from "@videojs/html/icons";
```

## Icon sets

Four sets ship with the same icon names and different designs.

| Set | `family` | SVG strings | Used by |
| --- | --- | --- | --- |
| Default | `default` | `@videojs/html/icons` or `@videojs/html/icons/default` | The default skins, such as [`<video-skin>`](https://videojs.org/docs/framework/html/reference/components/video-skin) |
| Neutral | `neutral` | `@videojs/html/icons/neutral` | The neutral skins, such as [`<video-neutral-skin>`](https://videojs.org/docs/framework/html/reference/components/video-neutral-skin) |
| Compat | `compat` | `@videojs/html/icons/compat` | The compat skins, such as [`<video-compat-skin>`](https://videojs.org/docs/framework/html/reference/components/video-compat-skin) |
| Scaffold | `scaffold` | `@videojs/html/icons/scaffold` | The scaffold skins, such as [`<video-scaffold-skin>`](https://videojs.org/docs/framework/html/reference/components/video-scaffold-skin) |

## Available icons

| Name | Export |
| --- | --- |
| `airplay-enter` | `airPlayEnterIcon` |
| `airplay-exit` | `airPlayExitIcon` |
| `captions-off` | `captionsOffIcon` |
| `captions-on` | `captionsOnIcon` |
| `cast-enter` | `castEnterIcon` |
| `cast-exit` | `castExitIcon` |
| `check` | `checkIcon` |
| `chevron` | `chevronIcon` |
| `fullscreen-enter` | `fullscreenEnterIcon` |
| `fullscreen-exit` | `fullscreenExitIcon` |
| `gear` | `gearIcon` |
| `pause` | `pauseIcon` |
| `pip-enter` | `pipEnterIcon` |
| `pip-exit` | `pipExitIcon` |
| `play` | `playIcon` |
| `quality` | `qualityIcon` |
| `restart` | `restartIcon` |
| `seek` | `seekIcon` |
| `speech` | `speechIcon` |
| `speed` | `speedIcon` |
| `spinner` | `spinnerIcon` |
| `switches` | `switchesIcon` |
| `volume-high` | `volumeHighIcon` |
| `volume-low` | `volumeLowIcon` |
| `volume-off` | `volumeOffIcon` |

## Element

`<media-icon>` renders a registered icon as its child `<svg>`, in the light DOM. It renders nothing when the name is not registered in the family.

| Attribute | Default | Description |
| --- | --- | --- |
| `name` | — | Icon name from the [available icons](#available-icons), such as `play` |
| `family` | `default` | Icon set to read from, such as `neutral` |

```html
<media-play-button>
  <media-icon class="play-icon" name="play"></media-icon>
  <media-icon class="pause-icon" name="pause" family="neutral"></media-icon>
</media-play-button>
```

Each module below defines `<media-icon>` if it is not already defined:

| Module | Registers |
| --- | --- |
| `@videojs/html/icons/element` | Every set, loading each one the first time a `<media-icon>` asks for its family |
| `@videojs/html/icons/element/default` | The default set, up front |
| `@videojs/html/icons/element/neutral` | The neutral set, up front |
| `@videojs/html/icons/element/compat` | The compat set, up front |

## SVG strings

Each icon export from `@videojs/html/icons`, `@videojs/html/icons/default`, `@videojs/html/icons/neutral`, and `@videojs/html/icons/compat` is the icon’s SVG markup as a string; `@videojs/html/icons` also exports [`registerIcons`](#registericons). Importing them does not define `<media-icon>`.

```ts
import { playIcon } from "@videojs/html/icons";

button.innerHTML = playIcon;
```

## `registerIcons`

`registerIcons(family, icons)` registers SVG strings under icon names for `<media-icon>` and defines the element if needed. Only the icons you import ship, which is how skin source from the Shadcn registry registers its icons. Registering into an existing family adds to it, and `<media-icon>` elements already in the page update.

```ts
import { pauseIcon, playIcon, registerIcons } from "@videojs/html/icons";

registerIcons("default", { play: playIcon, pause: pauseIcon });
registerIcons("brand", { play: '<svg viewBox="0 0 18 18">…</svg>' });
```

```html
<media-icon name="play"></media-icon>
<media-icon name="play" family="brand"></media-icon>
```

Once a family has registered icons, `<media-icon>` renders only those for it, even when `@videojs/html/icons/element` is also imported. `registerIcons` throws when a different element is already defined as `media-icon` and does not support registration.

## Styling

Icons use `fill="currentColor"`, so they take the text color of their parent. They are drawn on an 18×18 grid and render most sharply at 18px or a whole multiple, such as 36px.

```css
media-icon svg {
  width: 36px;
  height: 36px;
  color: white;
}
```

## Accessibility

Every icon renders with `aria-hidden="true"`. Give the surrounding control its accessible name. Built-in buttons, such as the [play button](https://videojs.org/docs/framework/html/reference/components/play-button), provide one automatically.

---

HTML documentation: https://videojs.org/docs/framework/html/llms.txt
All documentation: https://videojs.org/llms.txt
