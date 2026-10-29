"""Find the closest pair of shared sample texts with TF-IDF cosine similarity."""

from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_FILE = Path(__file__).resolve().parents[2] / "01_Preprocessing" / "sample_texts.txt"


def load_texts():
    return [
        line.strip()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def most_similar_pair(texts):
    """Return two distinct texts and their cosine similarity score."""
    if len(texts) < 2:
        raise ValueError("At least two texts are required.")
    matrix = TfidfVectorizer().fit_transform(texts)
    scores = cosine_similarity(matrix)
    for index in range(len(texts)):
        scores[index, index] = -1
    left, right = divmod(int(scores.argmax()), scores.shape[1])
    return texts[left], texts[right], float(scores[left, right])


def main() -> None:
    first, second, score = most_similar_pair(load_texts())
    print(f"Similarity: {score:.3f}")
    print("Text 1:", first)
    print("Text 2:", second)


if __name__ == "__main__":
    main()
