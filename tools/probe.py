import asyncio, sys, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1120, 'height': 900})
        await pg.goto('http://127.0.0.1:5191/preview.html#width=960')
        await pg.wait_for_selector('.kerf'); await pg.wait_for_timeout(1200)
        await pg.locator('.kerf-gear').click(); await pg.wait_for_timeout(500)
        r = await pg.evaluate('''() => { const m = document.querySelector('.kerf-menu'); const cs = getComputedStyle(m);
          const g = document.querySelector('.kerf-gear').getBoundingClientRect(); const k = document.querySelector('.kerf-ui').getBoundingClientRect();
          const pages = [...m.querySelectorAll('.kerf-menu-page')].map(p => ({r: p.getBoundingClientRect().toJSON(), attrs: [...p.attributes].map(a=>a.name+'='+a.value).join(' ')}));
          return {rect: m.getBoundingClientRect().toJSON(), style: m.getAttribute('style'), attrs: [...m.attributes].map(a=>a.name).join(' '), w: cs.width, pos: cs.position, popover: m.matches(':popover-open'), gear: g.toJSON(), ui: k.toJSON(), pages}; }''')
        print(json.dumps(r, indent=1))
        await b.close()
asyncio.run(main())
