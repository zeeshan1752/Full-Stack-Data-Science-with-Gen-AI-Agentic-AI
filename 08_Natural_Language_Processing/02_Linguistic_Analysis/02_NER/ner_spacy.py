# Named Entity Recognition Using spaCy

import spacy
from collections import Counter

# Load the English language model
nlp = spacy.load("en_core_web_sm")

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

# Process the text with spaCy
doc = nlp(text)

# Display tokens
print("\nTokens:")
for token in doc:
    print(token.text)

# Display named entities
print("\nNamed Entities:")
for entity in doc.ents:
    print(entity.text, ":", entity.label_)

# Display entity text and descriptions
print("\nEntity Details:")
for entity in doc.ents:
    print("Entity:", entity.text)
    print("Label:", entity.label_)
    print("Description:", spacy.explain(entity.label_))
    print("-" * 40)

# Count entity labels
entity_counts = Counter(
    entity.label_ for entity in doc.ents
)

print("\nEntity Category Counts:")
for label, count in entity_counts.items():
    print(label, ":", count)

# Display unique entity names
unique_entities = sorted(
    set(entity.text for entity in doc.ents)
)

print("\nUnique Named Entities:")
for name in unique_entities:
    print(name)

# Group entities by category
entities_by_category = {}

for entity in doc.ents:
    if entity.label_ not in entities_by_category:
        entities_by_category[entity.label_] = []

    entities_by_category[entity.label_].append(entity.text)

print("\nEntities Grouped by Category:")
for label, names in entities_by_category.items():
    print("\nCategory:", label)

    for name in sorted(set(names)):
        print("-", name)

# Display person entities
print("\nPerson Entities:")
for entity in doc.ents:
    if entity.label_ == "PERSON":
        print(entity.text)

# Display organization entities
print("\nOrganization Entities:")
for entity in doc.ents:
    if entity.label_ == "ORG":
        print(entity.text)

# Display location-related entities
print("\nLocation Entities:")
for entity in doc.ents:
    if entity.label_ in ["GPE", "LOC", "FAC"]:
        print(entity.text, ":", entity.label_)

# Display entity character positions
print("\nEntity Character Positions:")
for entity in doc.ents:
    print("Entity:", entity.text)
    print("Start Character:", entity.start_char)
    print("End Character:", entity.end_char)
    print("Label:", entity.label_)
    print("-" * 40)

# Display entities sentence by sentence
print("\nSentence-Level Entity Analysis:")

for sentence in doc.sents:
    print("\nSentence:", sentence.text)

    if sentence.ents:
        for entity in sentence.ents:
            print(entity.text, ":", entity.label_)
    else:
        print("No named entities detected.")

# Process a second sentence
sentence = "Satya Nadella leads Microsoft in the United States."

print("\nSecond Sentence:")
print(sentence)

doc2 = nlp(sentence)

print("\nEntities in the Second Sentence:")
for entity in doc2.ents:
    print(entity.text, ":", entity.label_)

# Process multiple sentences
sentences = [
    "Ada Lovelace studied mathematics.",
    "Google operates in many countries.",
    "London is the capital of the United Kingdom.",
    "Apple develops software and electronic devices.",
    "Elon Musk founded SpaceX.",
    "The Eiffel Tower is located in Paris, France."
]

print("\nNamed Entity Recognition on Multiple Sentences:")

for sentence in sentences:
    print("\nSentence:", sentence)

    sentence_doc = nlp(sentence)

    if sentence_doc.ents:
        for entity in sentence_doc.ents:
            print(entity.text, ":", entity.label_)
    else:
        print("No named entities detected.")

# Count entities in the multiple-sentence examples
all_entities = []

for sentence in sentences:
    sentence_doc = nlp(sentence)

    for entity in sentence_doc.ents:
        all_entities.append((entity.text, entity.label_))

print("\nAll Entities from Multiple Sentences:")
for name, label in all_entities:
    print(name, ":", label)

# Count entity categories across the multiple-sentence examples
all_entity_counts = Counter(
    label for name, label in all_entities
)

print("\nEntity Category Frequency:")
for label, count in all_entity_counts.most_common():
    print(label, ":", count)

# Find unique entities across the multiple-sentence examples
all_unique_entities = sorted(
    set(name for name, label in all_entities)
)

print("\nUnique Entities Across Multiple Sentences:")
for name in all_unique_entities:
    print(name)

# Compare the same text with and without named entities
comparison_text = "Apple announced a new product in California."

print("\nEntity Recognition Example:")
print(comparison_text)

comparison_doc = nlp(comparison_text)

print("\nDetected Entities:")
for entity in comparison_doc.ents:
    print(entity.text, ":", entity.label_)

# Display common spaCy entity labels
print("\nCommon spaCy Entity Labels:")
print("PERSON - People, including fictional characters")
print("ORG    - Organizations")
print("GPE    - Countries, cities, and states")
print("LOC    - Non-GPE locations")
print("FAC    - Facilities and infrastructure")
print("DATE   - Dates or periods")
print("TIME   - Times smaller than a day")
print("MONEY  - Monetary values")
print("PERCENT - Percentage values")
print("PRODUCT - Products")
print("EVENT  - Named events")
print("WORK_OF_ART - Titles of creative works")

# Display total entity statistics for the original text
print("\nOriginal Text Statistics:")
print("Total Entities:", len(doc.ents))
print("Unique Entity Names:", len(unique_entities))
print("Entity Categories:", len(entity_counts))

# Display total entity statistics for the multiple-sentence examples
print("\nMultiple-Sentence Statistics:")
print("Total Entities:", len(all_entities))
print("Unique Entity Names:", len(all_unique_entities))
print("Entity Categories:", len(all_entity_counts))

# Practice exercises
print("\nPractice Exercises:")
print("1. Add your own paragraph and extract named entities.")
print("2. Compare entity recognition for people and organizations.")
print("3. Try sentences containing cities and countries.")
print("4. Test the model with dates, money, and percentages.")
print("5. Check whether every proper noun is detected as an entity.")
print("6. Compare the output of spaCy NER with NLTK NER.")
print("7. Investigate an entity that spaCy labels incorrectly.")
