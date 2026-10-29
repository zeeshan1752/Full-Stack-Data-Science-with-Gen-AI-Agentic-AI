# Parsing

**Status:** The code has not been run locally.

## 1. Introduction

Parsing is an NLP technique used to analyze the grammatical structure of a sentence.

In this folder, you will learn two approaches to parsing:

- **Constituency Parsing:** Groups words into phrases and shows the hierarchical structure of a sentence.
- **Dependency Parsing:** Connects words to their head words and identifies grammatical relationships between them.

Both approaches analyze sentence structure, but they represent it differently.

## 2. Installation

Install NLTK and spaCy:

```bash
python -m pip install nltk spacy
```

Download the English language model required by the spaCy example:

```bash
python -m spacy download en_core_web_sm
```

## 3. What You Will Learn

### Constituency Parsing

Constituency parsing groups words into grammatical phrases, such as noun phrases (NP) and verb phrases (VP).

The NLTK example uses a small, hand-written Context-Free Grammar (CFG) to generate parse trees.

### Dependency Parsing

Dependency parsing connects each word to a head word and labels the relationship between them.

The spaCy example demonstrates how to inspect tokens, their head words, and their dependency labels.

These are two different views of sentence structure, so the examples demonstrate them separately.

## 4. How to Run

Run either script from the repository root.

**Constituency parsing:**

```bash
python 08_Natural_Language_Processing/02_Linguistic_Analysis/03_Parsing/constituency_parser_nltk.py
```

**Dependency parsing:**

```bash
python 08_Natural_Language_Processing/02_Linguistic_Analysis/03_Parsing/dependency_parser_spacy.py
```

## 5. Constituency Parsing vs. Dependency Parsing

| Feature | Constituency Parsing | Dependency Parsing |
|---|---|---|
| Main focus | Phrase structure | Word-to-word relationships |
| Basic unit | Grammatical phrase | Dependency relation |
| Example labels | `S`, `NP`, `VP` | `ROOT`, `nsubj`, `obj` |
| Output | Hierarchical parse tree | Dependency relationships |
| Library used here | NLTK | spaCy |

## 6. Common Mistakes

- **Expecting every sentence to parse:** The NLTK grammar is deliberately small. A sentence outside its grammar may have no parse.
- **Missing spaCy model:** Install `en_core_web_sm` before running the dependency parsing example.
- **Confusing parsing approaches:** Constituency parsing groups words into phrases, while dependency parsing connects words through grammatical relationships.
- **Assuming every dependency label is correct:** spaCy's dependency labels are model predictions and may contain errors.
- **Running scripts from the wrong directory:** Use the repository root when following the commands above.

## 7. Points to Remember

- Parsing analyzes the grammatical structure of sentences.
- Constituency parsing represents phrase structure.
- Dependency parsing represents grammatical relationships between words.
- NLTK demonstrates constituency parsing with a hand-written grammar.
- spaCy demonstrates dependency parsing with a trained English language model.
- The code has not been run locally, so its execution still needs to be verified.

