"""Train a simple sentiment model on the shared synthetic review dataset."""

import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


DATA_FILE = Path(__file__).resolve().parents[2] / "04_Neural_Models" / "restaurant_reviews.tsv"


def load_reviews():
    """Return review text and integer sentiment labels from the shared TSV."""
    with DATA_FILE.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file, delimiter="\t"))
    texts = [row["Review"] for row in rows]
    labels = [int(row["Liked"]) for row in rows]
    return texts, labels


def train_sentiment_model():
    """Fit a TF-IDF and logistic-regression pipeline and report holdout accuracy."""
    texts, labels = load_reviews()
    x_train, x_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )
    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2)),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(f"Holdout accuracy: {accuracy_score(y_test, predictions):.3f}")
    return model


def predict_sentiment(model, text: str) -> str:
    """Return positive or negative for one review."""
    label = int(model.predict([text])[0])
    return "positive" if label == 1 else "negative"


def main() -> None:
    model = train_sentiment_model()
    example = "The meal was fresh and the staff were kind."
    print(f"Example prediction: {predict_sentiment(model, example)}")


if __name__ == "__main__":
    main()
