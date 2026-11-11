import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']); pg = await b.new_page(viewport={'width': 1280, 'height': 800})
        await pg.goto('http://127.0.0.1:5191/index.html'); await pg.wait_for_timeout(5000)
        print(await pg.evaluate("(() => { const m = document.querySelector('mux-video'); return {src: m.src, dur: m.duration, rs: m.readyState, engine: m.engineName, q: m.videoRenditions && m.videoRenditions.length, tracks: [...m.textTracks].map(t => t.kind + ':' + t.label)} })()"))
        await pg.evaluate("(() => { const m = document.querySelector('mux-video'); m.muted = true; m.currentTime = 21.4; })()")
        await pg.wait_for_timeout(2500)
        await pg.mouse.move(640, 300); await pg.wait_for_timeout(300)
        await pg.screenshot(path='/tmp/claude-1000/-home-driss-projects-orvio--claude-worktrees-clever-ramanujan-4778fc/c6c619b2-ea98-4585-9fb2-7dd0f99259b3/scratchpad/mux-ok.png')
        sb = await pg.locator('.kerf-seek').bounding_box(); await pg.mouse.move(sb['x'] + sb['width'] * 0.62, sb['y'] + 22); await pg.wait_for_timeout(900)
        await pg.screenshot(path='/tmp/claude-1000/-home-driss-projects-orvio--claude-worktrees-clever-ramanujan-4778fc/c6c619b2-ea98-4585-9fb2-7dd0f99259b3/scratchpad/mux-scrub.png')
        await pg.mouse.move(640, 300); await pg.locator('.kerf-gear').click(); await pg.wait_for_timeout(500)
        await pg.screenshot(path='/tmp/claude-1000/-home-driss-projects-orvio--claude-worktrees-clever-ramanujan-4778fc/c6c619b2-ea98-4585-9fb2-7dd0f99259b3/scratchpad/mux-menu.png')
        await b.close()
asyncio.run(main())
