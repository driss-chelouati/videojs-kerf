# Video.js v10 — HTML Documentation

> Every page below is also available as Markdown at its `.md` URL. The whole set in one file (about 325k tokens): https://videojs.org/docs/framework/html/llms-full.txt

> Install the [Video.js skill](https://github.com/videojs/skills) to help AI coding agents find version-matched pages from this index.

> The `video.js` package on npm contains no player; install `video.js@8` to stay on Video.js 8. Video.js 10 ships as `@videojs/html`; to move existing Video.js 8 code, read https://videojs.org/docs/framework/html/guides/migrate-from-video-js-8.md

> Vidstack Player is in security-only maintenance. To move existing `vidstack` code, read https://videojs.org/docs/framework/html/guides/migrate-from-vidstack.md

> Print version-matched installation options without changing files: `npx @videojs/cli agents init`, then pass `--framework html` with the other choices. Installation guide index: https://videojs.org/docs/guides/installation.md

## Guides

Installation, migration, concepts, playback guides, customization, and tooling for Video.js.

Section index: [guides/llms.txt](https://videojs.org/docs/framework/html/guides/llms.txt). This section in one file (about 142k tokens): https://videojs.org/docs/framework/html/guides/llms-full.txt

### Getting Started

Install Video.js, customize a skin, understand its main pieces, check browser and AI tool support, and contribute.

- [HTML Installation Guide](https://videojs.org/docs/guides/installation/html.md): Install Video.js with HTML custom elements and build an accessible, customizable video player
- [Vue Installation Guide](https://videojs.org/docs/guides/installation/vue.md): Install Video.js in Vue or Nuxt and build a video player with HTML custom elements
- [Svelte Installation Guide](https://videojs.org/docs/guides/installation/svelte.md): Install Video.js in Svelte or SvelteKit and build a video player with HTML custom elements
- [Shadcn Installation Guide](https://videojs.org/docs/guides/installation/shadcn.md): Add editable React or HTML skin source with the Shadcn registry
- [CDN Installation Guide](https://videojs.org/docs/guides/installation/cdn.md): Load Video.js from jsDelivr and build an HTML video player without installing Video.js packages
- [Build your own UI component](https://videojs.org/docs/framework/html/guides/build-your-own-component.md): Create custom player controls that read state, dispatch actions, and stay accessible.
- [Architecture](https://videojs.org/docs/framework/html/guides/architecture.md): How Video.js players are structured — state, UI, media, and extensions
- [Customize skins](https://videojs.org/docs/framework/html/guides/customize-skins.md): Style a packaged Video.js skin or add its source to change controls, layout, styles, and interactions
- [Build your own skin](https://videojs.org/docs/framework/html/guides/build-your-own-skin.md): Create a skin project, preview it locally, and compose your own player interface from Video.js UI components
- [Why Video.js?](https://videojs.org/docs/framework/html/guides/why-videojs.md): The open-source video player for React and HTML. Lightweight, accessible components built for performance and streaming.
- [Browser support](https://videojs.org/docs/framework/html/guides/browser-support.md): Browsers and rendering environments supported by Video.js 10, and how the packaged skins reach them
- [Build with AI](https://videojs.org/docs/framework/html/guides/build-with-ai.md): Install the Video.js skill and give AI coding agents version-matched docs for building and migrating players
- [v10 Roadmap](https://videojs.org/docs/framework/html/guides/v10-roadmap.md): Where Video.js v10 stands, what comes after 10.0, and the support plan for Video.js 8
- [Contribute to Video.js](https://github.com/videojs/video.js/blob/main/CONTRIBUTING.md)

### Frameworks

Guides for using the HTML version of Video.js with Vue, Nuxt, Svelte, or SvelteKit.

- [Vue](https://videojs.org/docs/framework/html/guides/vue.md): Add Video.js to a Vue or Nuxt app
- [Svelte](https://videojs.org/docs/framework/html/guides/svelte.md): Add Video.js to a Svelte or SvelteKit app

### Environment

TypeScript, bundlers, the CDN, self-hosting, and Content Security Policy.

- [TypeScript](https://videojs.org/docs/framework/html/guides/typescript.md): TypeScript version and module resolution requirements for Video.js packages
- [Bundlers](https://videojs.org/docs/framework/html/guides/bundlers.md): Bundler requirements for Video.js package exports, CSS, and wrapper libraries
- [CDN](https://videojs.org/docs/framework/html/guides/cdn.md): Understand the browser-ready bundles, stylesheets, and URL layout published by the Video.js CDN
- [Self-host the player](https://videojs.org/docs/framework/html/guides/self-hosting.md): Serve the Video.js HTML player from your own origin for offline, air-gapped, or restricted-network deployments
- [Content Security Policy](https://videojs.org/docs/framework/html/guides/content-security-policy.md): Allow the media, images, workers, and styles a Video.js player needs when your page enforces a Content Security Policy

### Concepts

Understanding-oriented pages that explain how and why things work. Read these to build a mental model of the library.

- [Features](https://videojs.org/docs/framework/html/guides/features.md): The state and actions each feature adds to the player
- [Skins](https://videojs.org/docs/framework/html/guides/skins.md): Packaged player designs that include both UI components and their styles.
- [Presets](https://videojs.org/docs/framework/html/guides/presets.md): Pre-packaged player configurations that bundle state management, skins, and media components for specific use cases.
- [UI components](https://videojs.org/docs/framework/html/guides/ui-components.md): How Video.js UI components use focused elements, data attributes for state, and compound composition.
- [Accessibility](https://videojs.org/docs/framework/html/guides/accessibility.md): How Video.js approaches accessibility, and what you should consider if you're deeply customizing your player
- [Media sources](https://videojs.org/docs/framework/html/guides/media-sources.md): Set what a media component plays and how its engine plays it with the structured source property

### Playback

Guides for one player capability each: the recommended setup, how it works, browser constraints, variations, and troubleshooting.

- [Autoplay](https://videojs.org/docs/framework/html/guides/autoplay.md): Start playback automatically and handle browser autoplay restrictions.
- [Automatically show and hide controls](https://videojs.org/docs/framework/html/guides/controls.md): Show controls while the user is active, hide them during playback, and toggle them by touch.
- [Add a poster and loading placeholder](https://videojs.org/docs/framework/html/guides/poster.md): Set the image shown before playback, then add a lightweight placeholder while it loads
- [Show captions and subtitles](https://videojs.org/docs/framework/html/guides/captions.md): Show captions and subtitles, and let users turn them on and pick a language.
- [Add keyboard shortcuts and gestures](https://videojs.org/docs/framework/html/guides/keyboard-shortcuts.md): Add keyboard shortcuts, tap and double-tap gestures, and on-screen feedback for input actions.
- [Play live streams](https://videojs.org/docs/framework/html/guides/live-streams.md): Play live streams with live-edge tracking, DVR windows, and stream-type detection.
- [Add a quality selector](https://videojs.org/docs/framework/html/guides/quality.md): Read available renditions, let the engine adapt automatically, and offer manual quality selection.
- [Go fullscreen and lock orientation](https://videojs.org/docs/framework/html/guides/fullscreen.md): Present the player fullscreen with custom controls intact, and lock screen orientation on mobile.
- [Use picture-in-picture](https://videojs.org/docs/framework/html/guides/picture-in-picture.md): Pop the video into a floating window, with availability detection and state that tracks every entry path.
- [Show timeline thumbnail previews](https://videojs.org/docs/framework/html/guides/thumbnails.md): Preview frames along the timeline while the user scrubs, powered by a storyboard track.
- [Cast to AirPlay and Chromecast](https://videojs.org/docs/framework/html/guides/casting.md): Send playback to AirPlay and Google Cast devices, with availability detection and connection state.
- [Handle playback errors](https://videojs.org/docs/framework/html/guides/playback-errors.md): Display playback failures, report them, and choose a useful recovery action.
- [Remember user preferences](https://videojs.org/docs/framework/html/guides/user-preferences.md): Save volume and caption preferences, restore them after loading, and adapt the pattern for quality selection.
- [Add a background video](https://videojs.org/docs/framework/html/guides/background-video.md): Add an accessible background video from an MP4, WebM, HLS, or Mux source
- [Internationalize the player](https://videojs.org/docs/framework/html/guides/internationalization.md): Translate player labels and announcements: shipped locale packs, custom translations, runtime switching, and server rendering.
- [Track video telemetry with Google Analytics 4](https://videojs.org/docs/framework/html/guides/google-analytics.md): Track video engagement, progress milestones, and playback interactions by adding the Google Analytics extension to a player
- [Monitor playback with Mux Data](https://videojs.org/docs/framework/html/guides/mux-data.md): Measure startup time, rebuffering, failures, and watch time by adding the Mux Data extension to a player

### Migrate

Guides for moving an existing player integration to Video.js v10, one per player you might be coming from.

- [Migrate to Video.js v10](https://videojs.org/docs/framework/html/guides/migrate.md): Understand how Video.js v10 differs from the players it brings together, and choose the migration guide for the player you use today.
- [Migrate from Video.js 8](https://videojs.org/docs/framework/html/guides/migrate-from-video-js-8.md): Move a Video.js 8 integration to v10, mapping the options object, techs, plugins, and player API onto composed components
- [Migrate from Mux Player](https://videojs.org/docs/framework/html/guides/migrate-from-mux-player.md): Move a Mux Player embed to Video.js v10 using a player, media component, skin, and analytics extension
- [Migrate from Plyr](https://videojs.org/docs/framework/html/guides/migrate-from-plyr.md): Move an existing Plyr integration to Video.js v10, mapping Plyr options and its instance API onto components and player state
- [Migrate from Media Chrome](https://videojs.org/docs/framework/html/guides/migrate-from-media-chrome.md): Move a Media Chrome player to Video.js v10, mapping its controller, controls, styles, and imperative calls
- [Migrate from Vidstack](https://videojs.org/docs/framework/html/guides/migrate-from-vidstack.md): Move a Vidstack Player integration to Video.js 10, mapping the player, providers, layouts, and media store onto composed components

## Components

API reference for skins, media components, extensions, and interface components.

Section index: [reference/components/llms.txt](https://videojs.org/docs/framework/html/reference/components/llms.txt). This section in one file (about 133k tokens): https://videojs.org/docs/framework/html/reference/components/llms-full.txt

### Layout

API reference for the components that establish a player and lay out its interface.

- [video-player](https://videojs.org/docs/framework/html/reference/components/player.md): The state boundary — creates a store and broadcasts it to all descendants.
- [media-container](https://videojs.org/docs/framework/html/reference/components/player-container.md): The player's visual and interaction surface for layout, fullscreen, focus, and user activity.
- [media-controls](https://videojs.org/docs/framework/html/reference/components/controls.md): Container component for composing and auto-hiding video player controls on user interaction

### Skins

API reference for the packaged skins each preset ships.

- [video-skin](https://videojs.org/docs/framework/html/reference/components/video-skin.md): The video preset's default skin with the modern, frosted look
- [video-neutral-skin](https://videojs.org/docs/framework/html/reference/components/video-neutral-skin.md): The video preset's visually lighter skin, closer to a classic control bar
- [video-compat-skin](https://videojs.org/docs/framework/html/reference/components/video-compat-skin.md): The video preset's plain, unbranded skin, a polished step above native controls
- [video-scaffold-skin](https://videojs.org/docs/framework/html/reference/components/video-scaffold-skin.md): A video skin with minimal styling for custom skins
- [audio-skin](https://videojs.org/docs/framework/html/reference/components/audio-skin.md): The audio preset's default skin with the modern, frosted look
- [audio-neutral-skin](https://videojs.org/docs/framework/html/reference/components/audio-neutral-skin.md): The audio preset's visually lighter skin, closer to a classic control bar
- [audio-compat-skin](https://videojs.org/docs/framework/html/reference/components/audio-compat-skin.md): The audio preset's plain, unbranded skin, a polished step above native controls
- [audio-scaffold-skin](https://videojs.org/docs/framework/html/reference/components/audio-scaffold-skin.md): An audio skin with minimal styling for custom skins
- [live-video-skin](https://videojs.org/docs/framework/html/reference/components/live-video-skin.md): The live video preset's default skin, which swaps time controls for a Live button
- [live-video-neutral-skin](https://videojs.org/docs/framework/html/reference/components/live-video-neutral-skin.md): The live video preset's visually lighter skin, closer to a classic control bar
- [live-video-compat-skin](https://videojs.org/docs/framework/html/reference/components/live-video-compat-skin.md): The live video preset's plain, unbranded skin, a polished step above native controls
- [live-video-scaffold-skin](https://videojs.org/docs/framework/html/reference/components/live-video-scaffold-skin.md): A live video skin with minimal styling for custom skins
- [live-audio-skin](https://videojs.org/docs/framework/html/reference/components/live-audio-skin.md): The live audio preset's default skin, which swaps time controls for a Live button
- [live-audio-neutral-skin](https://videojs.org/docs/framework/html/reference/components/live-audio-neutral-skin.md): The live audio preset's visually lighter skin, closer to a classic control bar
- [live-audio-compat-skin](https://videojs.org/docs/framework/html/reference/components/live-audio-compat-skin.md): The live audio preset's plain, unbranded skin, a polished step above native controls
- [live-audio-scaffold-skin](https://videojs.org/docs/framework/html/reference/components/live-audio-scaffold-skin.md): A live audio skin with minimal styling for custom skins
- [background-video-skin](https://videojs.org/docs/framework/html/reference/components/background-video-skin.md): The background preset's chrome-less skin for ambient video

### Media

API reference for media components that handle streaming protocols and playback.

- [audio](https://videojs.org/docs/framework/html/reference/components/audio.md): Native audio playback that can provide media to a Video.js player
- [background-video](https://videojs.org/docs/framework/html/reference/components/background-video.md): Decorative background video element with automatic muting and looping
- [cloudflare-video](https://videojs.org/docs/framework/html/reference/components/cloudflare-video.md): Video component that plays Cloudflare Stream videos through the Stream player
- [dailymotion-video](https://videojs.org/docs/framework/html/reference/components/dailymotion-video.md): Video component that plays Dailymotion videos through a Dailymotion player configuration
- [dash-video](https://videojs.org/docs/framework/html/reference/components/dash-video.md): DASH video element powered by dash.js for adaptive bitrate streaming
- [hls-audio](https://videojs.org/docs/framework/html/reference/components/hls-audio.md): Audio-only HLS element that plays the audio rendition of an HLS stream
- [hls-background-video](https://videojs.org/docs/framework/html/reference/components/hls-background-video.md): HLS background video without controls, audio, captions, or adaptive quality
- [hls-video](https://videojs.org/docs/framework/html/reference/components/hls-video.md): Lightweight HLS video element with minimal bundle size
- [hlsjs-video](https://videojs.org/docs/framework/html/reference/components/hlsjs-video.md): HLS video element powered by hls.js for adaptive bitrate streaming
- [mixcloud-audio](https://videojs.org/docs/framework/html/reference/components/mixcloud-audio.md): Audio component that plays Mixcloud shows through the Mixcloud Widget
- [mux-audio](https://videojs.org/docs/framework/html/reference/components/mux-audio.md): Audio element for Mux-hosted HLS streams
- [mux-background-video](https://videojs.org/docs/framework/html/reference/components/mux-background-video.md): Mux-specific name for the HLS background video component
- [mux-video](https://videojs.org/docs/framework/html/reference/components/mux-video.md): Video element for Mux-hosted HLS streams
- [native-hls-video](https://videojs.org/docs/framework/html/reference/components/native-hls-video.md): HLS video element using the browser's built-in HLS support
- [playerjs-video](https://videojs.org/docs/framework/html/reference/components/playerjs-video.md): Video component that plays any embed implementing the player.js protocol, such as Mux Player, Gumlet, FrameRate, Livid, Bunny Stream, and Streamable
- [shaka-video](https://videojs.org/docs/framework/html/reference/components/shaka-video.md): Video element powered by Shaka Player for DASH, HLS, and progressive playback with DRM
- [soundcloud-audio](https://videojs.org/docs/framework/html/reference/components/soundcloud-audio.md): Audio component that plays SoundCloud tracks and sets through the SoundCloud Widget
- [spotify-audio](https://videojs.org/docs/framework/html/reference/components/spotify-audio.md): Audio component that plays Spotify tracks, episodes, playlists, and shows through the Spotify embed
- [tiktok-video](https://videojs.org/docs/framework/html/reference/components/tiktok-video.md): Video component that plays TikTok videos through the TikTok embed player
- [twitch-video](https://videojs.org/docs/framework/html/reference/components/twitch-video.md): Video component that plays Twitch videos and live channels through the Twitch embed player
- [video](https://videojs.org/docs/framework/html/reference/components/video.md): Native video playback that can provide media to a Video.js player
- [vimeo-video](https://videojs.org/docs/framework/html/reference/components/vimeo-video.md): Video component that plays Vimeo videos and live events through the Vimeo player
- [wistia-video](https://videojs.org/docs/framework/html/reference/components/wistia-video.md): Video component that plays Wistia-hosted videos through Wistia's web component
- [youtube-video](https://videojs.org/docs/framework/html/reference/components/youtube-video.md): Video component that plays YouTube videos and playlists through the YouTube IFrame player

### Extensions

API reference for extensions that connect external services to the player.

- [google-analytics](https://videojs.org/docs/framework/html/reference/components/google-analytics.md): Options for the Google Analytics 4 extension that tracks video engagement and playback events
- [google-cast](https://videojs.org/docs/framework/html/reference/components/google-cast.md): Options for the Google Cast extension that configures the receiver and load request
- [mux-data](https://videojs.org/docs/framework/html/reference/components/mux-data.md): Options for the Mux Data extension that monitors playback quality

### Buttons

API reference for the button components that trigger playback actions.

- [media-play-button](https://videojs.org/docs/framework/html/reference/components/play-button.md): Accessible play/pause button with keyboard support and customizable rendering
- [media-mute-button](https://videojs.org/docs/framework/html/reference/components/mute-button.md): Accessible mute/unmute button with keyboard support and volume state reflection
- [media-seek-button](https://videojs.org/docs/framework/html/reference/components/seek-button.md): Accessible seek button for skipping forward or backward by a configurable number of seconds
- [media-fullscreen-button](https://videojs.org/docs/framework/html/reference/components/fullscreen-button.md): Accessible fullscreen toggle button with keyboard support and state reflection
- [media-pip-button](https://videojs.org/docs/framework/html/reference/components/pip-button.md): Accessible picture-in-picture toggle button with keyboard support and state reflection
- [media-captions-button](https://videojs.org/docs/framework/html/reference/components/captions-button.md): Accessible captions toggle button with availability detection and state reflection
- [media-playback-rate-button](https://videojs.org/docs/framework/html/reference/components/playback-rate-button.md): A button that cycles through playback speed rates
- [media-live-button](https://videojs.org/docs/framework/html/reference/components/live-button.md): Accessible live indicator button that seeks to the live edge when pressed
- [media-airplay-button](https://videojs.org/docs/framework/html/reference/components/airplay-button.md): Accessible AirPlay toggle button that opens the WebKit playback target picker and reflects session state
- [media-cast-button](https://videojs.org/docs/framework/html/reference/components/cast-button.md): Accessible Cast toggle button with state reflection and keyboard support

### Sliders

API reference for the slider components that scrub time and adjust volume.

- [media-slider](https://videojs.org/docs/framework/html/reference/components/slider.md): A composable slider component with track, fill, thumb, preview, and value parts
- [media-time-slider](https://videojs.org/docs/framework/html/reference/components/time-slider.md): A slider component for seeking through media playback time
- [media-volume-slider](https://videojs.org/docs/framework/html/reference/components/volume-slider.md): A slider component for controlling media playback volume

### Menus

API reference for menus, popovers, and the radio groups that pick tracks, quality, and speed.

- [media-menu](https://videojs.org/docs/framework/html/reference/components/menu.md): A composable menu component for settings, option selection, and actions
- [media-popover](https://videojs.org/docs/framework/html/reference/components/popover.md): A popover component for displaying contextual content anchored to a trigger
- [media-volume-popover](https://videojs.org/docs/framework/html/reference/components/volume-popover.md): A volume-aware popover that keeps mute available when volume level controls are unavailable
- [media-audio-track-radio-group](https://videojs.org/docs/framework/html/reference/components/audio-track-radio-group.md): A menu radio group for selecting an audio track
- [media-captions-radio-group](https://videojs.org/docs/framework/html/reference/components/captions-radio-group.md): A menu radio group for selecting caption and subtitle tracks
- [media-playback-rate-radio-group](https://videojs.org/docs/framework/html/reference/components/playback-rate-radio-group.md): A menu radio group for selecting playback speed
- [media-quality-radio-group](https://videojs.org/docs/framework/html/reference/components/quality-radio-group.md): A menu radio group for selecting video quality

### Display

API reference for components that display player state, media metadata, and previews.

- [media-time](https://videojs.org/docs/framework/html/reference/components/time.md): Time display components for showing current time, duration, and remaining time in a video player
- [media-title](https://videojs.org/docs/framework/html/reference/components/title.md): Displays the resolved content title for the current media
- [media-poster](https://videojs.org/docs/framework/html/reference/components/poster.md): Poster image component that displays a thumbnail until video playback starts
- [media-thumbnail](https://videojs.org/docs/framework/html/reference/components/thumbnail.md): Time-based thumbnail preview component for timeline scrubbing and hover previews
- [media-tooltip](https://videojs.org/docs/framework/html/reference/components/tooltip.md): A tooltip component for displaying contextual labels on hover and focus
- [media-buffering-indicator](https://videojs.org/docs/framework/html/reference/components/buffering-indicator.md): Loading indicator that displays when the video player is buffering or waiting for data
- [media-seek-indicator](https://videojs.org/docs/framework/html/reference/components/seek-indicator.md): A temporary visual indicator for keyboard and gesture seeking
- [media-status-indicator](https://videojs.org/docs/framework/html/reference/components/status-indicator.md): Display temporary visual feedback for keyboard and gesture actions
- [media-volume-indicator](https://videojs.org/docs/framework/html/reference/components/volume-indicator.md): Display temporary visual feedback for keyboard and gesture volume actions

### Dialogs

API reference for modal dialogs, alerts, and playback error surfaces.

- [media-dialog](https://videojs.org/docs/framework/html/reference/components/dialog.md): A modal dialog for application content, including players opened from a thumbnail
- [media-alert-dialog](https://videojs.org/docs/framework/html/reference/components/alert-dialog.md): A modal alert dialog for urgent messages that require acknowledgement
- [media-error-dialog](https://videojs.org/docs/framework/html/reference/components/error-dialog.md): An alert dialog that presents and dismisses playback errors

### Behavior

API reference for the non-visual components that add gestures, hotkeys, and announcements.

- [media-gesture](https://videojs.org/docs/framework/html/reference/components/gesture.md): Map tap and double-tap gestures to player actions
- [media-hotkey](https://videojs.org/docs/framework/html/reference/components/hotkey.md): Register a keyboard shortcut that invokes a player action
- [media-status-announcer](https://videojs.org/docs/framework/html/reference/components/status-announcer.md): Announce player state changes through a persistent status live region

### Icons

API reference for the icon sets the skins use, available for your own controls.

- [Icons](https://videojs.org/docs/framework/html/reference/components/icons.md): The SVG icon sets used by the packaged skins, as React components, SVG strings, and the media-icon element

## API

API reference for the player factory, presets, store controllers, features, translation tools, and utilities.

Section index: [reference/api/llms.txt](https://videojs.org/docs/framework/html/reference/api/llms.txt). This section in one file (about 50k tokens): https://videojs.org/docs/framework/html/reference/api/llms-full.txt

### Player

API reference for creating a player and reaching it and its container from your own code.

- [createPlayer](https://videojs.org/docs/framework/html/reference/api/html-create-player.md): Factory function that creates a typed player element and controller for HTML custom elements
- [PlayerController](https://videojs.org/docs/framework/html/reference/api/player-controller.md): Reactive controller for accessing player store state in HTML custom elements
- [UIElement](https://videojs.org/docs/framework/html/reference/api/ui-element.md): Base class for custom elements that read player state through reactive controllers
- [Media capability guards](https://videojs.org/docs/framework/html/reference/api/media-capabilities.md): Type guards that narrow a Media object to the capabilities it supports

### Presets

API reference for the presets: each bundles a player, feature bundle, skins, and media for one use case.

- [Video preset](https://videojs.org/docs/framework/html/reference/api/preset-video.md): The general-purpose video preset — a player, feature bundle, skins, and media for on-demand video
- [Audio preset](https://videojs.org/docs/framework/html/reference/api/preset-audio.md): The audio-only preset — a player, feature bundle, skins, and media for on-demand audio
- [Live video preset](https://videojs.org/docs/framework/html/reference/api/preset-live-video.md): The live video preset — a player, feature bundle, skins, and media for live video streams
- [Live audio preset](https://videojs.org/docs/framework/html/reference/api/preset-live-audio.md): The live audio preset — a player, feature bundle, skins, and media for live audio streams
- [Background preset](https://videojs.org/docs/framework/html/reference/api/preset-background.md): The background video preset — a player, feature bundle, skin, and media for ambient video with no controls

### Store

API reference for reading and subscribing to player state: selectors and the store controllers.

- [Player store](https://videojs.org/docs/framework/html/reference/api/player-store.md): Every state field and action on the player store, grouped by the feature that adds it
- [createSelector](https://videojs.org/docs/framework/html/reference/api/create-selector.md): Create a type-safe selector for a store slice's state
- [StoreController](https://videojs.org/docs/framework/html/reference/api/store-controller.md): Reactive controller for subscribing to store state in HTML custom elements
- [SnapshotController](https://videojs.org/docs/framework/html/reference/api/snapshot-controller.md): Reactive controller for subscribing to a State container in HTML custom elements
- [SubscriptionController](https://videojs.org/docs/framework/html/reference/api/subscription-controller.md): Reactive controller that resolves a store and manages a derived subscription

### Features

API reference for the feature modules passed to createPlayer, which provide player capabilities and state.

- [Buffer](https://videojs.org/docs/framework/html/reference/api/feature-buffer.md): Buffered and seekable time range state for the player store
- [Controls](https://videojs.org/docs/framework/html/reference/api/feature-controls.md): User activity and controls visibility state for the player store
- [Error](https://videojs.org/docs/framework/html/reference/api/feature-error.md): Media error state and actions for the player store
- [Fullscreen](https://videojs.org/docs/framework/html/reference/api/feature-fullscreen.md): Fullscreen state and actions for the player store
- [Live](https://videojs.org/docs/framework/html/reference/api/feature-live.md): Live edge state for the player store
- [Metadata](https://videojs.org/docs/framework/html/reference/api/feature-metadata.md): Resolved title and poster values for the player store
- [Orientation lock](https://videojs.org/docs/framework/html/reference/api/feature-orientation-lock.md): Screen orientation locking while fullscreen is active
- [Picture-in-picture](https://videojs.org/docs/framework/html/reference/api/feature-pip.md): Picture-in-picture state and actions for the player store
- [Playback](https://videojs.org/docs/framework/html/reference/api/feature-playback.md): Play/pause state and actions for the player store
- [Playback rate](https://videojs.org/docs/framework/html/reference/api/feature-playback-rate.md): Playback speed state and actions for the player store
- [Quality](https://videojs.org/docs/framework/html/reference/api/feature-quality.md): Video rendition state and actions for the player store
- [Audio track](https://videojs.org/docs/framework/html/reference/api/feature-audio-track.md): Audio track state and actions for the player store
- [Remote Playback](https://videojs.org/docs/framework/html/reference/api/feature-remote-playback.md): Remote playback state and actions for the player store
- [Source](https://videojs.org/docs/framework/html/reference/api/feature-source.md): Media source state and actions for the player store
- [Stream type](https://videojs.org/docs/framework/html/reference/api/feature-stream-type.md): Stream delivery type (live / on-demand) state for the player store
- [Text tracks](https://videojs.org/docs/framework/html/reference/api/feature-text-tracks.md): Subtitles, captions, and chapter track state for the player store
- [Time](https://videojs.org/docs/framework/html/reference/api/feature-time.md): Playback position and duration state for the player store
- [Volume](https://videojs.org/docs/framework/html/reference/api/feature-volume.md): Volume level and mute state for the player store

### i18n

API reference for translating the player: the i18n elements, controller, and the phrase registry.

- [createI18n](https://videojs.org/docs/framework/html/reference/api/create-i18n.md): Factory that creates framework i18n helpers with custom loading options
- [media-i18n](https://videojs.org/docs/framework/html/reference/api/media-i18n.md): HTML custom element that resolves locale and supplies translations to descendants
- [media-text](https://videojs.org/docs/framework/html/reference/api/media-text.md): HTML custom element that renders a translated string by semantic key
- [Translation phrases](https://videojs.org/docs/framework/html/reference/api/translation-phrases.md): Semantic i18n keys, their English defaults, and the player UI that uses them
- [registerI18n](https://videojs.org/docs/framework/html/reference/api/register-i18n.md): Register or merge translation strings for a BCP 47 locale tag in the global i18n registry
- [getI18nTranslations](https://videojs.org/docs/framework/html/reference/api/get-i18n-translations.md): Read the merged translation map for a locale using BCP 47 parent-chain fallback
- [hasRegisteredLocale](https://videojs.org/docs/framework/html/reference/api/has-registered-locale.md): Check whether an exact locale tag exists in the global i18n registry
- [onI18nRegistryChange](https://videojs.org/docs/framework/html/reference/api/on-i18n-registry-change.md): Subscribe to global i18n registry mutations
- [createTranslator](https://videojs.org/docs/framework/html/reference/api/create-translator.md): Build a typed translator from a resolved translation map
- [translateText](https://videojs.org/docs/framework/html/reference/api/translate-text.md): Translate a text descriptor, or fall back to its English default
- [resolveTranslation](https://videojs.org/docs/framework/html/reference/api/resolve-translation.md): Translate a key with the params its English default requires
- [isText](https://videojs.org/docs/framework/html/reference/api/is-text.md): Check whether a value is a text descriptor
- [loadLocale](https://videojs.org/docs/framework/html/reference/api/load-locale.md): Lazy-load the built-in translation pack for a locale
- [getLocaleKey](https://videojs.org/docs/framework/html/reference/api/get-locale-key.md): Normalize a locale tag to the key the i18n registry stores it under
- [findLocaleKeys](https://videojs.org/docs/framework/html/reference/api/find-locale-keys.md): List the locale tags a lookup falls back through, most specific first
- [I18nController](https://videojs.org/docs/framework/html/reference/api/i18n-controller.md): Reactive controller for consuming translator and locale values from an HTML i18n context

### Utils

Lower-level building blocks: adapter and MIME type resolution, and the keyboard shortcut controller for custom components.

- [resolveAdapterType](https://videojs.org/docs/framework/html/reference/api/resolve-adapter-type.md): Resolve which type of adapter plays a source URL, from its host, MIME type, or file extension
- [resolveMimeType](https://videojs.org/docs/framework/html/reference/api/resolve-mime-type.md): Resolve a source's MIME type from its file extension
- [AriaKeyShortcutsController](https://videojs.org/docs/framework/html/reference/api/aria-key-shortcuts-controller.md): Reactive controller that exposes registered hotkey shortcut metadata

### Error codes

Reference for codes thrown when Video.js 8 APIs are used with the Video.js 10 package.

- [Error Codes](https://videojs.org/docs/framework/html/reference/api/error-codes.md): Error codes emitted by the video.js package and how to resolve them
- [VJS8_LEGACY_INIT](https://videojs.org/docs/framework/html/reference/api/vjs8-legacy-init.md): Legacy Video.js 8 player initialization error
- [VJS8_LEGACY_PLUGIN](https://videojs.org/docs/framework/html/reference/api/vjs8-legacy-plugin.md): Legacy Video.js 8 plugin registration error
- [VJS8_LEGACY_COMPONENT](https://videojs.org/docs/framework/html/reference/api/vjs8-legacy-component.md): Legacy Video.js 8 component registration error
- [VJS8_LEGACY_GET_PLAYER](https://videojs.org/docs/framework/html/reference/api/vjs8-legacy-get-player.md): Legacy Video.js 8 player lookup error
- [VJS8_LEGACY_OPTIONS](https://videojs.org/docs/framework/html/reference/api/vjs8-legacy-options.md): Legacy Video.js 8 global options error

---

All documentation: https://videojs.org/llms.txt
