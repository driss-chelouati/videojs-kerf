import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']); pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.mouse.move(2, 2); await pg.wait_for_timeout(3500)
        k = await pg.locator('.kerf').bounding_box(); clip = {'x': k['x'] - 20, 'y': k['y'] - 20, 'width': k['width'] + 40, 'height': k['height'] + 40}
        band = lambda: pg.evaluate("getComputedStyle(document.querySelector('.kerf-band')).transform")
        attrs = lambda: pg.evaluate("[...document.querySelector('.kerf-ui').attributes].map(a => a.name).filter(n => n.startsWith('data')).join(' ')")
        print('idle poster:', await band(), '|', await attrs()); await pg.screenshot(path=f'{OUT}/f1-idle.png', clip=clip)
        await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 2); await pg.mouse.move(k['x'] + k['width'] / 2 + 20, k['y'] + k['height'] / 2); await pg.wait_for_timeout(500)
        print('hover poster:', await band(), '|', await attrs()); await pg.screenshot(path=f'{OUT}/f2-hover.png', clip=clip)
        await pg.mouse.move(2, 2); await pg.wait_for_timeout(3500); print('after idle:', await band())
        await pg.keyboard.press('Tab'); await pg.keyboard.press('Tab'); await pg.keyboard.press('Tab'); await pg.keyboard.press('Tab'); await pg.wait_for_timeout(400)
        print('tab focus:', await pg.evaluate("document.activeElement.className"), await band())
        await pg.evaluate("(() => { const m = document.querySelector('mux-video'); m.muted = true; return m.play() })()"); await pg.wait_for_timeout(1200)
        await pg.evaluate("document.querySelector('mux-video').pause()"); await pg.evaluate("document.activeElement.blur()"); await pg.mouse.move(2, 2); await pg.wait_for_timeout(3500)
        print('paused after play, idle:', await band()); await pg.screenshot(path=f'{OUT}/f3-paused.png', clip=clip)
        await b.close()
asyncio.run(main())
