# NLTK

NLTK is a Python toolkit for learning and experimenting with natural-language processing. This folder keeps library-specific practice; detailed explanations live in the core NLP modules to avoid repeating the same notes in multiple places.

## Existing practice

- [Tokens.ipynb](Tokens.ipynb) is a cross-topic practical notebook covering tokenization, N-grams, stop words, stemming, lemmatization, POS tagging, NER, and WordCloud.
- Treat the notebook as a teaching example, not a complete test suite. Some language resources and tagging models require separate NLTK data downloads.
- Read the canonical notes for [text preprocessing](../../01_Text_Preprocessing/README.md), [N-grams](../../02_Text_Representation/02_N_Grams/README.md), [POS tagging](../../03_Linguistic_Analysis/01_POS_Tagging/README.md), and [NER](../../03_Linguistic_Analysis/02_Named_Entity_Recognition/README.md).

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
