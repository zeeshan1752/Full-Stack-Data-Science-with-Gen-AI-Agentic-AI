"""Extract dependency relations with spaCy's English pipeline."""

import spacy


MODEL_NAME = "en_core_web_sm"


def parse_dependencies(text: str, nlp=None):
    """Return dependency rows as (word, head, relation) tuples."""
    if nlp is None:
        try:
            nlp = spacy.load(MODEL_NAME)
        except OSError as error:
            raise RuntimeError(
                "Install the English model with: "
                "python -m spacy download en_core_web_sm"
            ) from error

    document = nlp(text)
    return [(token.text, token.head.text, token.dep_) for token in document]


def main() -> None:
    sentence = "The quick fox jumps over the dog."
    for word, head, relation in parse_dependencies(sentence):
        print(f"{word:10} head={head:10} relation={relation}")


if __name__ == "__main__":
    main()
