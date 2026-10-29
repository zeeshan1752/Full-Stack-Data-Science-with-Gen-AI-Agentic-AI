# Constituency Parsing Using NLTK

import nltk

# Define a Context-Free Grammar
grammar = nltk.CFG.fromstring("""
S -> NP VP

NP -> Det Adj N
NP -> Det N
NP -> Name

VP -> V NP
VP -> V

Det -> 'the' | 'a'
Adj -> 'quick' | 'lazy' | 'small'
N -> 'fox' | 'dog' | 'cat' | 'book'
Name -> 'ada' | 'john'

V -> 'sees' | 'writes' | 'likes'
""")

# Create a chart parser
parser = nltk.ChartParser(grammar)

# Define a sentence
sentence = "The quick fox sees a dog"

print("Original Sentence:")
print(sentence)

# Convert the sentence to lowercase tokens
tokens = sentence.lower().split()

print("\nTokens:")
print(tokens)

# Generate constituency parse trees
parses = list(parser.parse(tokens))

print("\nNumber of Parse Trees:")
print(len(parses))

# Display each parse tree
print("\nConstituency Parse Trees:")

for tree in parses:
    print(tree)

# Display the tree in a readable format
print("\nReadable Parse Tree:")

for tree in parses:
    tree.pretty_print()

# Parse another sentence
sentence2 = "Ada writes a book"
tokens2 = sentence2.lower().split()

print("\nSecond Sentence:")
print(sentence2)

parses2 = list(parser.parse(tokens2))

print("\nSecond Sentence Parse Trees:")
if parses2:
    for tree in parses2:
        print(tree)
else:
    print("No parse found for the second sentence.")

# Parse a sentence with a different noun phrase
sentence3 = "The small cat likes the dog"
tokens3 = sentence3.lower().split()

print("\nThird Sentence:")
print(sentence3)

parses3 = list(parser.parse(tokens3))

print("\nThird Sentence Parse Trees:")
if parses3:
    for tree in parses3:
        print(tree)
else:
    print("No parse found for the third sentence.")

# Compare valid and invalid sentences
sentences = [
    "The fox sees a dog",
    "Ada writes a book",
    "The lazy dog likes the cat",
    "The bird sees a dog",
    "John reads a book"
]

print("\nParsing Multiple Sentences:")

for text in sentences:
    print("\nSentence:", text)

    sentence_tokens = text.lower().split()
    sentence_parses = list(parser.parse(sentence_tokens))

    if sentence_parses:
        print("Parse found.")

        for tree in sentence_parses:
            print(tree)
    else:
        print("No parse found. The sentence may not match the grammar.")

# Display grammar productions
print("\nGrammar Productions:")

for production in grammar.productions():
    print(production)

# Display grammar categories
print("\nGrammar Categories:")
print("S    - Sentence")
print("NP   - Noun Phrase")
print("VP   - Verb Phrase")
print("Det  - Determiner")
print("Adj  - Adjective")
print("N    - Noun")
print("Name - Proper Name")
print("V    - Verb")

# Practice exercises
print("\nPractice Exercises:")
print("1. Add more nouns to the grammar.")
print("2. Add more verbs to the grammar.")
print("3. Add another adjective.")
print("4. Test a sentence that is not covered by the grammar.")
print("5. Observe how changing the grammar changes the parse results.")
