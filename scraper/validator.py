def validate_text(text: str) -> None:
    if not text or len(text) < 200:
        raise ValueError("Extracted content too short or empty")
