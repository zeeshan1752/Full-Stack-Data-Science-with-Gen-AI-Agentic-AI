# Tokenization using NLTK

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")

# Original Text
text = """Natural Language Processing (NLP) is an interesting field of AI.
It helps computers understand human language. Python is widely used for NLP!"""

print("Original Text:")
print(text)

# Sentence Tokenization
sentences = sent_tokenize(text)

print("\nSentence Tokens:")
print(sentences)

print("\nNumber of Sentences:", len(sentences))

# Display Each Sentence
print("\nIndividual Sentences:")
for index, sentence in enumerate(sentences, start=1):
    print(f"Sentence {index}: {sentence}")

# Word Tokenization
word_tokens = word_tokenize(text)

print("\nWord Tokens:")
print(word_tokens)

print("\nNumber of Word Tokens:", len(word_tokens))

# Display Each Token
print("\nIndividual Tokens:")
for index, token in enumerate(word_tokens, start=1):
    print(f"Token {index}: {token}")

# Separate Words and Punctuation
words = [token for token in word_tokens if token.isalnum()]
punctuation = [token for token in word_tokens if not token.isalnum()]

print("\nWords:")
print(words)

print("\nPunctuation and Special Tokens:")
print(punctuation)

# Count Words
print("\nTotal Words:", len(words))

# Count Punctuation and Special Tokens
print("Total Punctuation and Special Tokens:", len(punctuation))

# Convert Tokens to Lowercase
lowercase_tokens = [token.lower() for token in word_tokens]

print("\nLowercase Tokens:")
print(lowercase_tokens)

# Count Unique Tokens
unique_tokens = set(lowercase_tokens)

print("\nUnique Tokens:")
print(unique_tokens)

print("\nNumber of Unique Tokens:", len(unique_tokens))

# Display Token Frequencies
print("\nToken Frequencies:")

for token in sorted(unique_tokens):
    print(f"{token}: {lowercase_tokens.count(token)}")

# Tokenization of a Separate Sentence
sample_text = "Hello, world! How are you?"

print("\nSample Text:")
print(sample_text)

sample_tokens = word_tokenize(sample_text)

print("\nSample Word Tokens:")
print(sample_tokens)

# Tokenization of User Input
user_text = input("\nEnter a sentence to tokenize: ")

user_tokens = word_tokenize(user_text)

print("\nUser Input:")
print(user_text)

print("\nTokens:")
print(user_tokens)

print("\nTotal Tokens:", len(user_tokens))