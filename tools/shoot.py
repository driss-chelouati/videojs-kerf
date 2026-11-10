import sys, asyncio
from playwright.async_api import async_playwright
# usage: shoot.py <html> <out.png> [scale] [clip: x,y,w,h]
async def main():
    src, out = sys.argv[1], sys.argv[2]
    scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1600, 'height': 1000}, device_scale_factor=scale)
        await pg.goto('file://' + src)
        await pg.wait_for_load_state('networkidle')
        await pg.evaluate('document.fonts.ready')
        await pg.wait_for_timeout(400)
        if len(sys.argv) > 4:
            x, y, w, h = map(int, sys.argv[4].split(','))
            await pg.screenshot(path=out, clip={'x': x, 'y': y, 'width': w, 'height': h})
        else:
            await pg.screenshot(path=out, full_page=True)
        h = await pg.evaluate('document.documentElement.scrollHeight')
        print('height', h)
        await b.close()
asyncio.run(main())
