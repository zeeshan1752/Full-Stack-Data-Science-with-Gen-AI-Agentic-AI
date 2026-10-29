# Tokenization using spaCy

import spacy
from collections import Counter

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = """
Natural Language Processing (NLP) is a branch of Artificial Intelligence.
It helps computers understand, process, and analyze human language.
spaCy is a popular Python library used for NLP tasks.
Tokenization is one of the basic steps in text preprocessing!
"""

# Process the text using spaCy
doc = nlp(text)

# Display the original text
print("Original Text:")
print(text)

# Sentence Tokenization
print("\nSentence Tokenization:")
for sentence in doc.sents:
    print(sentence.text)

# Word Tokenization
print("\nWord Tokenization:")
for token in doc:
    if not token.is_space:
        print(token.text)

# Store all tokens in a list
tokens = [token.text for token in doc if not token.is_space]

print("\nToken List:")
print(tokens)

# Count the total number of tokens
print("\nTotal Number of Tokens:")
print(len(tokens))

# Display tokens in lowercase
lowercase_tokens = [token.text.lower() for token in doc if not token.is_space]

print("\nLowercase Tokens:")
print(lowercase_tokens)

# Display alphabetic tokens only
alphabetic_tokens = [
    token.text for token in doc
    if token.is_alpha
]

print("\nAlphabetic Tokens:")
print(alphabetic_tokens)

# Display punctuation tokens
punctuation_tokens = [
    token.text for token in doc
    if token.is_punct
]

print("\nPunctuation Tokens:")
print(punctuation_tokens)

# Remove punctuation tokens
tokens_without_punctuation = [
    token.text for token in doc
    if not token.is_punct and not token.is_space
]

print("\nTokens Without Punctuation:")
print(tokens_without_punctuation)

# Display stop words
stop_words = [
    token.text for token in doc
    if token.is_stop
]

print("\nStop Words:")
print(stop_words)

# Remove stop words
tokens_without_stopwords = [
    token.text for token in doc
    if not token.is_stop and not token.is_space
]

print("\nTokens Without Stop Words:")
print(tokens_without_stopwords)

# Display lemmas
print("\nLemmatization:")
for token in doc:
    if not token.is_space:
        print(token.text, "->", token.lemma_)

# Display part-of-speech tags
print("\nPart-of-Speech Tags:")
for token in doc:
    if not token.is_space:
        print(token.text, "->", token.pos_)

# Display detailed token information
print("\nDetailed Token Information:")
for token in doc:
    if not token.is_space:
        print(
            "Text:", token.text,
            "| Lemma:", token.lemma_,
            "| POS:", token.pos_,
            "| Is Alphabetic:", token.is_alpha,
            "| Is Punctuation:", token.is_punct,
            "| Is Stop Word:", token.is_stop
        )

# Count token frequency
word_tokens = [
    token.text.lower() for token in doc
    if token.is_alpha
]

token_frequency = Counter(word_tokens)

print("\nToken Frequency:")
for word, frequency in token_frequency.items():
    print(word, ":", frequency)

# Display unique tokens
unique_tokens = sorted(set(word_tokens))

print("\nUnique Tokens:")
print(unique_tokens)

# Tokenize user-provided text
user_text = input("\nEnter text to tokenize: ")

user_doc = nlp(user_text)

print("\nUser Text Tokens:")
for token in user_doc:
    if not token.is_space:
        print(token.text)

# Display user text sentences
print("\nSentences in User Text:")
for sentence in user_doc.sents:
    print(sentence.text)