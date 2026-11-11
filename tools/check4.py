import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 1440, 'height': 900}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(1500)
        W = lambda: pg.evaluate("Math.round(document.getElementById('player-slot').getBoundingClientRect().width) + 'x' + Math.round(document.getElementById('player-slot').getBoundingClientRect().height)")
        log = ['start ' + await W()]
        await pg.locator('[data-customize]').click(); await pg.wait_for_timeout(800); log.append('drawer ' + await W())
        for step in [('size', 'tablet'), ('size', 'phone'), ('size', 'desktop'), ('film', '916'), ('size', 'tablet'), ('size', 'desktop'), ('film', '169'), ('size', 'phone'), ('size', 'desktop')]:
            await pg.locator(f'label:has(input[name="{step[0]}"][value="{step[1]}"])').click(); await pg.wait_for_timeout(900)
            log.append(f'{step[0]}={step[1]} ' + await W())
            if step == ('film', '916'): await pg.screenshot(path=f'{OUT}/s-916.png')
        await pg.locator('[data-close]').click(); await pg.wait_for_timeout(800); log.append('closed ' + await W())
        await pg.screenshot(path=f'{OUT}/s-desktop.png')
        print('\n'.join(log)); await pg.close()
        for vw, vh in [(390, 844), (768, 1024)]:
            pg = await b.new_page(viewport={'width': vw, 'height': vh}, color_scheme='dark')
            await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(1500)
            print(vw, 'player', await W())
            await pg.screenshot(path=f'{OUT}/m-{vw}.png')
            await pg.locator('[data-customize]').click(); await pg.wait_for_timeout(800)
            await pg.locator('label:has(input[name="film"][value="916"])').click(); await pg.wait_for_timeout(1200)
            print(vw, '916 with drawer', await W())
            await pg.screenshot(path=f'{OUT}/m-{vw}-drawer.png')
            await pg.close()
        await b.close()
asyncio.run(main())
