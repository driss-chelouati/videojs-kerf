import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for scale, suffix in [(1, ''), (2, '@2x')]:
            pg = await b.new_page(viewport={'width': 1600, 'height': 1200}, color_scheme='dark', device_scale_factor=scale)
            await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(1800)
            await pg.evaluate("""() => { const s = document.querySelector('section[aria-labelledby="home-h"]'); document.querySelectorAll('main > *, .announce, .topbar, .foot, .kerfline').forEach(e => { if (e !== s) e.style.visibility = 'hidden'; }); const h = s.getBoundingClientRect().height; s.style.zoom = Math.min(1, 1088 / h); }""")
            await pg.wait_for_timeout(300)
            await pg.evaluate("""() => { const s = document.querySelector('section[aria-labelledby="home-h"]'); const r = s.getBoundingClientRect(); scrollBy(0, r.top + r.height / 2 - innerHeight / 2); }""")
            await pg.wait_for_timeout(900)
            await pg.screenshot(path=f'{OUT}/kerf-at-home-bento-1600x1200{suffix}.png')
            await pg.close()
        await b.close()
asyncio.run(main())
