import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

def fetch_url(url: str) -> str:
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        return response.text

    except requests.HTTPError as e:
        raise RuntimeError(
            f"Site blocked scraping (HTTP {response.status_code})."
        )

    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch URL: {e}")
