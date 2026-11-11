"""Screenshots of the Kerf site pages. usage: site_shots.py <out_dir> [page]   (through tools/run-heavy.sh)"""
import asyncio, sys, os
from playwright.async_api import async_playwright

OUT = sys.argv[1]
PAGE = sys.argv[2] if len(sys.argv) > 2 else 'index'
os.makedirs(OUT, exist_ok=True)
BASE = 'http://127.0.0.1:5191/'


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        logs = []

        async def page(w, h, hash_='', theme=None, scheme='dark'):
            c = await b.new_context(viewport={'width': w, 'height': h}, color_scheme=scheme, device_scale_factor=1)
            pg = await c.new_page()
            pg.on('console', lambda m: logs.append(f'{w}: {m.type}: {m.text[:200]}') if m.type in ('error', 'warning') else None)
            pg.on('pageerror', lambda e: logs.append(f'{w}: pageerror: {e}'))
            await pg.goto(f'{BASE}{PAGE}.html{hash_}')
            await pg.wait_for_timeout(2500)
            return c, pg

        if PAGE == 'index':
            c, pg = await page(1440, 900)
            await pg.screenshot(path=f'{OUT}/p1-desktop.png')
            info = await pg.evaluate("(() => { const m = document.querySelector('mux-video'); return m ? {dur: m.duration, rs: m.readyState, err: m.error && m.error.message} : null })()")
            logs.append(f'mux: {info}')
            await pg.locator('[data-customize]').click()
            await pg.wait_for_timeout(900)
            await pg.screenshot(path=f'{OUT}/p2-drawer.png')
            await pg.locator('input[name="surface"][value="light"]').check(force=True)
            await pg.locator('input[name="accent"][value="#3155ff"]').check(force=True)
            await pg.locator('input[name="size"][value="tablet"]').check(force=True)
            await pg.wait_for_timeout(900)
            await pg.screenshot(path=f'{OUT}/p3-tablet-light.png')
            await pg.locator('input[name="size"][value="phone"]').check(force=True)
            await pg.locator('input[name="film"][value="916"]').check(force=True)
            await pg.wait_for_timeout(1500)
            await pg.screenshot(path=f'{OUT}/p4-phone-916.png')
            await pg.locator('[data-theme-toggle]').click()
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=f'{OUT}/p5-site-light.png')
            await c.close()
            c, pg = await page(390, 844)
            await pg.screenshot(path=f'{OUT}/p6-mobile.png')
            await pg.locator('[data-customize]').click()
            await pg.wait_for_timeout(900)
            await pg.screenshot(path=f'{OUT}/p7-mobile-drawer.png')
            await c.close()
        else:
            c, pg = await page(1440, 900)
            await pg.screenshot(path=f'{OUT}/d1-full.png', full_page=True)
            await c.close()
            c, pg = await page(390, 844)
            await pg.screenshot(path=f'{OUT}/d2-mobile.png', full_page=True)
            await c.close()
        print('\n'.join(logs) or 'no console errors')
        await b.close()

asyncio.run(main())
