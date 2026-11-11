import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1440, 'height': 900}, color_scheme='dark', device_scale_factor=3)
        await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(1800)
        k = pg.locator('#hero-player .kd'); await k.scroll_into_view_if_needed(); await pg.wait_for_timeout(500)
        bb = await k.bounding_box(); await pg.screenshot(path=f'{OUT}/drawn-bl.png', clip={'x': bb['x'], 'y': bb['y'] + bb['height'] - 60, 'width': 60, 'height': 60})
        await pg.close()
        pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme='dark', device_scale_factor=3)
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(2500)
        bb = await pg.locator('.kerf').bounding_box(); await pg.mouse.move(bb['x'] + bb['width'] / 2, bb['y'] + bb['height'] / 2); await pg.wait_for_timeout(600)
        await pg.screenshot(path=f'{OUT}/live-bl.png', clip={'x': bb['x'], 'y': bb['y'] + bb['height'] - 60, 'width': 60, 'height': 60})
        await pg.screenshot(path=f'{OUT}/live-br.png', clip={'x': bb['x'] + bb['width'] - 60, 'y': bb['y'] + bb['height'] - 60, 'width': 60, 'height': 60})
        await b.close()
asyncio.run(main())
