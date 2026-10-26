"""Sentence and word tokenization with NLTK.

If tokenization raises LookupError, install the required data in this Python
environment: python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
"""
import nltk

paragraph = """I have three visions for India. In 3000 years of our history, people from all over
the world have come and invaded us, captured our lands, conquered our minds.
From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
the French, the Dutch, all of them came and looted us, took over what was ours.
Yet we have not done this to any other nation. We have not conquered anyone.
We have not grabbed their land, their culture, their history and tried to enforce
our way of life on them. Why? Because we respect the freedom of others.
That is why my first vision is that of freedom."""

try:
    sentences = nltk.sent_tokenize(paragraph)
    words = nltk.word_tokenize(paragraph)
except LookupError as exc:
    raise SystemExit(
        "Required NLTK tokenizer data is missing. Run the download command "
        "in this file's docstring, then run the script again."
    ) from exc

print(f"Number of sentences: {len(sentences)}")
print("\nSentences:")
for index, sentence in enumerate(sentences, start=1):
    print(f"{index}. {sentence}")

print(f"\nNumber of word tokens (including punctuation): {len(words)}")
print(words)
