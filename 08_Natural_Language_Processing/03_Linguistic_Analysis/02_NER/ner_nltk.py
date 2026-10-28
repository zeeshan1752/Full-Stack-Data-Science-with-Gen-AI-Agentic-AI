"""Extract named entities with NLTK."""

import nltk
from nltk import Tree


def extract_entities(text: str) -> list[tuple[str, str]]:
    """Return entity text and NLTK entity label pairs."""
    tagged = nltk.pos_tag(nltk.word_tokenize(text))
    tree = nltk.ne_chunk(tagged, binary=False)
    return [
        (" ".join(word for word, _tag in node.leaves()), node.label())
        for node in tree
        if isinstance(node, Tree)
    ]