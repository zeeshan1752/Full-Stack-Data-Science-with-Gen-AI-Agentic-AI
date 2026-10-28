"""Tokenize text into word and punctuation tokens with spaCy."""

from functools import lru_cache

import spacy


@lru_cache(maxsize=1)
def _load_pipeline():
    return spacy.load("en_core_web_sm")


def tokenize(text: str) -> list[str]:
    """Return word and punctuation tokens for text."""
    return [token.text for token in _load_pipeline()(text) if not token.is_space]