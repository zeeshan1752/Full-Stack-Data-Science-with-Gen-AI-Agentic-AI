"""Group shared sample texts with a small TF-IDF and K-means example."""

from pathlib import Path

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


DATA_FILE = Path(__file__).resolve().parents[2] / "01_Preprocessing" / "sample_texts.txt"


def cluster_texts(texts, cluster_count=3):
    """Return one cluster number for each text."""
    if not texts:
        raise ValueError("At least one text is required.")
    if not 1 <= cluster_count <= len(texts):
        raise ValueError("The cluster count must be between 1 and the text count.")
    features = TfidfVectorizer().fit_transform(texts)
    model = KMeans(n_clusters=cluster_count, n_init=10, random_state=42)
    return model.fit_predict(features).tolist()


def main() -> None:
    texts = [
        line.strip()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    labels = cluster_texts(texts)
    for label, text in zip(labels, texts):
        print(f"Cluster {label}: {text}")


if __name__ == "__main__":
    main()
