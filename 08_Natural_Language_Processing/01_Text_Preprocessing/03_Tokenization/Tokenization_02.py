"""Tokenize a paragraph into sentences and word tokens using NLTK.

If tokenization raises LookupError, install the required data in this Python
environment: python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
"""
import nltk

paragraph = """AI, machine learning and deep learning are common terms in enterprise IT
and sometimes used interchangeably, especially by companies in their marketing materials.
But there are distinctions. AI refers to the simulation of human intelligence by machines.
Machine learning enables software applications to learn patterns from data, while deep
learning uses multi-layer neural networks."""

try:
    sentences = nltk.sent_tokenize(paragraph)
    words = nltk.word_tokenize(paragraph)
except LookupError as exc:
    raise SystemExit(
        "Required NLTK tokenizer data is missing. Run the download command "
        "in this file's docstring, then run the script again."
    ) from exc

print("Sentence tokens:")
for index, sentence in enumerate(sentences, start=1):
    print(f"{index}. {sentence}")

print("\nWord tokens:")
print(words)
print(f"\nTotal word tokens, including punctuation: {len(words)}")
