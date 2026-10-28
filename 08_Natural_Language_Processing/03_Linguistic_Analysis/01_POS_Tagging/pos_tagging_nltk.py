"""Illustrate token-level part-of-speech tagging with NLTK."""
import nltk


sentence = "Ada Lovelace wrote careful notes about analytical engines."
tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)

for token, tag in tagged_tokens:
    print(f"{token:15} {tag}")

# If NLTK reports missing data, consult https://www.nltk.org/data.html.
# Exercise: compare how changing a word's surrounding context changes its tag.
