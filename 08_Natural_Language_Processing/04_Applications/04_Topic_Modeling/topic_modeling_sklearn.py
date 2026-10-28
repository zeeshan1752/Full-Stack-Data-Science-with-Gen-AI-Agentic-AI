"""Show a small Latent Dirichlet Allocation topic-modeling example."""

from pathlib import Path

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "sample_texts.txt"


def top_words_per_topic(texts, topic_count=3, words_per_topic=5):
    """Return the most prominent words for each learned topic."""
    vectorizer = CountVectorizer(stop_words="english")
    document_terms = vectorizer.fit_transform(texts)
    model = LatentDirichletAllocation(
        n_components=topic_count, random_state=42, max_iter=10
    )
    model.fit(document_terms)
    terms = vectorizer.get_feature_names_out()
    topics = []
    for topic in model.components_:
        top_indices = topic.argsort()[-words_per_topic:][::-1]
        topics.append([terms[index] for index in top_indices])
    return topics


def main() -> None:
    texts = [
        line.strip()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    for number, words in enumerate(top_words_per_topic(texts), start=1):
        print(f"Topic {number}: {', '.join(words)}")


if __name__ == "__main__":
    main()
