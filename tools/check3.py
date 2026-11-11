import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for vw, vh in [(1440, 900), (1920, 1080), (390, 844)]:
            pg = await b.new_page(viewport={'width': vw, 'height': vh}, color_scheme='dark')
            await pg.goto('http://127.0.0.1:5191/index.html', wait_until='domcontentloaded')
            ws = []
            for t in [150, 400, 900, 2500]:
                await pg.wait_for_timeout(t - (0 if not ws else [150, 400, 900, 2500][len(ws) - 1]))
                ws.append(await pg.evaluate("Math.round(document.getElementById('player-slot').getBoundingClientRect().width)"))
            print(vw, 'player widths over time', ws)
            await pg.screenshot(path=f'{OUT}/load-{vw}.png')
            await pg.close()
        pg = await b.new_page(viewport={'width': 1440, 'height': 900}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(2000)
        top = await pg.evaluate("document.querySelector('.explode').offsetTop"); h = await pg.evaluate("document.querySelector('.explode').offsetHeight")
        await pg.evaluate(f"scrollTo(0, {top} + ({h} - innerHeight) * 0.75)"); await pg.wait_for_timeout(700)
        await pg.screenshot(path=f'{OUT}/explode-final.png')
        await b.close()
asyncio.run(main())
