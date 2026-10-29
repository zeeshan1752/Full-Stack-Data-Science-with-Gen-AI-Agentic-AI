# Text Cleaning Using Python Regular Expressions

import re
from pathlib import Path

# Locate the shared NLP sample text file
DATA_FILE = Path(__file__).resolve().parents[2] / "01_Preprocessing" / "sample_texts.txt"

# Read text samples from the shared data file
samples = [
    sample.strip()
    for sample in DATA_FILE.read_text(encoding="utf-8").splitlines()
    if sample.strip()
]

# Display original text samples
print("Original Text Samples:")
for index, sample in enumerate(samples, start=1):
    print(f"{index}. {sample}")

# Convert text to lowercase
print("\nLowercase Text:")
for sample in samples:
    print(sample.lower())

# Remove punctuation and special characters
print("\nText Without Punctuation:")
for sample in samples:
    cleaned_text = re.sub(r"[^\w\s]", " ", sample)
    print(cleaned_text)

# Remove digits
print("\nText Without Digits:")
for sample in samples:
    cleaned_text = re.sub(r"\d+", "", sample)
    print(cleaned_text)

# Extract all numbers
print("\nExtracted Numbers:")
for sample in samples:
    numbers = re.findall(r"\d+", sample)
    print(numbers)

# Extract alphabetic words
print("\nExtracted Words:")
for sample in samples:
    words = re.findall(r"[A-Za-z]+", sample)
    print(words)

# Replace multiple spaces with a single space
print("\nNormalized Whitespace:")
for sample in samples:
    cleaned_text = re.sub(r"\s+", " ", sample).strip()
    print(cleaned_text)

# Remove email addresses
print("\nText Without Email Addresses:")
for sample in samples:
    cleaned_text = re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "",
        sample
    )
    print(re.sub(r"\s+", " ", cleaned_text).strip())

# Extract email addresses
print("\nExtracted Email Addresses:")
for sample in samples:
    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        sample
    )
    print(emails)

# Extract hashtags
print("\nExtracted Hashtags:")
for sample in samples:
    hashtags = re.findall(r"#[A-Za-z0-9_]+", sample)
    print(hashtags)

# Remove hashtags
print("\nText Without Hashtags:")
for sample in samples:
    cleaned_text = re.sub(r"#[A-Za-z0-9_]+", "", sample)
    print(re.sub(r"\s+", " ", cleaned_text).strip())

# Replace URLs with a placeholder
print("\nURLs Replaced With Placeholder:")
for sample in samples:
    cleaned_text = re.sub(
        r"https?://\S+|www\.\S+",
        "[URL]",
        sample
    )
    print(cleaned_text)

# Extract URLs
print("\nExtracted URLs:")
for sample in samples:
    urls = re.findall(
        r"https?://\S+|www\.\S+",
        sample
    )
    print(urls)

# Remove repeated punctuation
print("\nText Without Repeated Punctuation:")
for sample in samples:
    cleaned_text = re.sub(r"([!?.,])\1+", r"\1", sample)
    print(cleaned_text)

# Remove text enclosed in parentheses
print("\nText Without Parenthetical Content:")
for sample in samples:
    cleaned_text = re.sub(r"\([^)]*\)", "", sample)
    print(re.sub(r"\s+", " ", cleaned_text).strip())

# Apply complete text normalization
print("\nFully Normalized Text:")
for sample in samples:
    cleaned_text = sample.lower()
    cleaned_text = re.sub(r"https?://\S+|www\.\S+", " ", cleaned_text)
    cleaned_text = re.sub(r"[^\w\s]", " ", cleaned_text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()

    print(cleaned_text)

# Display the number of samples processed
print("\nTotal Samples Processed:", len(samples))
