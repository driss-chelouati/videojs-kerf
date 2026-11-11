import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme='light', device_scale_factor=2)
        await pg.goto('http://127.0.0.1:5191/index.html#surface=light'); await pg.wait_for_timeout(2500)
        k = await pg.locator('.kerf').bounding_box()
        for name, x, y in [('tl', k['x'] - 6, k['y'] - 6), ('br', k['x'] + k['width'] - 70, k['y'] + k['height'] - 70)]:
            await pg.screenshot(path=f'{OUT}/corner-{name}.png', clip={'x': x, 'y': y, 'width': 76, 'height': 76})
        await pg.screenshot(path=f'{OUT}/light.png')
        await b.close()
asyncio.run(main())
