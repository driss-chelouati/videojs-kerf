"""Capture the live Kerf player in its key states from the workbench preview.

usage: states.py <out_dir> [width] [extra-hash]   (run through tools/run-heavy.sh)
"""
import asyncio, sys, os
from playwright.async_api import async_playwright

OUT = sys.argv[1]
W = int(sys.argv[2]) if len(sys.argv) > 2 else 960
EXTRA = sys.argv[3] if len(sys.argv) > 3 else ''
SEARCH = sys.argv[4] if len(sys.argv) > 4 else ''
URL = f'http://127.0.0.1:5191/preview.html{SEARCH}#width={W}{EXTRA}'
os.makedirs(OUT, exist_ok=True)


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        pg = await b.new_page(viewport={'width': W + 160, 'height': 900}, device_scale_factor=1)
        logs = []
        pg.on('console', lambda m: logs.append(f'{m.type}: {m.text}') if m.type in ('error', 'warning') else None)
        pg.on('pageerror', lambda e: logs.append(f'pageerror: {e}'))
        await pg.goto(URL)
        await pg.wait_for_selector('.kerf')
        await pg.wait_for_timeout(1500)
        k = pg.locator('.kerf')
        box = await k.bounding_box()

        async def shot(name):
            bb = await k.bounding_box()
            await pg.screenshot(path=f'{OUT}/{name}.png', clip={'x': bb['x'] - 24, 'y': max(0, bb['y'] - 24), 'width': bb['width'] + 48, 'height': bb['height'] + 48})

        await shot('01-ready')
        v = pg.locator('video')
        await v.evaluate('v => { v.muted = true; v.currentTime = 21.4; }')
        await pg.wait_for_timeout(800)
        await pg.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 3)
        await shot('02-paused-21')
        # scrub preview
        seek = pg.locator('.kerf-seek')
        sb = await seek.bounding_box()
        await pg.mouse.move(sb['x'] + sb['width'] * 0.6, sb['y'] + sb['height'] / 2)
        await pg.wait_for_timeout(500)
        await shot('03-scrub')
        # volume popover
        mb = await pg.locator('.kerf-mute').bounding_box()
        await pg.mouse.move(mb['x'] + 22, mb['y'] + 22)
        await pg.wait_for_timeout(700)
        await shot('04-volume')
        # settings menu
        await pg.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 3)
        await pg.wait_for_timeout(300)
        await pg.locator('.kerf-gear').click()
        await pg.wait_for_timeout(500)
        await shot('05-menu')
        await pg.keyboard.press('Enter')
        await pg.wait_for_timeout(500)
        await shot('06-menu-speed')
        await pg.keyboard.press('Escape')
        await pg.keyboard.press('Escape')
        await pg.wait_for_timeout(300)
        # keyboard focus on the blade, then a seek
        await pg.locator('.kerf-blade').focus()
        await pg.keyboard.press('ArrowRight')
        await pg.wait_for_timeout(250)
        await shot('07-focus-seek')
        # captions on, playing, then idle so the controls sink
        await pg.locator('.kerf-captions').click() if await pg.locator('.kerf-captions').is_visible() else None
        await v.evaluate('v => { v.currentTime = 20.5; v.play(); }')
        await pg.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 3)
        await pg.wait_for_timeout(600)
        await shot('08-playing-captions')
        await pg.mouse.move(5, 5)
        await pg.wait_for_timeout(3800)
        await shot('09-sunk')
        print('\n'.join(logs[:20]) or 'no console errors')
        await b.close()

asyncio.run(main())
