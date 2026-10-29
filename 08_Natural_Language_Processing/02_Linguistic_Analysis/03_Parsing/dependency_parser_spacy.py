# Dependency Parsing Using spaCy

import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define a sentence
sentence = "The quick fox jumps over the dog."

# Display the original sentence
print("Original Sentence:")
print(sentence)

# Process the sentence
doc = nlp(sentence)

# Display tokens
print("\nTokens:")
for token in doc:
    print(token.text)

# Display dependency relations
print("\nDependency Relations:")
print(f"{'Word':15} {'Head':15} {'Dependency':20}")

for token in doc:
    print(f"{token.text:15} {token.head.text:15} {token.dep_:20}")

# Display detailed token information
print("\nDetailed Token Information:")

for token in doc:
    print("Token:", token.text)
    print("Lemma:", token.lemma_)
    print("Part of Speech:", token.pos_)
    print("Dependency Relation:", token.dep_)
    print("Head Word:", token.head.text)
    print("Is Root:", token.head == token)
    print("-" * 40)

# Display the root word
print("\nRoot Word:")

for token in doc:
    if token.dep_ == "ROOT":
        print(token.text)

# Display the children of each token
print("\nChildren of Each Token:")

for token in doc:
    children = [child.text for child in token.children]
    print(token.text, ":", children)

# Display the ancestors of each token
print("\nAncestors of Each Token:")

for token in doc:
    ancestors = [ancestor.text for ancestor in token.ancestors]
    print(token.text, ":", ancestors)

# Display subject-related tokens
print("\nSubject Relations:")

for token in doc:
    if token.dep_ in ["nsubj", "nsubjpass", "csubj"]:
        print("Subject:", token.text)
        print("Related Verb:", token.head.text)

# Display object-related tokens
print("\nObject Relations:")

for token in doc:
    if token.dep_ in ["dobj", "obj", "pobj", "iobj"]:
        print("Object:", token.text)
        print("Head Word:", token.head.text)
        print("Dependency:", token.dep_)

# Display modifiers
print("\nModifiers:")

for token in doc:
    if token.dep_ in ["amod", "advmod", "det", "compound"]:
        print("Modifier:", token.text)
        print("Modified Word:", token.head.text)
        print("Dependency:", token.dep_)

# Display prepositions and their relationships
print("\nPrepositional Relationships:")

for token in doc:
    if token.pos_ == "ADP":
        print("Preposition:", token.text)
        print("Head Word:", token.head.text)

        for child in token.children:
            print("Child:", child.text, "Dependency:", child.dep_)

# Analyze another sentence
sentence2 = "The intelligent student solved the difficult problem."

print("\nSecond Sentence:")
print(sentence2)

doc2 = nlp(sentence2)

print("\nDependency Relations:")
for token in doc2:
    print(
        f"Word: {token.text:15}",
        f"Head: {token.head.text:15}",
        f"Relation: {token.dep_}"
    )

# Analyze a sentence with a direct object
sentence3 = "Ada writes a letter."

print("\nThird Sentence:")
print(sentence3)

doc3 = nlp(sentence3)

for token in doc3:
    print(token.text, "->", token.head.text, ":", token.dep_)

# Analyze multiple sentences
sentences = [
    "The cat sleeps.",
    "John reads a book.",
    "The dog runs quickly.",
    "The teacher explains the lesson.",
    "The bird flies over the house."
]

print("\nDependency Parsing on Multiple Sentences:")

for sentence in sentences:
    print("\nSentence:", sentence)

    sentence_doc = nlp(sentence)

    for token in sentence_doc:
        print(
            f"{token.text:15} "
            f"{token.head.text:15} "
            f"{token.dep_:20}"
        )

# Display common dependency labels
print("\nCommon Dependency Labels:")
print("ROOT   - Main root of the sentence")
print("nsubj  - Nominal subject")
print("obj    - Object")
print("dobj   - Direct object in older label schemes")
print("iobj   - Indirect object")
print("amod   - Adjectival modifier")
print("advmod - Adverbial modifier")
print("det    - Determiner")
print("prep   - Prepositional modifier in older label schemes")
print("pobj   - Object of a preposition in older label schemes")
print("aux    - Auxiliary verb")
print("attr   - Attribute")
print("conj   - Conjunct")
print("cc     - Coordinating conjunction")
print("punct  - Punctuation")

# Count dependency labels
dependency_counts = {}

for token in doc:
    if token.dep_ not in dependency_counts:
        dependency_counts[token.dep_] = 0

    dependency_counts[token.dep_] += 1

print("\nDependency Label Frequency:")

for relation, count in dependency_counts.items():
    print(relation, ":", count)

# Display the number of tokens
print("\nSentence Statistics:")
print("Total Tokens:", len(doc))
print("Total Dependency Relations:", len(doc))

# Practice exercises
print("\nPractice Exercises:")
print("1. Change the sentence and observe the dependency relations.")
print("2. Identify the subject and root of each sentence.")
print("3. Find the head word of every token.")
print("4. Compare direct objects and indirect objects.")
print("5. Observe how adjectives modify nouns.")
print("6. Compare dependency parsing with constituency parsing.")
