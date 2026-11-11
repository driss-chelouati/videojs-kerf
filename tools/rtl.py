import asyncio, sys, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); out = {}
        for d in ['rtl', 'ltr']:
            pg = await b.new_page(viewport={'width': 1000, 'height': 800})
            await pg.goto(f'http://127.0.0.1:5191/preview.html#width=768&dir={d}&locale={"ar" if d=="rtl" else "en"}')
            await pg.wait_for_selector('.kerf'); await pg.wait_for_timeout(1200)
            await pg.locator('.kerf-gear').click(); await pg.wait_for_timeout(500)
            out[d] = await pg.evaluate('''() => { const m = document.querySelector('.kerf-menu').getBoundingClientRect(), u = document.querySelector('.kerf-ui').getBoundingClientRect(); return {menuLeft: m.left, menuRight: m.right, uiLeft: u.left, uiRight: u.right}; }''')
            if d == 'rtl': await pg.screenshot(path=sys.argv[1])
            await pg.close()
        print(json.dumps(out)); await b.close()
asyncio.run(main())
