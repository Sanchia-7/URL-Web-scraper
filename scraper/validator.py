# def validate_text(text: str) -> None:
#     if not text or len(text) < 100:
#         raise ValueError("Extracted content too short or empty.\nWord count: {}".format(len(text)))
def validate_text(text: str, source_url: str = "") -> None:
    """
    Validates extracted webpage text to ensure it is usable.
    Provides helpful errors for JavaScript-heavy or blocked sites.
    """
    word_count = len(text.split())

    if word_count < 50:
        raise ValueError(
            f"Extracted content too short or empty. Word count: {word_count}"
        )
