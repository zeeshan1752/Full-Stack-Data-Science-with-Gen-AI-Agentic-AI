"""Extract named entities with spaCy."""

from functools import lru_cache

import spacy


@lru_cache(maxsize=1)
def _load_pipeline():
    return spacy.load("en_core_web_sm")


def extract_entities(text: str) -> list[tuple[str, str]]:
    """Return entity text and spaCy label pairs."""
    document = _load_pipeline()(text)
    return [(entity.text, entity.label_) for entity in document.ents]