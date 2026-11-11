import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(2500)
        k = await pg.locator('.kerf').bounding_box()
        await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 2); await pg.wait_for_timeout(400)
        g = await pg.locator('.kerf-gear').bounding_box(); await pg.mouse.click(g['x'] + 22, g['y'] + 22); await pg.wait_for_timeout(500)
        clip = {'x': k['x'] + k['width'] - 300, 'y': k['y'] + k['height'] - 230, 'width': 320, 'height': 250}
        rect = "(() => { const m = document.querySelector('.kerf-menu'); const r = m.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.right), Math.round(r.width), m.hasAttribute('data-ending-style'), m.getAttribute('style').match(/(left|translate|position-anchor)[^;]*/g)] })()"
        await pg.mouse.click(k['x'] + k['width'] / 2, k['y'] + k['height'] / 3)
        for i in range(6):
            print(i, await pg.evaluate(rect)); await pg.screenshot(path=f'{OUT}/c{i}.png', clip=clip); await pg.wait_for_timeout(15)
        await b.close()
asyncio.run(main())
