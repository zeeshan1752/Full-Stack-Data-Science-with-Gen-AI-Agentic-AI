# N-Grams

import re

# Sample sentence
text = "Natural language models learn from sequences of words."

print("Original Text:", text)

# Tokenization
tokens = re.findall(r"[a-z]+", text.lower())

print("Tokens:", tokens)

# Unigrams (N = 1)
unigrams = [
    tuple(tokens[index:index + 1])
    for index in range(len(tokens))
]

print("\nUnigrams:")
print(unigrams)

# Bigrams (N = 2)
bigrams = [
    tuple(tokens[index:index + 2])
    for index in range(len(tokens) - 1)
]

print("\nBigrams:")
print(bigrams)

# Trigrams (N = 3)
trigrams = [
    tuple(tokens[index:index + 3])
    for index in range(len(tokens) - 2)
]

print("\nTrigrams:")
print(trigrams)

# General N-Grams
n = 4

n_grams = [
    tuple(tokens[index:index + n])
    for index in range(len(tokens) - n + 1)
]

print(f"\n{n}-Grams:")
print(n_grams)

# Count the number of N-Grams
print("\nNumber of Unigrams:", len(unigrams))
print("Number of Bigrams:", len(bigrams))
print("Number of Trigrams:", len(trigrams))
print(f"Number of {n}-Grams:", len(n_grams))