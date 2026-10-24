"""Create a basic named-entity tree using NLTK."""
import nltk


sentence = "Ada Lovelace worked in London and wrote about the Analytical Engine."
tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)
entity_tree = nltk.ne_chunk(tagged_tokens, binary=False)

print(entity_tree)

# NLTK may request model or corpus data. See https://www.nltk.org/data.html.
# Exercise: compare the entity types found in two sentences about organizations.
