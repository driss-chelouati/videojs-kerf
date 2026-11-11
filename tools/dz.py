import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1440, 'height': 900}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(2000)
        for sel, name in [('#scrub', 'scrub'), ('#states .cell:nth-child(6)', 'seek'), ('#phones .cell:nth-child(2)', 'phone')]:
            el = pg.locator(sel); await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(900)
            await el.screenshot(path=f'{OUT}/{name}.png')
        await b.close()
asyncio.run(main())
