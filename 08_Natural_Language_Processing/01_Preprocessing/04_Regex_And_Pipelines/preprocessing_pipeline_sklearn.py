# Text Preprocessing Pipeline Using Scikit-learn

import re
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Locate the shared NLP sample text file
DATA_FILE = Path(__file__).resolve().parents[2] / "01_Preprocessing" / "sample_texts.txt"

# Read documents from the shared text file
documents = [
    line.strip()
    for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
    if line.strip()
]

# Display the original documents
print("Original Documents:")
for index, document in enumerate(documents, start=1):
    print(f"Document {index}: {document}")

# Define text cleaning using a lambda expression
cleaner = FunctionTransformer(
    lambda documents: [
        re.sub(
            r"\s+",
            " ",
            re.sub(r"[^\w\s]", " ", document.lower())
        ).strip()
        for document in documents
    ],
    validate=False
)

# Create the text preprocessing pipeline
pipeline = Pipeline([
    ("clean", cleaner),
    ("tfidf", TfidfVectorizer())
])

# Fit the pipeline and transform documents into TF-IDF features
features = pipeline.fit_transform(documents)

# Retrieve cleaned documents
cleaned_documents = pipeline.named_steps["clean"].transform(documents)

print("\nCleaned Documents:")
for index, document in enumerate(cleaned_documents, start=1):
    print(f"Document {index}: {document}")

# Display the total number of documents and features
print("\nDataset Information:")
print("Total Documents:", len(documents))
print("TF-IDF Matrix Shape:", features.shape)
print("Total Features:", features.shape[1])

# Display feature names
terms = pipeline.named_steps["tfidf"].get_feature_names_out()

print("\nFirst 10 Feature Names:")
print(terms[:10].tolist())

print("\nComplete Vocabulary:")
print(terms.tolist())

# Convert the sparse TF-IDF matrix into a dense array for inspection
tfidf_array = features.toarray()

print("\nTF-IDF Feature Matrix:")
print(tfidf_array)

# Display TF-IDF values for each document
print("\nTF-IDF Values for Each Document:")
for index, row in enumerate(tfidf_array, start=1):
    print(f"Document {index}:")
    for term, score in zip(terms, row):
        if score > 0:
            print(f"  {term}: {score:.4f}")

# Display the highest-scoring terms in each document
print("\nTop 5 TF-IDF Terms per Document:")
for index, row in enumerate(tfidf_array, start=1):
    top_indices = row.argsort()[::-1][:5]

    top_terms = [
        (terms[i], round(row[i], 4))
        for i in top_indices
        if row[i] > 0
    ]

    print(f"Document {index}: {top_terms}")

# Calculate cosine similarity between documents
similarity_matrix = cosine_similarity(features)

print("\nCosine Similarity Matrix:")
print(similarity_matrix)

# Display pairwise similarity scores
print("\nDocument Similarity Scores:")
for i in range(len(documents)):
    for j in range(i + 1, len(documents)):
        print(
            f"Document {i + 1} and Document {j + 1}: "
            f"{similarity_matrix[i, j]:.4f}"
        )

# Transform a new document using the fitted pipeline
new_document = ["Natural language processing uses machine learning"]

new_features = pipeline.transform(new_document)

print("\nNew Document:")
print(new_document[0])

print("\nNew Document TF-IDF Shape:")
print(new_features.shape)

print("\nNew Document TF-IDF Features:")
print(new_features.toarray())