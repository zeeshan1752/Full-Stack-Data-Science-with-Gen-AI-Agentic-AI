"""Normalize shared sample text with Python's regular-expression library."""

import re
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "sample_texts.txt"


def clean_text(text: str) -> str:
    """Lowercase text, replace punctuation with spaces, and collapse whitespace."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def main() -> None:
    samples = DATA_FILE.read_text(encoding="utf-8").splitlines()
    for sample in samples:
        if sample.strip():
            print(clean_text(sample))


if __name__ == "__main__":
    main()
