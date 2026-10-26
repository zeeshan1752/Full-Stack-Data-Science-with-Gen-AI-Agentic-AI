# Text Normalization

import re
import unicodedata

# Original text
text = "   HELLO!!!   I don't know   why u r waiting.   "

print("Original Text:", repr(text))

# Unicode normalization
text = unicodedata.normalize("NFC", text)

print("\nAfter Unicode Normalization:")
print(text)

# Convert text to lowercase
text = text.lower()

print("\nAfter Lowercasing:")
print(text)

# Expand contractions
text = text.replace("don't", "do not")

print("\nAfter Contraction Expansion:")
print(text)

# Normalize informal words
normalization_map = {
    "u": "you",
    "r": "are",
    "gr8": "great",
    "pls": "please",
    "thx": "thanks"
}

words = text.split()

normalized_words = [
    normalization_map.get(word, word)
    for word in words
]

text = " ".join(normalized_words)

print("\nAfter Informal Word Normalization:")
print(text)

# Normalize repeated whitespace
text = re.sub(r"\s+", " ", text).strip()

print("\nAfter Whitespace Normalization:")
print(text)

# Normalize repeated characters
text = re.sub(r"(.)\1{2,}", r"\1\1", text)

print("\nAfter Repeated Character Normalization:")
print(text)

# Normalize a separate example with extra spaces
sample_text = "   Natural     Language\n\nProcessing   "

normalized_text = re.sub(r"\s+", " ", sample_text).strip()

print("\nWhitespace Example:")
print("Original:", repr(sample_text))
print("Normalized:", normalized_text)

# Compare lowercase and uppercase text
sample_text = "Natural Language Processing"

print("\nCase Normalization:")
print("Original:", sample_text)
print("Lowercase:", sample_text.lower())
print("Uppercase:", sample_text.upper())

# Demonstrate Unicode normalization
unicode_text = "café"

normalized_unicode = unicodedata.normalize("NFC", unicode_text)

print("\nUnicode Normalization:")
print("Original:", unicode_text)
print("NFC Normalized:", normalized_unicode)

# Compare different Unicode normalization forms
print("NFD Normalized:", unicodedata.normalize("NFD", unicode_text))
print("NFKC Normalized:", unicodedata.normalize("NFKC", unicode_text))
print("NFKD Normalized:", unicodedata.normalize("NFKD", unicode_text))

# Demonstrate text normalization before tokenization
sample_text = "   PYTHON    is   GREAT!!!   "

normalized_text = sample_text.lower()
normalized_text = re.sub(r"\s+", " ", normalized_text).strip()

tokens = normalized_text.split()

print("\nNormalization Before Tokenization:")
print("Normalized Text:", normalized_text)
print("Tokens:", tokens)

# Compare text before and after normalization
original_text = "   HELLO     WORLD!   "

normalized_text = original_text.lower()
normalized_text = re.sub(r"\s+", " ", normalized_text).strip()

print("\nBefore and After Comparison:")
print("Original Text:", repr(original_text))
print("Normalized Text:", normalized_text)