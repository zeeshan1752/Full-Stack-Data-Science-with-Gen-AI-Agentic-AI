# Stop Word Removal

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

text = "This is a small example, and it is not perfect."

print("Original Text:", text)

# Tokenize the text
words = word_tokenize(text)

# Load English stop words
stop_words = set(stopwords.words("english"))

# Remove stop words
filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]

print("Original Tokens:", words)
print("After Stop Word Removal:", filtered_words)

# Display available stop-word languages
print("Available Languages:", sorted(stopwords.fileids()))