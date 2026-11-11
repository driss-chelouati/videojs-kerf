import asyncio, sys, json
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); res = []
        for page in ['index', 'design']:
            for w, h in [(1440, 900), (1280, 720), (1024, 768), (768, 1024), (390, 844), (360, 640)]:
                pg = await b.new_page(viewport={'width': w, 'height': h})
                await pg.goto(f'http://127.0.0.1:5191/{page}.html'); await pg.wait_for_timeout(1800)
                for drawer in ([False, True] if page == 'index' else [False]):
                    if drawer:
                        await pg.locator('[data-customize]').click(); await pg.wait_for_timeout(900)
                    m = await pg.evaluate("""() => { const d = document.documentElement; const wide = [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 1 && getComputedStyle(e).position !== 'fixed').slice(0, 4).map(e => e.className.toString().slice(0, 40) || e.tagName);
                      return {sw: d.scrollWidth, cw: d.clientWidth, sh: d.scrollHeight, ch: d.clientHeight, wide} }""")
                    res.append(f"{page} {w}x{h}{' drawer' if drawer else ''}: x-over {m['sw'] - m['cw']} y-over {m['sh'] - m['ch']} {m['wide'] if m['sw'] > m['cw'] else ''}")
                    if page == 'index':
                        await pg.screenshot(path=f"{OUT}/o-{page}-{w}{'-d' if drawer else ''}.png")
                await pg.close()
        print('\n'.join(res)); await b.close()
asyncio.run(main())
