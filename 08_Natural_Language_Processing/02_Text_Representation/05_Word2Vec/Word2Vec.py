# Word2Vec
# This is a tiny teaching corpus. Similarity scores are illustrative only;\n# use a much larger, representative corpus for meaningful embeddings.\nimport re
from gensim.models import Word2Vec

# Create a collection of sentences
sentences = [
    "cats chase small mice",
    "dogs chase small cats",
    "mice hide in small spaces",
    "dogs and cats are animals",
    "cats and dogs are common pets",
    "animals need food and water",
    "machine learning uses data",
    "python is useful for machine learning",
    "data science uses python",
    "students learn programming with python"
]

# Convert sentences into lowercase word tokens
tokenized_sentences = [
    re.findall(r"[a-z]+", sentence.lower())
    for sentence in sentences
]

print("Original Sentences:")
for index, sentence in enumerate(sentences, start=1):
    print(f"{index}. {sentence}")

print("\nTokenized Sentences:")
for sentence in tokenized_sentences:
    print(sentence)

# Train a Skip-gram Word2Vec model
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1,
    sg=1,
    seed=42,
    epochs=200
)

# Display vocabulary
vocabulary = model.wv.index_to_key

print("\nWords in Vocabulary:")
print(sorted(vocabulary))

print("\nVocabulary Size:", len(vocabulary))

# Display vector dimensions
print("\nVector Shape for 'cats':")
print(model.wv["cats"].shape)

# Display the learned vector for a word
print("\nWord Vector for 'cats':")
print(model.wv["cats"])

# Display vectors for selected words
print("\nSelected Word Vectors:")

for word in ["cats", "dogs", "animals", "python", "data"]:
    if word in model.wv:
        print(f"\n{word}:")
        print(model.wv[word])

# Find words most similar to a selected word
print("\nWords Similar to 'cats':")

for word, score in model.wv.most_similar("cats", topn=3):
    print(f"{word}: {score:.4f}")

# Calculate similarity between two words
print("\nWord Similarity:")

similarity = model.wv.similarity("cats", "dogs")
print("Cats vs Dogs:", round(float(similarity), 4))

similarity = model.wv.similarity("python", "data")
print("Python vs Data:", round(float(similarity), 4))

# Compare CBOW and Skip-gram
cbow_model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1,
    sg=0,
    seed=42,
    epochs=200
)

print("\nCBOW Vector Shape for 'cats':")
print(cbow_model.wv["cats"].shape)

print("\nCBOW Vocabulary:")
print(sorted(cbow_model.wv.index_to_key))

# Check whether words exist in the vocabulary
print("\nVocabulary Membership:")

for word in ["cats", "dogs", "python", "computer"]:
    if word in model.wv:
        print(f"{word}: Found in vocabulary")
    else:
        print(f"{word}: Not found in vocabulary")

# Train a model with a larger minimum word count
filtered_model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=30,
    window=2,
    min_count=2,
    workers=1,
    sg=1,
    seed=42,
    epochs=100
)

print("\nVocabulary with min_count=2:")
print(sorted(filtered_model.wv.index_to_key))

# Display model configuration
print("\nWord2Vec Model Configuration:")
print("Vector Size:", model.vector_size)
print("Context Window:", model.window)
print("Minimum Word Count:", model.min_count)
print("Training Epochs:", model.epochs)
print("Architecture:", "Skip-gram" if model.sg == 1 else "CBOW")