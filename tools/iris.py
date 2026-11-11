import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1440, 'height': 900})
        await pg.goto('https://iris-player.netlify.app/', wait_until='networkidle'); await pg.wait_for_timeout(2500)
        H = await pg.evaluate('document.documentElement.scrollHeight')
        for y in range(0, H, 700):
            await pg.evaluate(f'scrollTo(0, {y})'); await pg.wait_for_timeout(120)
        await pg.evaluate('scrollTo(0, 0)'); await pg.wait_for_timeout(500)
        await pg.screenshot(path=f'{OUT}/iris-full.png', full_page=True)
        await pg.screenshot(path=f'{OUT}/iris-hero.png')
        print('height', H); await b.close()
asyncio.run(main())
