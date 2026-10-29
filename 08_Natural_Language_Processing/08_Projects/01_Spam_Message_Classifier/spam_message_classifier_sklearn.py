"""Train a spam classifier from the shared UCI SMS Spam Collection file."""

import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


DATA_FILE = Path(__file__).resolve().parent / "sms_spam.tsv"


def load_messages():
    """Read UCI's tab-separated label and message columns."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            "Download the UCI SMS Spam Collection, extract SMSSpamCollection, "
            f"and place it at: {DATA_FILE}"
        )
    messages = []
    labels = []
    with DATA_FILE.open(encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            if len(row) < 2:
                continue
            label = row[0].strip().lower()
            if label not in {"ham", "spam"}:
                continue
            labels.append(label)
            messages.append(row[1])
    if not messages:
        raise ValueError("The TSV file contains no ham/spam message rows.")
    return messages, labels


def train_spam_classifier():
    """Fit a spam model and print its held-out classification report."""
    messages, labels = load_messages()
    x_train, x_test, y_train, y_test = train_test_split(
        messages, labels, test_size=0.2, random_state=42, stratify=labels
    )
    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2)),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(x_train, y_train)
    print(classification_report(y_test, model.predict(x_test), zero_division=0))
    return model


def predict_message(model, message: str) -> str:
    """Return ham or spam for a single message."""
    return str(model.predict([message])[0])


def main() -> None:
    model = train_spam_classifier()
    example = "Congratulations, you have won a free prize. Call now."
    print("Example prediction:", predict_message(model, example))


if __name__ == "__main__":
    main()
