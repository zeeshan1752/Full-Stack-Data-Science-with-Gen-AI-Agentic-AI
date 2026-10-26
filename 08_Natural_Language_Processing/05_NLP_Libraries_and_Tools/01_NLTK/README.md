# NLTK

NLTK is a Python toolkit for learning and experimenting with natural-language processing. This folder keeps library-specific practice; detailed explanations live in the core NLP modules to avoid repeating the same notes in multiple places.

## Existing practice

- [Tokens.ipynb](Tokens.ipynb) is a cross-topic practical notebook covering tokenization, N-grams, stop words, stemming, lemmatization, POS tagging, NER, and WordCloud.
- Treat the notebook as a teaching example, not a complete test suite. Some language resources and tagging models require separate NLTK data downloads.
- Read the canonical notes for [text preprocessing](../../01_Text_Preprocessing/README.md), [N-grams](../../02_Text_Representation/02_N_Grams/README.md), [POS tagging](../../03_Linguistic_Analysis/01_POS_Tagging/README.md), and [NER](../../03_Linguistic_Analysis/02_Named_Entity_Recognition/README.md).


## Exploring NLTK corpora

A **corpus** is a collection of text used for language study or NLP experiments. NLTK provides interfaces to several sample corpora, including Brown and Gutenberg. The corpus data is downloaded separately from the NLTK Python package.

Example:

```python
import nltk
from nltk.corpus import brown, gutenberg

# Run these downloads once in the environment you use for practice.
nltk.download("brown")
nltk.download("gutenberg")

print("Brown corpus file IDs:", brown.fileids()[:5])
print("First Brown words:", brown.words()[:20])
print("Gutenberg file IDs:", gutenberg.fileids()[:5])
print("Gutenberg word count in first file:", len(gutenberg.words(gutenberg.fileids()[0])))
```

Corpus data can be large, so inspect a small slice first. Use `fileids()` to discover available documents, `words()` to inspect tokens, and `sents()` to inspect sentence sequences. If a corpus is missing, download only the package named in the error or follow the official [NLTK data guide](https://www.nltk.org/data.html).

## Tokenizer and N-gram practical notes

The trainer notebook demonstrates sentence, word, blank-line, whitespace, and punctuation-aware tokenization, then generates unigrams, bigrams, trigrams, and arbitrary N-grams. The canonical explanations remain in [Tokenization](../../01_Text_Preprocessing/03_Tokenization/README.md) and [N-Grams](../../02_Text_Representation/02_N_Grams/README.md); use this folder for NLTK-specific APIs and corpus setup.

For `nltk.ngrams(tokens, n)`, always provide `n`. For example, `nltk.ngrams(tokens, 3)` creates trigrams. The number of adjacent N-grams is `max(0, len(tokens) - n + 1)`.

## Install and download data

Install the Python package in the same environment used by your notebook:

```bash
python -m pip install nltk
```

Download only the resources required by the examples. From Python:

```python
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("maxent_ne_chunker_tab")
nltk.download("words")
```

The exact resources depend on your NLTK version and the functions you call. Consult the official [NLTK data guide](https://www.nltk.org/data.html) if a resource is missing.

## Useful APIs

| API | Purpose |
|---|---|
| `word_tokenize(text)` | Split text into word-like tokens and punctuation |
| `sent_tokenize(text)` | Split text into sentences |
| `ngrams(tokens, n)` | Generate N-grams of a specified size |
| `stopwords.words("english")` | Load English stop words |
| `PorterStemmer()` | Reduce words using stemming rules |
| `WordNetLemmatizer()` | Map word forms to WordNet lemmas |
| `pos_tag(tokens)` | Predict part-of-speech tags |
| `ne_chunk(tagged_tokens)` | Build a simple named-entity chunk tree |

POS tags and named-entity chunks are model predictions and may be incorrect, especially for domain-specific or multilingual text.
