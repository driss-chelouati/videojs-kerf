import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(2500)
        await pg.evaluate("(() => { const m = document.querySelector('mux-video'); m.muted = true; m.currentTime = 12.4; })()"); await pg.wait_for_timeout(1200)
        k = await pg.locator('.kerf').bounding_box(); clip = {'x': k['x'] - 30, 'y': k['y'] - 30, 'width': k['width'] + 60, 'height': 160}
        await pg.locator('.kerf').focus(); await pg.keyboard.press('l')
        for i, t in enumerate([40, 120, 600, 1300, 1400, 1520]):
            await pg.wait_for_timeout(t - ([0, 40, 120, 600, 1300, 1400][i]))
            await pg.screenshot(path=f'{OUT}/n{i}.png', clip=clip)
        await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 3); await pg.locator('.kerf-gear').click(); await pg.wait_for_timeout(80)
        bc = {'x': k['x'] + k['width'] - 320, 'y': k['y'] + k['height'] - 260, 'width': 340, 'height': 280}
        await pg.screenshot(path=f'{OUT}/m0.png', clip=bc); await pg.wait_for_timeout(400); await pg.screenshot(path=f'{OUT}/m1.png', clip=bc)
        await b.close()
asyncio.run(main())
