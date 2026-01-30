from scraper.fetcher import fetch_url
from scraper.cleaner import clean_html
from scraper.validator import validate_text
from summarizer.llm import summarize

def run_pipeline(url: str) -> dict:
    html = fetch_url(url)
    text = clean_html(html)
    validate_text(text)
    summary = summarize(text)

    return {
        "url": url,
        "summary": summary,
        "word_count": len(text.split()),
        "status": "success"
    }
