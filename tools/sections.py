import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
AXE = 'https://cdn.jsdelivr.net/npm/axe-core@4.10.2/axe.min.js'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1440, 'height': 900}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(2000)
        H = await pg.evaluate('document.documentElement.scrollHeight')
        for y in range(0, H, 600):
            await pg.evaluate(f'scrollTo(0, {y})'); await pg.wait_for_timeout(40)
        for host in ['course', 'stream', 'notes']:
            await pg.locator(f'label:has(input[value="{host}"])').click(); await pg.wait_for_timeout(700)
            await pg.locator('.hosts').screenshot(path=f'{OUT}/host-{host}.png')
        el = pg.locator('.access'); await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(500); await el.screenshot(path=f'{OUT}/access.png')
        el = pg.locator('.steps'); await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(500); await el.screenshot(path=f'{OUT}/install.png')
        await pg.add_script_tag(url=AXE)
        v = await pg.evaluate("async () => (await axe.run(document, {resultTypes: ['violations']})).violations.map(v => v.id + ': ' + v.nodes.slice(0,2).map(n => n.target.join(' ')).join(' | '))")
        print('axe design:', v or 'none')
        print('x-over', await pg.evaluate('document.documentElement.scrollWidth - innerWidth'))
        await pg.close()
        pg = await b.new_page(viewport={'width': 390, 'height': 844}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(2000)
        el = pg.locator('.hosts'); await el.scroll_into_view_if_needed(); await pg.wait_for_timeout(600); await el.screenshot(path=f'{OUT}/host-mobile.png')
        print('mobile x-over', await pg.evaluate('document.documentElement.scrollWidth - innerWidth'))
        await b.close()
asyncio.run(main())
