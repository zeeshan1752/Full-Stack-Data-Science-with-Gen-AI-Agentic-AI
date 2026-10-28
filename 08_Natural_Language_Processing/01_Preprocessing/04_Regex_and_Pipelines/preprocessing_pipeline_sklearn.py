"""Clean sample text and convert it to TF-IDF features with a pipeline."""

import re
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer


DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "sample_texts.txt"


def clean_documents(documents):
    """Apply simple lowercase and punctuation cleaning to each document."""
    cleaned = []
    for document in documents:
        document = document.lower()
        document = re.sub(r"[^\w\s]", " ", document)
        cleaned.append(re.sub(r"\s+", " ", document).strip())
    return cleaned


def main() -> None:
    documents = [
        line.strip()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    pipeline = Pipeline(
        [
            (
                "clean",
                FunctionTransformer(clean_documents, validate=False),
            ),
            ("tfidf", TfidfVectorizer()),
        ]
    )
    features = pipeline.fit_transform(documents)
    terms = pipeline.named_steps["tfidf"].get_feature_names_out()
    print("Document-term matrix shape:", features.shape)
    print("First feature names:", terms[:10].tolist())


if __name__ == "__main__":
    main()
