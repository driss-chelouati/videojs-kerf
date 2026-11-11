import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        for scheme in ['dark', 'light']:
            pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme=scheme)
            await pg.goto(f'http://127.0.0.1:5191/index.html#surface={scheme}'); await pg.wait_for_timeout(2500)
            await pg.evaluate("(() => { const m = document.querySelector('mux-video'); m.muted = true; m.currentTime = 21.4; })()"); await pg.wait_for_timeout(1500)
            k = await pg.locator('.kerf').bounding_box()
            clip = {'x': k['x'] - 20, 'y': k['y'] - 20, 'width': k['width'] + 40, 'height': k['height'] + 40}
            await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 3); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'{OUT}/{scheme}-paused.png', clip=clip)
            sb = await pg.locator('.kerf-seek').bounding_box(); await pg.mouse.move(sb['x'] + sb['width'] * 0.3, sb['y'] + 22); await pg.wait_for_timeout(700)
            await pg.screenshot(path=f'{OUT}/{scheme}-scrub.png', clip=clip)
            await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 3); await pg.locator('.kerf-gear').click(); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f'{OUT}/{scheme}-menu.png', clip=clip)
            await pg.keyboard.press('Escape'); await pg.evaluate("document.querySelector('mux-video').play()"); await pg.mouse.move(2, 2); await pg.wait_for_timeout(3800)
            await pg.screenshot(path=f'{OUT}/{scheme}-sunk.png', clip=clip)
            await pg.close()
        pg = await b.new_page(viewport={'width': 390, 'height': 844}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(2500)
        await pg.screenshot(path=f'{OUT}/mobile.png'); await b.close()
asyncio.run(main())
