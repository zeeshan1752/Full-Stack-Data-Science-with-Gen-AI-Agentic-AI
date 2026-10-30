# Chunking and Chinking

## 1. Introduction

Chunking is a shallow syntactic analysis technique used in Natural Language Processing (NLP). It groups part-of-speech-tagged tokens into meaningful grammatical phrases, such as noun phrases (NP), verb phrases (VP), and prepositional phrases (PP).

**Chinking** is the process of removing selected tokens or tags from a chunk based on specified rules.

Chunking and chinking are commonly demonstrated using POS-tagged text and rule-based grammars.

## 2. What Is Chunking?

Chunking identifies groups of related words without constructing the complete grammatical structure of a sentence.

For example:

```text
The quick brown fox jumps over the fence.
```

A chunking grammar might identify noun phrases such as:

```text
[The quick brown fox]
[the fence]
```

The exact chunks depend on the POS tags and grammar rules.

### Common Phrase Types

| Phrase | Meaning | Example |
|---|---|---|
| NP | Noun Phrase | the quick fox |
| VP | Verb Phrase | jumps quickly |
| PP | Prepositional Phrase | over the fence |
| ADJP | Adjective Phrase | very quick |
| ADVP | Adverb Phrase | extremely quickly |

These are common linguistic phrase types. The exact categories recognized depend on the grammar being used.

## 3. What Is Chinking?

Chinking removes selected tokens from a chunk according to a defined rule.

For example, suppose a grammar initially groups a sequence of tokens into a noun phrase. A chinking rule can exclude tokens with particular POS tags from that chunk.

In NLTK, chunk grammars use regular-expression patterns over POS tags. Chinking rules specify which matching tokens should be excluded from a chunk.

## 4. Chunking vs. Chinking

| Feature | Chunking | Chinking |
|---|---|---|
| Purpose | Groups tokens into shallow phrases | Removes selected tokens from a chunk |
| Operation | Adds chunks | Excludes matching tokens |
| Input | POS-tagged tokens | POS-tagged tokens and existing chunks |
| Rules | Chunk grammar patterns | Chinking patterns |
| Main result | Phrase-level groups | Chunks with selected tokens excluded |

## 5. Chunking Using NLTK

NLTK provides `RegexpParser` for creating rule-based chunk parsers.

### Installation

Install NLTK:

```bash
python -m pip install nltk
```

If tokenization or POS tagging reports a missing resource, consult the official [NLTK Data Guide](https://www.nltk.org/data.html) and install the named resource.

### Example: Basic Chunking

```python
import nltk

sentence = "The quick brown fox jumps over the fence."

tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
"""

chunk_parser = nltk.RegexpParser(grammar)
chunk_tree = chunk_parser.parse(tagged_tokens)

print("Original Sentence:")
print(sentence)

print("\nPOS-Tagged Tokens:")
print(tagged_tokens)

print("\nChunked Tree:")
print(chunk_tree)

print("\nReadable Chunk Tree:")
chunk_tree.pretty_print()
```

### Explanation

- `word_tokenize()` splits the sentence into tokens.
- `pos_tag()` assigns grammatical tags to the tokens.
- `RegexpParser()` creates a chunk parser from the grammar rules.
- `NP` identifies a noun phrase in the grammar.
- `<DT>?` allows an optional determiner.
- `<JJ>*` allows zero or more adjectives.
- `<NN.*>+` matches one or more noun tags beginning with `NN`.

The grammar is rule-based, so its results depend on the POS tags and patterns specified.

## 6. Example: Chunking and Chinking

```python
import nltk

sentence = "The quick brown fox jumps over the fence."

tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
        }<JJ>{
"""

chunk_parser = nltk.RegexpParser(grammar)
chunk_tree = chunk_parser.parse(tagged_tokens)

print("Sentence:")
print(sentence)

print("\nPOS Tags:")
print(tagged_tokens)

print("\nChunking and Chinking Result:")
print(chunk_tree)

chunk_tree.pretty_print()
```

In this grammar:

- `NP: {<DT>?<JJ>*<NN.*>+}` defines the noun-phrase chunking pattern.
- `}<JJ>{` is a chinking rule that excludes adjective-tagged tokens from a chunk when the rule matches.

The final result depends on the order of the rules and the actual POS tags produced by NLTK.

## 7. Trainer Lesson

The trainer's NLTK example has been adapted into the [Chunking and Chinking notebook](chunking_nltk.ipynb).

The notebook includes:

- A phrase grammar
- A separate chinking rule
- Rule-based chunking demonstrations

The notebook does not run or download NLTK data automatically. Any required resources must be installed separately.

## 8. Syntactic Chunking vs. Long-Text Chunking

The word *chunking* is used in two different contexts in NLP.

### Syntactic Chunking

Syntactic chunking groups POS-tagged tokens into shallow grammatical phrases.

Examples include:

- Noun phrases
- Verb phrases
- Prepositional phrases

This is the focus of the NLTK lesson in this folder.

### Long-Text Chunking

Long-text chunking divides a large text into smaller pieces that fit within a model's token limit.

It is used in workflows involving language models, document processing, and retrieval-augmented generation (RAG).

The GPT-2 demonstration for long-text chunking is available in the [Transformer supplement](../../05_Attention_And_Transformers/03_GPT2_And_HF_Demos/README.md).

These two meanings are related only through the general idea of dividing something into smaller units; their methods and goals are different.

## 9. Limitations of Rule-Based Chunking

- **POS-tag dependence:** Incorrect POS tags can lead to incorrect chunks.
- **Grammar limitations:** The parser only recognizes patterns specified by its rules.
- **Ambiguity:** A phrase may be interpreted differently depending on context.
- **Shallow analysis:** Chunking does not provide a complete sentence parse.
- **Rule maintenance:** More complex text may require additional grammar rules.

## 10. Chunking vs. Constituency Parsing vs. Dependency Parsing

| Feature | Chunking | Constituency Parsing | Dependency Parsing |
|---|---|---|---|
| Main goal | Identify shallow phrases | Build a hierarchical phrase structure | Identify head-dependent relationships |
| Output | Chunks | Parse tree | Dependency tree |
| Typical representation | NP chunks | `S`, `NP`, `VP` | `ROOT`, `nsubj`, `obj` |
| Analysis depth | Shallow | Full phrase structure, according to the grammar | Word-level grammatical relationships |
| Example tool in this repository | NLTK `RegexpParser` | NLTK CFG parser | spaCy dependency parser |

For full sentence structure, study constituency parsing and dependency parsing.

## 11. Common Mistakes

- Confusing syntactic chunking with long-text chunking.
- Forgetting to POS-tag tokens before applying a POS-based chunk grammar.
- Assuming a chunk grammar recognizes every valid phrase.
- Writing a chinking pattern that does not match the intended POS tags.
- Treating a chunk tree as a complete sentence parse.
- Forgetting to install required NLTK resources.

## 12. Points to Remember

- Chunking is a shallow syntactic analysis technique.
- Chunking groups POS-tagged tokens into phrases.
- Chinking removes selected tokens from chunks using rules.
- NLTK provides `RegexpParser` for rule-based chunking.
- The results depend on POS tags and grammar rules.
- Syntactic chunking and long-text chunking are different concepts.
- Constituency and dependency parsing provide different views of sentence structure.

## 13. Related Topics

- [Part-of-Speech Tagging](../01_POS_Tagging/README.md)
- [Named Entity Recognition](../02_NER/README.md)
- [Parsing](../03_Parsing/README.md)
- [Transformer Supplement: GPT-2 and Hugging Face Demos](../../05_Attention_And_Transformers/03_GPT2_And_HF_Demos/README.md)

## 14. References

- [NLTK Official Documentation](https://www.nltk.org/)
- [NLTK Data Guide](https://www.nltk.org/data.html)
- [NLTK Book: Extracting Information from Text](https://www.nltk.org/book/ch07.html)
