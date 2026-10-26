"""Build a Bag of Words matrix from a few example documents.

Install dependencies with:
python -m pip install scikit-learn
"""
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "cats chase small mice",
    "dogs chase small cats",
    "mice hide in small spaces",
]

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)

print("Vocabulary in column order:")
print(vectorizer.get_feature_names_out().tolist())

print("\nBag of Words matrix (rows are documents, columns are vocabulary terms):")
print(bow_matrix.toarray())

print("\nDocument-term matrix shape:", bow_matrix.shape)
