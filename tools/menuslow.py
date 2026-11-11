import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme='dark', device_scale_factor=2)
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(2500)
        await pg.evaluate("document.querySelector('.kerf').style.cssText += ';--kerf-rise: 1600ms; --kerf-sink: 1600ms'")
        k = await pg.locator('.kerf').bounding_box()
        await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 2); await pg.wait_for_timeout(300)
        clip = {'x': k['x'] + k['width'] - 300, 'y': k['y'] + k['height'] - 230, 'width': 310, 'height': 240}
        g = await pg.locator('.kerf-gear').bounding_box(); await pg.mouse.click(g['x'] + 22, g['y'] + 22)
        for i in range(5):
            await pg.wait_for_timeout(320); await pg.screenshot(path=f'{OUT}/o{i}.png', clip=clip)
        await pg.wait_for_timeout(300)
        await pg.mouse.click(k['x'] + k['width'] / 3, k['y'] + k['height'] / 3)
        for i in range(6):
            await pg.screenshot(path=f'{OUT}/c{i}.png', clip=clip); await pg.wait_for_timeout(260)
        await b.close()
asyncio.run(main())
