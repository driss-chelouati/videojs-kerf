"""Audit pass for the Kerf skin in the workbench preview: states the first pass did not cover, keyboard, preferences.

usage: audit.py <out_dir>   (run through tools/run-heavy.sh)
"""
import asyncio, sys, os, json
from playwright.async_api import async_playwright

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
BASE = 'http://127.0.0.1:5191/preview.html'


async def open_player(b, w=960, search='', hash_extra='', **ctx):
    c = await b.new_context(viewport={'width': w + 160, 'height': 900}, **ctx)
    pg = await c.new_page()
    logs = []
    pg.on('console', lambda m: logs.append(f'{m.type}: {m.text}') if m.type in ('error', 'warning') else None)
    pg.on('pageerror', lambda e: logs.append(f'pageerror: {e}'))
    await pg.goto(f'{BASE}{search}#width={w}{hash_extra}')
    await pg.wait_for_selector('.kerf')
    await pg.wait_for_timeout(1200)
    await pg.locator('video').evaluate('v => { v.muted = true; v.currentTime = 21.4; }')
    await pg.wait_for_timeout(600)
    return c, pg, logs


async def shot(pg, name):
    k = pg.locator('.kerf')
    bb = await k.bounding_box()
    await pg.screenshot(path=f'{OUT}/{name}.png', clip={'x': bb['x'] - 24, 'y': max(0, bb['y'] - 24), 'width': bb['width'] + 48, 'height': bb['height'] + 48})


async def hover_center(pg):
    bb = await pg.locator('.kerf').bounding_box()
    await pg.mouse.move(bb['x'] + bb['width'] / 2, bb['y'] + bb['height'] / 3)


async def main():
    report = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])

        # 1. tooltips: play (edge), fullscreen (right edge), keyboard-opened
        c, pg, logs = await open_player(b)
        await hover_center(pg)
        fb = await pg.locator('.kerf-fullscreen').bounding_box()
        await pg.mouse.move(fb['x'] + 22, fb['y'] + 22)
        await pg.wait_for_timeout(900)
        await shot(pg, 'a1-tooltip-fullscreen')
        pb = await pg.locator('.kerf-play').bounding_box()
        await pg.mouse.move(pb['x'] + 22, pb['y'] + 22)
        await pg.wait_for_timeout(900)
        await shot(pg, 'a2-tooltip-play-hover')

        # 2. keyboard: tab order and focus
        await pg.mouse.move(2, 2)
        await pg.evaluate('document.activeElement && document.activeElement.blur()')
        order = []
        await pg.locator('body').focus()
        for i in range(10):
            await pg.keyboard.press('Tab')
            await pg.wait_for_timeout(120)
            order.append(await pg.evaluate('''() => { const a = document.activeElement; return a ? (a.className || a.tagName) + ' | ' + (a.getAttribute('aria-label') || a.textContent.trim().slice(0, 30)) : null }'''))
        report['tab_order'] = order
        # focus the gear, open with Enter, Escape returns focus
        await pg.locator('.kerf-gear').focus()
        await pg.wait_for_timeout(200)
        await shot(pg, 'a3-focus-gear')
        await pg.keyboard.press('Enter')
        await pg.wait_for_timeout(400)
        await pg.keyboard.press('ArrowDown')
        await pg.wait_for_timeout(200)
        await shot(pg, 'a4-menu-keyboard')
        await pg.keyboard.press('Escape')
        await pg.wait_for_timeout(400)
        report['focus_after_escape'] = await pg.evaluate('document.activeElement.className')
        # announcer text after pressing m
        await pg.keyboard.press('m')
        await pg.wait_for_timeout(400)
        report['announcer'] = await pg.evaluate("document.querySelector('media-status-announcer')?.textContent")
        await shot(pg, 'a5-volume-indicator')
        report['logs_1'] = logs
        await c.close()

        # 3. error: a missing source
        c, pg, logs = await open_player(b)
        await pg.locator('video').evaluate("v => { v.src = './media/missing.mp4'; v.load(); }")
        await pg.wait_for_timeout(1500)
        await shot(pg, 'b1-error')
        await c.close()

        # 4. light surface, cobalt accent
        c, pg, logs = await open_player(b)
        await pg.evaluate("""() => { const k = document.querySelector('.kerf'); k.dataset.surface = 'light'; k.style.setProperty('--media-accent-color', '#3155ff'); }""")
        await hover_center(pg)
        await pg.wait_for_timeout(400)
        await shot(pg, 'c1-light')
        sb = await pg.locator('.kerf-seek').bounding_box()
        await pg.mouse.move(sb['x'] + sb['width'] * 0.3, sb['y'] + 22)
        await pg.wait_for_timeout(500)
        await shot(pg, 'c2-light-scrub')
        await c.close()

        # 5. reduced motion + forced colours
        c, pg, logs = await open_player(b, reduced_motion='reduce', forced_colors='active')
        await hover_center(pg)
        await pg.locator('.kerf-gear').click()
        await pg.wait_for_timeout(300)
        await shot(pg, 'd1-forced-colors-menu')
        await c.close()

        # 6. fullscreen
        c, pg, logs = await open_player(b)
        await hover_center(pg)
        await pg.locator('.kerf-fullscreen').click()
        await pg.wait_for_timeout(900)
        await pg.screenshot(path=f'{OUT}/e1-fullscreen.png')
        report['fullscreen'] = await pg.evaluate('!!document.fullscreenElement && document.fullscreenElement.className')
        await c.close()

        # 7. buffering: slow the network so the film stalls
        c, pg, logs = await open_player(b)
        cdp = await c.new_cdp_session(pg)
        await cdp.send('Network.enable')
        await cdp.send('Network.emulateNetworkConditions', {'offline': False, 'latency': 400, 'downloadThroughput': 20000, 'uploadThroughput': 20000})
        await pg.locator('video').evaluate("v => { v.src = './media/sparvek-169.mp4?nocache=' + Date.now(); v.currentTime = 30; v.play().catch(()=>{}); }")
        await pg.wait_for_timeout(2500)
        await shot(pg, 'f1-buffering')
        await c.close()

        # 8. RTL + German labels at tablet width
        c, pg, logs = await open_player(b, w=768, hash_extra='&dir=rtl&locale=ar')
        await hover_center(pg)
        await pg.wait_for_timeout(300)
        await shot(pg, 'g1-rtl-ar')
        await pg.locator('.kerf-gear').click()
        await pg.wait_for_timeout(400)
        await shot(pg, 'g2-rtl-menu')
        await c.close()
        c, pg, logs = await open_player(b, w=768, hash_extra='&locale=de')
        await hover_center(pg)
        await pg.locator('.kerf-gear').click()
        await pg.wait_for_timeout(400)
        await shot(pg, 'g3-de-menu')
        await c.close()

        await b.close()
    print(json.dumps(report, indent=1))

asyncio.run(main())
