import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1280, 'height': 800})
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.mouse.move(2, 2); await pg.wait_for_timeout(3500)
        await pg.locator('.kerf-start').focus(); await pg.keyboard.press('Tab'); await pg.wait_for_timeout(400)
        print('keyboard focus on', await pg.evaluate("document.activeElement.className"), '-> band', await pg.evaluate("getComputedStyle(document.querySelector('.kerf-band')).transform"))
        await b.close()
asyncio.run(main())
