import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
AXE = 'https://cdn.jsdelivr.net/npm/axe-core@4.10.2/axe.min.js'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w in [1440, 1024, 390]:
            pg = await b.new_page(viewport={'width': w, 'height': 900}, color_scheme='dark')
            await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(1800)
            el = pg.locator('section[aria-labelledby="home-h"]'); await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(900)
            await el.screenshot(path=f'{OUT}/bento-{w}.png')
            if w == 1440:
                await pg.add_script_tag(url=AXE)
                print('axe:', await pg.evaluate("async () => (await axe.run(document.querySelector('section[aria-labelledby=\"home-h\"]'), {resultTypes: ['violations']})).violations.map(v => v.id + ' ' + v.nodes.slice(0,2).map(n => n.target.join(' ')).join(' | '))"))
            print(w, 'x-over', await pg.evaluate('document.documentElement.scrollWidth - innerWidth'))
            await pg.close()
        await b.close()
asyncio.run(main())
