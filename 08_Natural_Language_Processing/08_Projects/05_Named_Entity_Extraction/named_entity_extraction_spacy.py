"""Extract named entities from the shared sample texts with spaCy."""

from pathlib import Path

import spacy


DATA_FILE = Path(__file__).resolve().parents[2] / "01_Preprocessing" / "sample_texts.txt"
MODEL_NAME = "en_core_web_sm"


def load_nlp():
    try:
        return spacy.load(MODEL_NAME)
    except OSError as error:
        raise RuntimeError(
            "Install the English model with: "
            "python -m spacy download en_core_web_sm"
        ) from error


def extract_entities(text: str, nlp=None):
    """Return entity text and predicted label pairs for a text."""
    if nlp is None:
        nlp = load_nlp()
    document = nlp(text)
    return [(entity.text, entity.label_) for entity in document.ents]


def main() -> None:
    nlp = load_nlp()
    texts = [
        line.strip()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    for text in texts:
        print("Text:", text)
        print("Entities:", extract_entities(text, nlp=nlp))


if __name__ == "__main__":
    main()
