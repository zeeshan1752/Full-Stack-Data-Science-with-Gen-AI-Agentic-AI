# Text Cleaning

import re

text = "<p>NLP is useful!!! In 2026, text is everywhere.</p>"

print("Original Text:", text)

# Remove HTML tags
text = re.sub(r"<[^>]*>", " ", text)

# Remove punctuation and unwanted characters
text = re.sub(r"[^A-Za-z0-9\s']", " ", text)

# Remove extra spaces
text = re.sub(r"\s+", " ", text)

# Remove leading and trailing spaces
text = text.strip()

# Convert text to lowercase
text = text.lower()

print("Cleaned Text:", text)