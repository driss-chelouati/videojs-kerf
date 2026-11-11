"""Accessibility audit of the Kerf site: axe-core on each page and state, plus target sizes and focus visibility.
usage: a11y.py <out_dir>   (through tools/run-heavy.sh)"""
import asyncio, sys, json
from playwright.async_api import async_playwright

OUT = sys.argv[1]
AXE = 'https://cdn.jsdelivr.net/npm/axe-core@4.10.2/axe.min.js'


async def axe(pg, label, results):
    await pg.add_script_tag(url=AXE)
    r = await pg.evaluate("""async () => { const r = await axe.run(document, { resultTypes: ['violations'] });
      return r.violations.map(v => ({ id: v.id, impact: v.impact, help: v.help, nodes: v.nodes.slice(0, 4).map(n => n.target.join(' ') + ' :: ' + (n.failureSummary || '').split('\\n').slice(1, 2).join('')) })) }""")
    results[label] = r


async def main():
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        for scheme in ['dark', 'light']:
            pg = await b.new_page(viewport={'width': 1280, 'height': 800}, color_scheme=scheme)
            await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(2500)
            k = await pg.locator('.kerf').bounding_box()
            await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 2); await pg.wait_for_timeout(400)
            await axe(pg, f'player {scheme}', res)
            await pg.locator('[data-customize]').click(); await pg.wait_for_timeout(700)
            await axe(pg, f'player {scheme} drawer', res)
            await pg.locator('[data-close]').click(); await pg.wait_for_timeout(500)
            await pg.mouse.move(k['x'] + k['width'] / 2, k['y'] + k['height'] / 2)
            await pg.locator('.kerf-gear').click(); await pg.wait_for_timeout(500)
            await axe(pg, f'player {scheme} menu', res)
            await pg.keyboard.press('Escape')
            # touch targets inside the player
            sizes = await pg.evaluate("""() => [...document.querySelectorAll('.kerf button, .kerf [role=button], .kerf-seek, .kerf-blade')].filter(e => e.offsetParent).map(e => { const r = e.getBoundingClientRect(); return [e.className.toString().split(' ').slice(0,2).join('.'), Math.round(r.width), Math.round(r.height)] })""")
            res[f'targets {scheme}'] = [s for s in sizes if s[1] < 44 or s[2] < 24]
            await pg.close()
        pg = await b.new_page(viewport={'width': 1440, 'height': 900}, color_scheme='dark')
        await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(2000)
        H = await pg.evaluate('document.documentElement.scrollHeight')
        for y in range(0, H, 600):
            await pg.evaluate(f'scrollTo(0, {y})'); await pg.wait_for_timeout(40)
        await pg.evaluate('scrollTo(0, 0)')
        await axe(pg, 'design dark', res)
        # keyboard: every focusable element shows a visible outline or ring
        bad = await pg.evaluate("""() => { const out = []; for (const el of document.querySelectorAll('a[href], button, input, [tabindex="0"]')) { if (!el.offsetParent) continue; el.focus(); const cs = getComputedStyle(el); const ring = (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) || cs.boxShadow !== 'none'; if (!ring && document.activeElement === el) out.push(el.className.toString().slice(0, 30) || el.tagName); } return out.slice(0, 10) }""")
        res['design focus without visible ring (programmatic focus)'] = bad
        await pg.close()
        # reduced motion: no running animations on the design page
        c = await b.new_context(viewport={'width': 1440, 'height': 900}, reduced_motion='reduce')
        pg = await c.new_page(); await pg.goto('http://127.0.0.1:5191/design.html'); await pg.wait_for_timeout(1500)
        res['reduced motion running animations'] = await pg.evaluate("document.getAnimations().filter(a => a.playState === 'running').map(a => (a.animationName || a.constructor.name) + ' on ' + (a.effect && a.effect.target && a.effect.target.className && a.effect.target.className.toString().slice(0, 30))).slice(0, 10)")
        await c.close()
        await b.close()
    json.dump(res, open(f'{OUT}/a11y.json', 'w'), indent=1)
    for k, v in res.items():
        print(f'== {k}: {len(v) if isinstance(v, list) else v}')
        if isinstance(v, list):
            for x in v[:8]:
                print('   ', x if not isinstance(x, dict) else f"{x['impact']} {x['id']}: {x['help']} | {x['nodes'][:2]}")

asyncio.run(main())
