import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 390, 'height': 844})
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(1500)
        print(await pg.evaluate("""() => { const r = e => { const b = document.querySelector(e).getBoundingClientRect(); return [Math.round(b.width), Math.round(b.height)] };
          return {app: r('.app'), stage: r('.stage'), center: r('.stage-center'), device: r('.device'), drawer: r('.drawer'), cols: getComputedStyle(document.querySelector('.app')).gridTemplateColumns, rows: getComputedStyle(document.querySelector('.app')).gridTemplateRows, pw: getComputedStyle(document.querySelector('.stage')).getPropertyValue('--player-w')} }"""))
        await b.close()
asyncio.run(main())
