"""Classify 20 Newsgroups text into four topic categories."""

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline


CATEGORIES = [
    "comp.graphics",
    "rec.sport.baseball",
    "sci.space",
    "talk.politics.misc",
]


def train_news_classifier():
    """Download/cache the data, train a model, and report test accuracy."""
    train = fetch_20newsgroups(
        subset="train",
        categories=CATEGORIES,
        remove=("headers", "footers", "quotes"),
        random_state=42,
    )
    test = fetch_20newsgroups(
        subset="test",
        categories=CATEGORIES,
        remove=("headers", "footers", "quotes"),
        random_state=42,
    )
    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer(stop_words="english", min_df=2)),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(train.data, train.target)
    predictions = model.predict(test.data)
    print(f"Holdout accuracy: {accuracy_score(test.target, predictions):.3f}")
    return model, train.target_names


def main() -> None:
    model, category_names = train_news_classifier()
    examples = [
        "The spacecraft entered orbit around the planet.",
        "The team won the final game after a late home run.",
    ]
    for text, label_id in zip(examples, model.predict(examples)):
        print(f"{category_names[int(label_id)]}: {text}")


if __name__ == "__main__":
    main()
