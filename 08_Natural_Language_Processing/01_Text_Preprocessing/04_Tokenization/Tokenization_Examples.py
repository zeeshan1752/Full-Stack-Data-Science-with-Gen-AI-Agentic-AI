# Tokenization Examples

# Install: python -m pip install nltk

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize

text = "NLP is useful. Tokenizers split text into units!"

# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("Words:", words)

# Word-Punctuation Tokenization
word_punctuation = wordpunct_tokenize(text)
print("Word-punctuation tokens:", word_punctuation)