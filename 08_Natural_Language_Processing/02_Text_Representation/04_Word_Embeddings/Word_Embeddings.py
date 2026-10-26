"""Introductory word embedding demonstrations using Python's standard library.

The vectors defined here are illustrative teaching values, not pretrained embeddings.
See Word_Embeddings.ipynb for a longer lesson and optional Gensim Word2Vec training.
"""
from math import sqrt
import re


# Create illustrative dense vectors
embeddings = {
    "cat": [0.80, 0.20, 0.10, 0.70],
    "kitten": [0.75, 0.25, 0.15, 0.72],
    "dog": [0.70, 0.30, 0.20, 0.65],
    "banana": [0.10, 0.80, 0.90, 0.10],
}

print("Available words:", list(embeddings))
print("Vector for cat:", embeddings["cat"])
print("Embedding dimension:", len(embeddings["cat"]))


# Calculate cosine similarity between two vectors
def cosine_similarity(vector_a, vector_b):
    """Return cosine similarity for two non-zero vectors of equal length."""
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimension.")

    dot = sum(a * b for a, b in zip(vector_a, vector_b))
    norm_a = sqrt(sum(value * value for value in vector_a))
    norm_b = sqrt(sum(value * value for value in vector_b))

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector.")

    return dot / (norm_a * norm_b)


# Compare the illustrative word vectors
print("\nCosine similarity:")
for first, second in [("cat", "kitten"), ("cat", "dog"), ("cat", "banana")]:
    score = cosine_similarity(embeddings[first], embeddings[second])
    print(f"{first} vs {second}: {score:.4f}")


# Build a vocabulary and word-to-index mapping
corpus = [
    "cats chase small mice",
    "dogs chase small cats",
    "mice hide in small spaces",
]
tokens = []
for sentence in corpus:
    tokens.extend(re.findall(r"[a-z]+", sentence.lower()))

vocabulary = sorted(set(tokens))
word_to_index = {word: index for index, word in enumerate(vocabulary)}
index_to_word = {index: word for word, index in word_to_index.items()}

print("\nVocabulary:", vocabulary)
print("Word-to-index mapping:", word_to_index)
print("Index 0 represents:", index_to_word[0])


# Average word vectors to create a simple sentence vector
def average_vectors(words, vector_table):
    """Average known vectors; return None if no tokens are represented."""
    known_vectors = [vector_table[word] for word in words if word in vector_table]
    if not known_vectors:
        return None

    dimensions = len(known_vectors[0])
    return [
        sum(vector[i] for vector in known_vectors) / len(known_vectors)
        for i in range(dimensions)
    ]


sentence_a = ["cat", "kitten"]
sentence_b = ["dog", "cat"]
vector_a = average_vectors(sentence_a, embeddings)
vector_b = average_vectors(sentence_b, embeddings)

print("\nAverage vector for", sentence_a, ":", vector_a)
print("Average vector for", sentence_b, ":", vector_b)
print("Sentence similarity:", round(cosine_similarity(vector_a, vector_b), 4))


# Find the nearest available words by cosine similarity
def most_similar(query_word, vector_table, top_n=3):
    """Rank the other known words by cosine similarity."""
    if query_word not in vector_table:
        raise KeyError(f"Unknown word: {query_word}")

    scores = [
        (word, cosine_similarity(vector_table[query_word], vector))
        for word, vector in vector_table.items()
        if word != query_word
    ]
    return sorted(scores, key=lambda item: item[1], reverse=True)[:top_n]


print("\nWords most similar to cat in this illustrative table:")
for word, score in most_similar("cat", embeddings):
    print(f"{word}: {score:.4f}")


# Demonstrate context-window pairs used by predictive embedding methods
def context_pairs(tokens, window_size=2):
    """Return (target, context) pairs within a symmetric window."""
    pairs = []
    for i, target in enumerate(tokens):
        start = max(0, i - window_size)
        end = min(len(tokens), i + window_size + 1)
        for j in range(start, end):
            if i != j:
                pairs.append((target, tokens[j]))
    return pairs


print("\nContext pairs for 'cats chase small mice':")
for pair in context_pairs(["cats", "chase", "small", "mice"], window_size=2):
    print(pair)


# Reminder about the example
print(
    "\nReminder: these vectors were manually defined for learning. "
    "They are not learned or production-quality embeddings."
)
