"""A simple, configurable text preprocessing pipeline for NLP."""

import re
import unicodedata
from html import unescape


# Small demonstration list only; choose a suitable list for your task.
DEMO_STOP_WORDS = {
    "a", "an", "and", "are", "is", "of", "the", "to"
}


def clean_text(text):
    """Decode entities and normalize selected text patterns."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = unescape(text)
    text = unicodedata.normalize("NFC", text)

    # Remove simple HTML-like tags. This is not a full HTML parser.
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove URLs and email addresses for this demonstration.
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(
        r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b",
        " ",
        text
    )

    # Lowercase is appropriate for this example, but not every task.
    text = text.lower()

    # Collapse repeated whitespace.
    return re.sub(r"\s+", " ", text).strip()


def tokenize_text(text):
    """Extract English word-like tokens and numbers."""
    return re.findall(r"[a-z]+(?:'[a-z]+)?|\d+", text)


def preprocess_text(text, remove_stop_words=False):
    """Run cleaning, tokenization, and optional stop-word removal."""
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)

    if remove_stop_words:
        tokens = [
            token for token in tokens
            if token not in DEMO_STOP_WORDS
        ]

    return tokens


if __name__ == "__main__":
    raw_text = (
        "<p>THE Cat is learning NLP &amp; Python!</p> "
        "Visit https://example.com or email team@example.com."
    )

    print("Raw text:")
    print(raw_text)

    print("\nTokens without stop-word removal:")
    print(preprocess_text(raw_text))

    print("\nTokens with demo stop-word removal:")
    print(preprocess_text(raw_text, remove_stop_words=True))
