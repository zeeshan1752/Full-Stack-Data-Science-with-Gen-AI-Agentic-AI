"""Demonstrate common regular-expression operations for NLP."""

import re


# Find numbers in text
text = "I have 2 notebooks and 15 pens."
numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

# Search for a word
text = "I am learning Python for NLP."
match = re.search(r"Python", text)

if match:
    print("Found word:", match.group())
    print("Start index:", match.start())
    print("End index:", match.end())

# Normalize repeated whitespace
text = "Python     is   useful for NLP."
cleaned_text = re.sub(r"\s+", " ", text).strip()
print("Normalized whitespace:", cleaned_text)

# Extract email-like patterns
text = "Contact support@example.com or team@example.org."
email_pattern = r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"
emails = re.findall(email_pattern, text)
print("Email-like patterns:", emails)

# Split text using commas, semicolons, or whitespace
text = "apple, banana; orange  grape"
items = re.split(r"[,;\s]+", text.strip())
print("Split items:", items)

# Capture date components
text = "Date: 2026-10-26"
date_match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)

if date_match:
    print("Year:", date_match.group(1))
    print("Month:", date_match.group(2))
    print("Day:", date_match.group(3))

# Basic NLP cleaning example
from html import unescape

def clean_text(text):
    """Decode HTML entities and remove simple markup, URLs, and extra spaces."""
    text = unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


raw_text = "<p>Learn NLP at https://example.com   today!</p>"
print("Cleaned text:", clean_text(raw_text))
