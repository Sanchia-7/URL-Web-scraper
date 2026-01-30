# from scraper.fetcher import fetch_url
# from scraper.cleaner import clean_html
# from scraper.validator import validate_text
# from summarizer.llm import summarize
#
# def run_pipeline(url: str) -> dict:
#     html = fetch_url(url)
#     text = clean_html(html)
#     validate_text(text)
#     summary = summarize(text)
#
#     return {
#         "url": url,
#         "summary": summary,
#         "word_count": len(text.split()),
#         "status": "success"
#     }

from scraper.fetcher import fetch_url
from scraper.js_fetcher import fetch_url_js
from scraper.cleaner import clean_html
from scraper.validator import validate_text
from summarizer.llm import summarize


async def run_pipeline(url: str) -> dict:
    """
    Runs the scraping and summarization pipeline.
    Falls back to JavaScript rendering when static HTML fails.
    """
    rendering_mode = "html"

    try:
        # 1️⃣ Try static HTML first
        html = fetch_url(url)
        text = clean_html(html)
        validate_text(text, url)

    except ValueError:
        # 2️⃣ Fallback to JavaScript rendering (ASYNC)
        rendering_mode = "javascript"
        html = await fetch_url_js(url)
        text = clean_html(html)
        validate_text(text, url)

    summary = summarize(text)

    return {
        "url": url,
        "summary": summary,
        "word_count": len(text.split()),
        "rendering_mode": rendering_mode,
    }
