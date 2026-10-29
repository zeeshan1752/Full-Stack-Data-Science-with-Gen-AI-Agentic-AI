# Named Entity Recognition Using NLTK

import nltk
from nltk import Tree
from collections import Counter

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("maxent_ne_chunker")
nltk.download("maxent_ne_chunker_tab")
nltk.download("words")

# Sample text
text = """
Ada Lovelace worked on the Analytical Engine.
Charles Babbage designed the Analytical Engine.
Alan Turing worked in the United Kingdom.
Google is a technology company.
Microsoft is headquartered in Redmond.
Barack Obama was born in the United States.
"""

# Display original text
print("Original Text:")
print(text)

# Tokenize the text
tokens = nltk.word_tokenize(text)

print("\nTokens:")
print(tokens)

# Perform Part-of-Speech tagging
tagged_tokens = nltk.pos_tag(tokens)

print("\nPart-of-Speech Tags:")
for token, tag in tagged_tokens:
    print(f"{token:20} {tag}")

# Perform Named Entity Recognition
entity_tree = nltk.ne_chunk(tagged_tokens, binary=False)

print("\nNamed Entity Recognition Tree:")
print(entity_tree)

# Extract named entities
entities = []

for node in entity_tree:
    if isinstance(node, Tree):
        entity_name = " ".join(
            word for word, tag in node.leaves()
        )
        entity_label = node.label()

        entities.append((entity_name, entity_label))

# Display extracted entities
print("\nExtracted Named Entities:")
for entity_name, entity_label in entities:
    print(f"{entity_name:25} {entity_label}")

# Count entities by category
entity_counts = Counter(
    entity_label for entity_name, entity_label in entities
)

print("\nEntity Category Counts:")
for entity_label, count in entity_counts.items():
    print(f"{entity_label:20} {count}")

# Display unique entity names
unique_entities = sorted(
    set(entity_name for entity_name, entity_label in entities)
)

print("\nUnique Named Entities:")
for entity_name in unique_entities:
    print(entity_name)

# Group entities by category
entities_by_category = {}

for entity_name, entity_label in entities:
    if entity_label not in entities_by_category:
        entities_by_category[entity_label] = []

    entities_by_category[entity_label].append(entity_name)

print("\nEntities Grouped by Category:")
for entity_label, names in entities_by_category.items():
    print(f"\n{entity_label}:")

    for name in sorted(set(names)):
        print(" -", name)

# Display only person entities
print("\nPerson Entities:")
for entity_name, entity_label in entities:
    if entity_label == "PERSON":
        print(entity_name)

# Display organization entities
print("\nOrganization Entities:")
for entity_name, entity_label in entities:
    if entity_label == "ORGANIZATION":
        print(entity_name)

# Display location-related entities
print("\nLocation Entities:")
for entity_name, entity_label in entities:
    if entity_label in ["GPE", "LOCATION", "FACILITY"]:
        print(entity_name, ":", entity_label)

# Process a second sentence
sentence = "Satya Nadella leads Microsoft in the United States."

print("\nSecond Sentence:")
print(sentence)

sentence_tokens = nltk.word_tokenize(sentence)
sentence_tags = nltk.pos_tag(sentence_tokens)
sentence_tree = nltk.ne_chunk(sentence_tags, binary=False)

print("\nEntities in the Second Sentence:")
for node in sentence_tree:
    if isinstance(node, Tree):
        name = " ".join(word for word, tag in node.leaves())
        label = node.label()
        print(f"{name:25} {label}")

# Compare named entity recognition on different text
sentences = [
    "Ada Lovelace studied mathematics.",
    "Google operates in many countries.",
    "London is the capital of the United Kingdom.",
    "Apple develops software and electronic devices."
]

print("\nNamed Entity Recognition on Multiple Sentences:")

for sentence in sentences:
    print("\nSentence:", sentence)

    sentence_tokens = nltk.word_tokenize(sentence)
    sentence_tags = nltk.pos_tag(sentence_tokens)
    sentence_tree = nltk.ne_chunk(sentence_tags, binary=False)

    for node in sentence_tree:
        if isinstance(node, Tree):
            name = " ".join(word for word, tag in node.leaves())
            label = node.label()
            print(f"{name:25} {label}")

# Analyze the total number of detected entities
print("\nTotal Named Entities:", len(entities))

print("Unique Entity Names:", len(unique_entities))

# Display the most common entity categories
print("\nMost Common Entity Categories:")
for entity_label, count in entity_counts.most_common():
    print(f"{entity_label}: {count}")

# Exercise
print("\nPractice Exercises:")
print("1. Add your own paragraph and extract named entities.")
print("2. Compare entity recognition for people and organizations.")
print("3. Try sentences containing cities and countries.")
print("4. Check whether every proper noun is detected as an entity.")
print("5. Compare NLTK NER results with spaCy NER results.")
