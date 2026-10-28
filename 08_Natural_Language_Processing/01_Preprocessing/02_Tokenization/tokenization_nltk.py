"""Tokenize text into word and punctuation tokens with NLTK."""

from nltk.tokenize import word_tokenize


def tokenize(text: str) -> list[str]:
    """Return word and punctuation tokens for text."""
    return word_tokenize(text)