# Bag of Words

import re
from collections import Counter

# Sample documents
documents = [
    "cats chase small mice",
    "dogs chase cats",
    "mice like small spaces"
]

# Tokenize documents by converting to lowercase and extracting words
tokenized_documents = [
    re.findall(r"[a-z]+", document.lower())
    for document in documents
]

# Create a sorted vocabulary of unique words
vocabulary = sorted({
    word
    for words in tokenized_documents
    for word in words
})

print("Vocabulary:", vocabulary)

# Create the Bag of Words count matrix
print("\nCount Matrix:")
print("Rows represent documents; columns follow vocabulary order.")

for words in tokenized_documents:
    counts = Counter(words)
    print([counts[word] for word in vocabulary])