import asyncio, sys, json
from playwright.async_api import async_playwright
OUT = sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']); out = []
        c = await b.new_context(viewport={'width': 1440, 'height': 900}, color_scheme='dark'); pg = await c.new_page()
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text[:160]) if m.type == 'error' else None)
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(2500)
        await pg.screenshot(path=f'{OUT}/c1-player.png')
        await pg.locator('[data-customize]').click(); await pg.wait_for_timeout(700)
        out.append('after open: ' + await pg.evaluate("document.getElementById('app').dataset.drawer"))
        await pg.locator('[data-close]').click(); await pg.wait_for_timeout(700)
        out.append('after close click: ' + await pg.evaluate("document.getElementById('app').dataset.drawer"))
        await pg.locator('[data-customize]').click(); await pg.wait_for_timeout(700)
        await pg.locator('label:has(input[name="film"][value="916"])').click(); await pg.wait_for_timeout(1500)
        out.append('916 size: ' + await pg.evaluate("document.querySelector('input[name=size]:checked').value"))
        await pg.screenshot(path=f'{OUT}/c2-916.png')
        await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(2500)
        await pg.screenshot(path=f'{OUT}/c3-design-top.png')
        top = await pg.evaluate("document.querySelector('.explode').offsetTop")
        h = await pg.evaluate("document.querySelector('.explode').offsetHeight")
        for i, f in enumerate([0.05, 0.35, 0.7]):
            await pg.evaluate(f"scrollTo(0, {top} + ({h} - innerHeight) * {f})"); await pg.wait_for_timeout(600)
            await pg.screenshot(path=f'{OUT}/c4-explode-{i}.png')
            out.append(f'explode {f}: ' + await pg.evaluate("getComputedStyle(document.querySelector('.layer-3')).transform.slice(0,60)"))
        await pg.evaluate("scrollTo(0, 0)"); await pg.wait_for_timeout(300)
        # scroll through to trigger reveals, then a full page capture
        H = await pg.evaluate("document.documentElement.scrollHeight")
        for y in range(0, H, 500):
            await pg.evaluate(f"scrollTo(0, {y})"); await pg.wait_for_timeout(60)
        await pg.evaluate("scrollTo(0, 0)"); await pg.wait_for_timeout(400)
        await pg.screenshot(path=f'{OUT}/c5-design-full.png', full_page=True)
        out.append('x-over design: ' + str(await pg.evaluate("document.documentElement.scrollWidth - innerWidth")))
        await c.close()
        c = await b.new_context(viewport={'width': 390, 'height': 844}, color_scheme='dark'); pg = await c.new_page()
        await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(2000)
        H = await pg.evaluate("document.documentElement.scrollHeight")
        for y in range(0, H, 500):
            await pg.evaluate(f"scrollTo(0, {y})"); await pg.wait_for_timeout(50)
        await pg.evaluate("scrollTo(0, 0)"); await pg.wait_for_timeout(300)
        await pg.screenshot(path=f'{OUT}/c6-design-mobile.png', full_page=True)
        out.append('x-over design mobile: ' + str(await pg.evaluate("document.documentElement.scrollWidth - innerWidth")))
        print('\n'.join(out)); print('errors:', errs[:6]); await b.close()
asyncio.run(main())
