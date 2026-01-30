from playwright.async_api import async_playwright


async def fetch_url_js(url: str) -> str:
    """
    Fetch webpage content using a JavaScript-enabled browser (async).
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(url, timeout=30000)
        await page.wait_for_load_state("networkidle")

        html = await page.content()
        await browser.close()

        return html
