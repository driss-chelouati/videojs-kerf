import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for d, loc in [('ltr', 'en'), ('rtl', 'ar')]:
            pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme='dark', device_scale_factor=2)
            await pg.goto(f'http://127.0.0.1:5191/preview.html#width=960&dir={d}&locale={loc}'); await pg.wait_for_timeout(2500)
            await pg.evaluate("document.querySelector('.kerf').style.cssText += ';--kerf-rise: 1600ms; --kerf-sink: 1600ms'")
            k = await pg.locator('.kerf').bounding_box(); await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 2); await pg.wait_for_timeout(600)
            g = await pg.locator('.kerf-gear').bounding_box(); await pg.mouse.click(g['x'] + 22, g['y'] + 22); await pg.wait_for_timeout(1900)
            r = await pg.evaluate("(() => { const m = document.querySelector('.kerf-menu').getBoundingClientRect(), u = document.querySelector('.kerf-ui').getBoundingClientRect(), p = document.querySelector('.kerf-menu-page').getBoundingClientRect(); return {menu: [m.left, m.right], ui: [u.left, u.right], page: [p.left, p.right]} })()")
            print(d, r)
            x = k['x'] + k['width'] - 300 if d == 'ltr' else k['x'] - 10
            clip = {'x': x, 'y': k['y'] + k['height'] - 230, 'width': 310, 'height': 240}
            await pg.screenshot(path=f'{OUT}/{d}-open.png', clip=clip)
            await pg.keyboard.press('Escape')
            for i in range(3):
                await pg.wait_for_timeout(400); await pg.screenshot(path=f'{OUT}/{d}-c{i}.png', clip=clip)
            await pg.close()
        await b.close()
asyncio.run(main())
