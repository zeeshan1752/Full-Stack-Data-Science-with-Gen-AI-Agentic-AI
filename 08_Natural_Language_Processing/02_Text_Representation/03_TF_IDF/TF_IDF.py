# TF-IDF (Term Frequency-Inverse Document Frequency)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Create a collection of documents
documents = [
    "cats chase small mice",
    "dogs chase cats",
    "mice like small spaces",
    "dogs like playing outside",
    "machine learning uses data",
    "python is useful for machine learning",
    "data science uses python",
    "cats and dogs are common pets"
]

# Display the original documents
print("Original Documents:")

for index, document in enumerate(documents, start=1):
    print(f"Document {index}: {document}")

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Learn the vocabulary and transform documents into TF-IDF vectors
matrix = vectorizer.fit_transform(documents)

# Display the vocabulary
vocabulary = vectorizer.get_feature_names_out()

print("\nVocabulary:")
print(vocabulary.tolist())

# Display matrix dimensions
print("\nTF-IDF Matrix Shape:", matrix.shape)
print("Number of Documents:", matrix.shape[0])
print("Number of Terms:", matrix.shape[1])

# Display the sparse matrix
print("\nSparse TF-IDF Matrix:")
print(matrix)

# Convert the sparse matrix into a dense array
dense_matrix = matrix.toarray()

print("\nDense TF-IDF Matrix:")
print(dense_matrix.round(3))

# Display TF-IDF scores in tabular form
tfidf_table = pd.DataFrame(
    dense_matrix,
    columns=vocabulary,
    index=[f"Document {i}" for i in range(1, len(documents) + 1)]
)

print("\nTF-IDF Table:")
print(tfidf_table.round(3))

# Display non-zero term weights for each document
print("\nTerm Weights in Each Document:")

for index, document in enumerate(documents):
    print(f"\nDocument {index + 1}: {document}")

    row = dense_matrix[index]

    term_weights = [
        (vocabulary[i], row[i])
        for i in range(len(vocabulary))
        if row[i] > 0
    ]

    term_weights.sort(key=lambda item: item[1], reverse=True)

    for word, weight in term_weights:
        print(f"{word}: {weight:.4f}")

# Display inverse document frequency values
idf_values = vectorizer.idf_

print("\nInverse Document Frequency (IDF):")

for word, idf in zip(vocabulary, idf_values):
    print(f"{word}: {idf:.4f}")

# Calculate document frequency for each term
document_frequency = (matrix > 0).sum(axis=0).A1

print("\nDocument Frequency:")

for word, frequency in zip(vocabulary, document_frequency):
    print(f"{word}: {frequency}")

# Compare a common term and a less common term
print("\nSelected Term Comparison:")

for word in ["cats", "machine"]:
    if word in vocabulary:
        word_index = list(vocabulary).index(word)

        print("\nTerm:", word)
        print("Document Frequency:", document_frequency[word_index])
        print("IDF:", round(idf_values[word_index], 4))

# Calculate cosine similarity between documents
similarity_matrix = cosine_similarity(matrix)

print("\nCosine Similarity Matrix:")
print(similarity_matrix.round(3))

# Compare selected document pairs
print("\nSelected Document Similarities:")

print(
    "Document 1 vs Document 2:",
    round(similarity_matrix[0, 1], 3)
)

print(
    "Document 1 vs Document 3:",
    round(similarity_matrix[0, 2], 3)
)

print(
    "Document 5 vs Document 6:",
    round(similarity_matrix[4, 5], 3)
)

# Find the most similar document for each document
print("\nMost Similar Document for Each Document:")

for index in range(len(documents)):
    similarities = similarity_matrix[index].copy()

    # Exclude similarity with the document itself
    similarities[index] = -1

    most_similar_index = similarities.argmax()

    print(
        f"Document {index + 1} is most similar to "
        f"Document {most_similar_index + 1} "
        f"(similarity: {similarities[most_similar_index]:.3f})"
    )

# Generate Bag of Words counts for comparison
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(documents)

print("\nBag of Words Vocabulary:")
print(count_vectorizer.get_feature_names_out().tolist())

print("\nBag of Words Matrix Shape:", count_matrix.shape)

print("\nBag of Words Count Matrix:")
print(count_matrix.toarray())

# Compare Bag of Words and TF-IDF
print("\nBag of Words vs TF-IDF:")
print("Bag of Words stores word counts.")
print("TF-IDF weights terms using their document distribution.")

# Create TF-IDF vectors using unigrams and bigrams
bigram_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
bigram_matrix = bigram_vectorizer.fit_transform(documents)

print("\nUnigram and Bigram Vocabulary:")
print(bigram_vectorizer.get_feature_names_out().tolist())

print("\nUnigram and Bigram Matrix Shape:", bigram_matrix.shape)

# Display a small sample of the unigram and bigram matrix
print("\nFirst Document: Unigram and Bigram TF-IDF Values:")

bigram_vocabulary = bigram_vectorizer.get_feature_names_out()
first_document = bigram_matrix[0].toarray().flatten()

for word, weight in zip(bigram_vocabulary, first_document):
    if weight > 0:
        print(f"{word}: {weight:.4f}")

# Transform a new document using the already fitted vectorizer
new_document = ["cats chase mice"]

new_matrix = vectorizer.transform(new_document)

print("\nNew Document:", new_document[0])
print("Transformed TF-IDF Vector:")
print(new_matrix.toarray().round(3))

# Display the highest-weight terms in the new document
new_weights = new_matrix.toarray().flatten()

new_term_weights = [
    (vocabulary[i], new_weights[i])
    for i in range(len(vocabulary))
    if new_weights[i] > 0
]

new_term_weights.sort(key=lambda item: item[1], reverse=True)

print("\nNew Document Term Weights:")

for word, weight in new_term_weights:
    print(f"{word}: {weight:.4f}")
