# Token-Level Part-of-Speech Tagging with NLTK

import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter

# Download required NLTK resources if they are missing
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

# Define a sentence
sentence = "Ada Lovelace wrote careful notes about analytical engines."

# Tokenize the sentence
tokens = word_tokenize(sentence)

print("Original Sentence:")
print(sentence)

print("\nTokens:")
print(tokens)

# Perform POS tagging
tagged_tokens = pos_tag(tokens)

print("\nPart-of-Speech Tags:")
for token, tag in tagged_tokens:
    print(f"{token:15} {tag}")

# Display token and tag in a structured format
print("\nToken-Level POS Tagging:")
print(f"{'Token':15} {'POS Tag':15}")
print("-" * 30)

for token, tag in tagged_tokens:
    print(f"{token:15} {tag:15}")

# Count the frequency of each POS tag
tag_counts = Counter(tag for token, tag in tagged_tokens)

print("\nPOS Tag Frequency:")
for tag, count in tag_counts.items():
    print(f"{tag:10} {count}")

# Tag another sentence
sentence2 = "The intelligent student solved the difficult problem."

tokens2 = word_tokenize(sentence2)
tagged_tokens2 = pos_tag(tokens2)

print("\nSecond Sentence:")
print(sentence2)

print("\nPOS Tags:")
for token, tag in tagged_tokens2:
    print(f"{token:15} {tag}")

# Compare the tags of the word 'book' in different contexts
sentences = [
    "I read a book yesterday.",
    "Please book a ticket today."
]

print("\nContext-Based POS Tagging:")
for text in sentences:
    words = word_tokenize(text)
    tags = pos_tag(words)

    print(f"\nSentence: {text}")
    for token, tag in tags:
        if token.lower() == "book":
            print(f"Word: {token}, POS Tag: {tag}")

# Display common POS tags
print("\nCommon POS Tag Meanings:")
print("NN  - Noun, singular")
print("NNS - Noun, plural")
print("NNP - Proper noun, singular")
print("VB  - Verb, base form")
print("VBD - Verb, past tense")
print("VBG - Verb, gerund or present participle")
print("JJ  - Adjective")
print("RB  - Adverb")
print("DT  - Determiner")
print("IN  - Preposition or subordinating conjunction")
print("PRP - Personal pronoun")

# Exercise: change the context and observe how the POS tag changes
print("\nExercise:")
print("1. Compare 'I read a book' with 'Please book a ticket'.")
print("2. Try changing 'careful notes' to 'carefully written notes'.")
print("3. Observe how the POS tags change with the sentence context.")