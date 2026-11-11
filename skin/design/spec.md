# Kerf design spec

Source of truth: the approved design board, `../board/index.html` (Driss's Go, 2026-11-11). This file records the
rules the build follows and every decision the board does not show.

## Idea
The picture is cut to make room for the controls. Controls live in a notch of the player's own frame, a solid
surface (dark by default, `data-surface="light"` for light), so contrast never depends on the footage. Everything that
opens rises out of the frame from its control; transient feedback hangs from the top edge.

## Geometry
- Outer radius = inner radius + frame: 20 = 14 + 6. `--media-border-radius` sets the outer; the inner follows.
- Band: 44 px targets plus a 6 px gap above them (50 px). Buttons radius 14 (concentric with the outer corner).
- Notch fillets 10 px; the time tab's top corner shares that radius.
- Seek: 6 px track (8 px while pointing), chapters separated by 3 px kerfs, a 4 x 20 px blade with a 3 px cut.

## Layout and order
Time tab (current / duration), then the band: play, seek, mute (volume popover), captions, settings, fullscreen.
Below 560 px of player width the captions button hides; captions stay in the settings menu.

## Poster
Before the first play the band and the time tab fold away while the user is idle; hover, a tap or keyboard focus
inside the player brings them back. A paused player that has played keeps its controls. Opt out with
`data-poster-controls="show"` on the skin root.

## Menus and popups
Settings sits flush right with a square corner and the picture's corner redrawn above it. Speed offers six rates
(0.5, 0.75, 1, 1.25, 1.5, 2) as a 3 x 2 grid of chips. Tooltips, volume and the preview are tabs with both fillets.

## Motion
Rise 200 ms cubic-bezier(.2, .8, .2, 1), revealed from the notch's base (a clip-path, never a scale), so nothing
passes the frame; sink 120 ms ease-in back into the band; status notches retract into the top edge inside the picture's
clip; band 240 ms. Transitions only, so an interrupted popup turns back from where it is. Reduced motion: instant.

## Derived (not drawn on the board)
- Volume popover shows no percentage; the volume indicator in the top notch reports it on key presses.
- The error dialog keeps Video.js's single close button (styled with the accent); no custom retry.
- Captions: Chromium draws the cue box with the 10 px radius; other engines keep the square cue background.
- Hover on the play button and the ready tile takes the accent; other buttons take a 9 % ink wash.
- Font: `--media-font-family`, falling back to Inter, then the system UI font.
