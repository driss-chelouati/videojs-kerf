# Kerf

A Video.js 10 skin built on one cut: the picture makes room for the controls, so they always sit on solid ground, in
your product's own colour. An entry to the Video.js Skins Design Challenge on Contra.

- `skin/src/`: the skin itself (HTML and CSS), ready to drop into any Video.js 10 project. Start at `src/video/skin.html`.
- `skin/apps/preview/`: the demo site (player and design pages, built with Vite) and the CLI workbench.
- `skin/design/spec.md`: the design rules the build follows.
- `board/`: the approved design board.
- `brand/`: the Kerf mark and lockups.

## Run

```sh
cd skin
npm install
npm run dev
```

## Customise

```css
.kerf {
  --media-accent-color: #d4f53c;
  --media-border-radius: 20px;
}
```

On the skin root: `data-surface="light"` (or `auto`), `data-motion="reduce"`, `data-poster-controls="show"`.

## Credits

- Design and build: Driss Chelouati, https://drisschelouati.dev
- Player: Video.js 10 (Apache 2.0), with its official Default icon set.
- Film: the Sparvek launch film by Orvio, streamed from Mux.
- Type: Geist and Geist Mono (SIL Open Font License). Site icons: Lucide (ISC).

## Licence

Apache License 2.0. See `LICENSE`.
