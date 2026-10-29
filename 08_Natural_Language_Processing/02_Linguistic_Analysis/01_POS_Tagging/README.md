# Part-of-Speech Tagging (POS Tagging)

## 1. Introduction

**Part-of-Speech (POS) Tagging** is an NLP technique used to assign a grammatical category to each word or token in a sentence based on its usage and context.

These grammatical categories include nouns, verbs, adjectives, adverbs, pronouns, prepositions, and conjunctions.

For example, consider the sentence:

> Ada Lovelace wrote careful notes about analytical engines.

Each word has a grammatical role:

| Token | POS Tag | Grammatical Category |
|---|---|---|
| Ada | NNP | Proper noun |
| Lovelace | NNP | Proper noun |
| wrote | VBD | Verb, past tense |
| careful | JJ | Adjective |
| notes | NNS | Plural noun |
| about | IN | Preposition |
| analytical | JJ | Adjective |
| engines | NNS | Plural noun |
| . | . | Sentence-ending punctuation |

The exact tags returned may vary depending on the model, its version, and the surrounding text.

## 2. Why Do We Need POS Tagging?

POS tagging helps computers analyze the grammatical structure of natural language.

A sentence contains different types of words, and a word's grammatical role can change depending on its context.

Consider the word `book`:

**Example 1: Noun**

```text
I read a book yesterday.
```

Here, `book` refers to a thing, so it functions as a noun.

**Example 2: Verb**

```text
Please book a ticket today.
```

Here, `book` describes an action, so it functions as a verb.

POS tagging helps identify these differences.

### Main Uses

- Text analysis and linguistic processing
- Named Entity Recognition (NER) pipelines
- Syntactic analysis and parsing
- Information extraction
- Question-answering systems
- Text preprocessing for selected NLP tasks
- Grammar analysis and language-learning applications

POS tagging is useful in many NLP pipelines, but not every NLP task requires it.

## 3. Important POS Categories

The following table lists common English grammatical categories.

| Category | Description | Examples |
|---|---|---|
| Noun | Names a person, place, object, or concept | student, city, book |
| Verb | Expresses an action or state | write, run, is |
| Adjective | Describes a noun or pronoun | careful, intelligent, large |
| Adverb | Modifies a verb, adjective, or another adverb | quickly, very, carefully |
| Pronoun | Replaces or refers to a noun phrase | he, she, they, it |
| Determiner | Specifies or limits a noun | the, a, an, this |
| Preposition | Expresses relationships such as location or time | in, on, under, about |
| Conjunction | Connects words, phrases, or clauses | and, but, because |
| Interjection | Expresses an emotion or reaction | wow, oh, hey |
| Numeral | Expresses a number or numerical concept | three, ten, first |

These are broad grammatical categories. A tagger's output depends on the tag set it uses, so its labels may be more specific than these categories.

## 4. Common NLTK POS Tags

NLTK's `nltk.pos_tag()` commonly uses the Penn Treebank tag set for English.

| Tag | Meaning | Example |
|---|---|---|
| `CC` | Coordinating conjunction | and, but |
| `CD` | Cardinal number | one, 25 |
| `DT` | Determiner | the, a |
| `EX` | Existential there | there |
| `IN` | Preposition or subordinating conjunction | in, about, because |
| `JJ` | Adjective | careful, large |
| `JJR` | Comparative adjective | larger, faster |
| `JJS` | Superlative adjective | largest, fastest |
| `MD` | Modal verb | can, should |
| `NN` | Singular noun | book, engine |
| `NNS` | Plural noun | books, engines |
| `NNP` | Singular proper noun | Ada, London |
| `NNPS` | Plural proper noun | Americans |
| `PDT` | Predeterminer | all, both |
| `POS` | Possessive ending | 's |
| `PRP` | Personal pronoun | I, you, they |
| `PRP$` | Possessive pronoun or determiner | my, your, their |
| `RB` | Adverb | quickly, very |
| `RBR` | Comparative adverb | faster |
| `RBS` | Superlative adverb | fastest |
| `RP` | Particle | up, off |
| `TO` | The word `to` | to |
| `UH` | Interjection | oh, wow |
| `VB` | Verb, base form | write, run |
| `VBD` | Verb, past tense | wrote, walked |
| `VBG` | Verb, gerund or present participle | writing, running |
| `VBN` | Verb, past participle | written, eaten |
| `VBP` | Verb, non-third-person singular present | write, walk |
| `VBZ` | Verb, third-person singular present | writes, walks |
| `WDT` | Wh-determiner | which, that |
| `WP` | Wh-pronoun | who, what |
| `WP$` | Possessive wh-pronoun | whose |
| `WRB` | Wh-adverb | where, when |
| `.` | Sentence-ending punctuation | . |
| `,` | Comma | , |

**Note:** This table describes common Penn Treebank tags. Other languages and POS-tagging models may use different tag sets.

## 5. How POS Tagging Works

A POS-tagging pipeline typically includes the following steps:

1. **Input text:** Provide a sentence or paragraph.
2. **Tokenization:** Split the text into tokens.
3. **Context analysis:** Use the surrounding words and learned language patterns.
4. **Tag prediction:** Assign a grammatical tag to each token.
5. **Output:** Return token-tag pairs for further analysis.

For example:

```text
Sentence:
The intelligent student reads books.

Tokens:
The
intelligent
student
reads
books
.
```

A tagger might produce:

```text
The          DT
intelligent  JJ
student      NN
reads        VBZ
books        NNS
.            .
```

The tags are predictions made by the model. They are not guaranteed to be correct for every sentence.

## 6. POS Tagging Using NLTK

NLTK is a Python library for natural language processing. It provides tokenization, POS tagging, corpus access, and many other NLP utilities.

### Installation

Install NLTK using:

```bash
python -m pip install nltk
```

If NLTK reports missing resources, consult the official [NLTK Data Guide](https://www.nltk.org/data.html).

The required resource names can depend on the NLTK version.

### Example 1: Basic POS Tagging

```python
import nltk

sentence = "Ada Lovelace wrote careful notes about analytical engines."

tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)

print("Original Sentence:")
print(sentence)

print("\nPOS Tagged Tokens:")

for token, tag in tagged_tokens:
    print(f"{token:15} {tag}")
```

### Explanation

- `nltk.word_tokenize(sentence)` splits the sentence into tokens.
- `nltk.pos_tag(tokens)` assigns a POS tag to each token.
- Each returned pair contains a token and its predicted tag.
- The formatted print statement aligns the output into columns.

The exact output can depend on the installed NLTK resources and model version.

### Example 2: POS Tagging with Token and Tag Columns

```python
import nltk

sentence = "The intelligent student solved the difficult problem."

tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)

print(f"{'Token':20} {'POS Tag':15}")
print("-" * 35)

for token, tag in tagged_tokens:
    print(f"{token:20} {tag:15}")
```

This format makes the relationship between each token and its predicted grammatical tag easier to read.

### Example 3: Count POS Tags

POS-tag counts can provide a simple overview of the grammatical categories in a sentence.

```python
import nltk
from collections import Counter

sentence = "The intelligent student solved the difficult problem."

tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)

tag_counts = Counter(tag for token, tag in tagged_tokens)

print("POS Tag Frequency:")

for tag, count in tag_counts.items():
    print(f"{tag}: {count}")
```

`Counter` counts how many times each tag appears in the output.

For instance, if a sentence contains several adjectives, the `JJ` tag may occur multiple times. Punctuation may also appear as a tag.

### Example 4: Compare a Word in Different Contexts

```python
import nltk

sentences = [
    "I read a book yesterday.",
    "Please book a ticket today."
]

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged_tokens = nltk.pos_tag(tokens)

    print("\nSentence:", sentence)

    for token, tag in tagged_tokens:
        if token.lower() == "book":
            print("Token:", token)
            print("POS Tag:", tag)
```

In the first sentence, `book` functions as a noun. In the second, it functions as a verb.

This example illustrates why context matters when predicting grammatical categories. The exact model output should still be checked rather than assumed.

## 7. Understanding the Output

Consider a possible output for the sentence:

```text
Ada Lovelace wrote careful notes.
```

| Token | Tag | Interpretation |
|---|---|---|
| Ada | `NNP` | Singular proper noun |
| Lovelace | `NNP` | Singular proper noun |
| wrote | `VBD` | Past-tense verb |
| careful | `JJ` | Adjective |
| notes | `NNS` | Plural noun |
| . | `.` | Sentence-ending punctuation |

### What Do the Tags Tell Us?

- `NNP` identifies a proper noun under the Penn Treebank tag set.
- `VBD` indicates a past-tense verb.
- `JJ` indicates an adjective.
- `NNS` indicates a plural noun.
- `.` identifies sentence-ending punctuation.

These labels describe grammatical categories rather than the full meaning of the sentence.

## 8. POS Tagging and Context

A word does not always have the same grammatical role in every sentence.

Consider these examples:

| Sentence | Word | Possible grammatical role |
|---|---|---|
| I read a book. | book | Noun |
| Please book a room. | book | Verb |
| They watch television. | watch | Verb |
| My watch is new. | watch | Noun |
| The water is clean. | clean | Adjective |
| Please clean the room. | clean | Verb |

A POS tagger uses learned patterns and surrounding context to predict a tag.

However, context can be ambiguous. A statistical tagger may misclassify unfamiliar, unusual, or grammatically complex sentences.

## 9. POS Tagging vs. Tokenization

Tokenization and POS tagging are related but different tasks.

| Feature | Tokenization | POS Tagging |
|---|---|---|
| Purpose | Splits text into tokens | Assigns grammatical labels to tokens |
| Input | Text | Usually a sequence of tokens |
| Output | Tokens | Token-tag pairs |
| Example | `["The", "cat", "runs", "."]` | `[("The", "DT"), ("cat", "NN"), ...]` |
| Uses grammatical context | Not necessarily | Yes, in the tagger's predictions |

Tokenization is often performed before POS tagging because the tagger needs tokens to label.

## 10. POS Tagging vs. Named Entity Recognition

POS tagging and Named Entity Recognition (NER) identify different types of information.

| Feature | POS Tagging | NER |
|---|---|---|
| Main purpose | Identify grammatical categories | Identify named entities |
| Output | Noun, verb, adjective, etc. | Person, organization, location, etc. |
| Example | `Ada → NNP` | `Ada Lovelace → PERSON` |
| Typical unit | Individual tokens | Often a token or a multi-token span |
| Main focus | Grammar | Entity identification |

For example, POS tagging may identify `Ada` as a proper noun, while NER may identify `Ada Lovelace` as a person.

POS tagging does not itself establish that a proper noun refers to a real person, organization, or location.

See the [Named Entity Recognition notes](../02_NER/README.md).

## 11. Applications of POS Tagging

### Text Analysis

POS tags help examine the grammatical composition of text.

### Syntactic Parsing

POS tags can contribute to identifying grammatical relationships and sentence structure.

### Information Extraction

Grammatical information can help some systems identify candidate phrases and relationships.

### Named Entity Recognition Pipelines

POS features may support certain NER systems, although modern NER models can also work directly with tokens and contextual representations.

### Question Answering

POS information can help identify verbs, nouns, and other grammatical patterns in a question.

### Linguistic Research

POS tagging can support studies of word usage, sentence construction, and grammatical patterns.

These are potential applications. POS tagging alone does not complete all the tasks listed above.

## 12. Limitations of POS Tagging

1. **Context ambiguity:** A word can have multiple grammatical roles.
2. **Model errors:** A tagger can predict an incorrect tag.
3. **Language dependence:** A model trained for English may not work properly for another language.
4. **Tag-set differences:** Different models can use different tag conventions.
5. **Unusual text:** Slang, misspellings, abbreviations, and informal writing can reduce accuracy.
6. **Domain differences:** A model trained on one type of text may perform differently on technical or specialized text.
7. **Limited interpretation:** POS tags provide grammatical labels, not a complete understanding of meaning.

## 13. Common Mistakes

- Confusing tokenization with POS tagging.
- Assuming each word always has the same grammatical role.
- Treating predicted tags as guaranteed grammatical truth.
- Assuming every POS tag set uses the same labels.
- Forgetting to install NLTK.
- Ignoring missing tokenizer or tagger resources.
- Assuming a proper noun tag is the same as a named entity label.
- Assuming POS tagging alone provides a complete syntactic or semantic analysis.

## 14. Troubleshooting NLTK Resources

If your code raises a `LookupError`, NLTK may be unable to find a required data resource.

First, read the error message to identify the missing resource.

Consult the official [NLTK Data Guide](https://www.nltk.org/data.html) and install the appropriate resource for your environment.

Resource requirements can vary by NLTK version. For example, some versions require `punkt_tab` for tokenization and `averaged_perceptron_tagger_eng` for English POS tagging.

Do not assume that downloading only one resource will fix every possible `LookupError`.

## 15. Points to Remember

- POS stands for Part-of-Speech.
- POS tagging assigns grammatical labels to tokens.
- Common categories include nouns, verbs, adjectives, and adverbs.
- NLTK provides the `pos_tag()` method for POS tagging.
- Tokenization commonly occurs before POS tagging.
- Context can change the grammatical role of a word.
- The Penn Treebank tag set includes tags such as `NN`, `VB`, `JJ`, and `RB`.
- POS tags are model predictions and can contain errors.
- POS tagging and NER are different NLP tasks.
- NLTK may require additional data resources beyond installing the Python package.

## 16. References

- [NLTK Official Documentation](https://www.nltk.org/)
- [NLTK POS Tagging Documentation](https://www.nltk.org/api/nltk.tag.html)
- [NLTK Data Guide](https://www.nltk.org/data.html)
- [Penn Treebank Project](https://www.cis.upenn.edu/~treebank/)
