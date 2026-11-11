import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        for ch in [None, 'chrome']:
            try:
                b = await (p.chromium.launch(channel=ch) if ch else p.chromium.launch())
            except Exception as e:
                print(ch, 'unavailable', str(e)[:80]); continue
            pg = await b.new_page()
            await pg.goto('http://127.0.0.1:5191/preview.html#width=640')
            await pg.wait_for_timeout(4000)
            r = await pg.evaluate('''() => { const m = document.querySelector('mux-video'); return {mse: MediaSource.isTypeSupported('video/mp4; codecs="avc1.640028,mp4a.40.2"'), canMp4: document.createElement('video').canPlayType('video/mp4; codecs="avc1.42E01E"'), dur: m && m.duration, err: m && m.error && (m.error.message || m.error.code), ready: m && m.readyState}; }''')
            print(ch or 'bundled', r); await b.close()
asyncio.run(main())
