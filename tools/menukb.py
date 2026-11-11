import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1280, 'height': 800})
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(2500)
        k = await pg.locator('.kerf').bounding_box(); await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 2); await pg.wait_for_timeout(600)
        ring = "getComputedStyle(document.querySelector('.kerf-menu-item')).boxShadow"
        await pg.locator('.kerf-gear').click(); await pg.wait_for_timeout(400); print('mouse open ring:', await pg.evaluate(ring))
        await pg.keyboard.press('Escape'); await pg.wait_for_timeout(300)
        await pg.locator('.kerf-gear').focus(); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(400); print('keyboard open ring:', await pg.evaluate(ring))
        await b.close()
asyncio.run(main())
