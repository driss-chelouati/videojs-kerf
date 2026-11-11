import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for vw, vh, h in [(390, 844, '#film=169'), (768, 1024, '#film=169'), (1440, 900, ''), (1440, 900, '#size=phone')]:
            pg = await b.new_page(viewport={'width': vw, 'height': vh})
            await pg.goto('http://127.0.0.1:5191/index.html' + h); await pg.wait_for_timeout(1800)
            print(vw, h, await pg.evaluate("(() => { const t = document.querySelector('.kerf-start'), k = document.querySelector('.kerf'); return {kerf: k.getBoundingClientRect().width, tile: t.getBoundingClientRect().width, cq: getComputedStyle(k).containerType + '/' + getComputedStyle(k).containerName, v: getComputedStyle(t).getPropertyValue('--kerf-tile')} })()"))
            await pg.close()
        await b.close()
asyncio.run(main())
