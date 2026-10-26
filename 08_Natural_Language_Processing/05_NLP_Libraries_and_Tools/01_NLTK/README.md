# NLTK

NLTK is a Python toolkit for learning and experimenting with natural-language processing. It includes tokenizers, stemmers, lemmatizers, corpora, part-of-speech tagging, and chunking utilities.

## Existing practice

- [Tokens.ipynb](Tokens.ipynb) is a cross-topic practical notebook covering tokenization, N-grams, stop words, stemming, lemmatization, POS tagging, NER, and WordCloud.
- The notebook is a teaching example, not a complete test suite. Some language stop-word lists and tagging models require separate NLTK data downloads.
- Focused notes are available for [text preprocessing](../../01_Text_Preprocessing/README.md), [N-grams](../../02_Text_Representation/02_N_Grams/README.md), [POS tagging](../../03_Linguistic_Analysis/01_POS_Tagging/README.md), and [NER](../../03_Linguistic_Analysis/02_Named_Entity_Recognition/README.md).

## Install and download data

Install the Python package in the same environment used by your notebook:

```bash
python -m pip install nltk
```

Download only the corpora or models needed for your examples. From a Python session:

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

The exact resources depend on your NLTK version and the functions you call. If a resource is unavailable, consult the official [NLTK data guide](https://www.nltk.org/data.html). Optional multilingual stop-word lists may not exist for every language in the NLTK corpus.

## Key APIs

| API | Purpose |
|---|---|
| word_tokenize(text) | Split text into word-like tokens and punctuation |
| sent_tokenize(text) | Split text into sentences |
| ngrams(tokens, n) | Generate N-grams of a specified size |
| stopwords.words("english") | Load English stop words |
| PorterStemmer() | Reduce words using stemming rules |
| WordNetLemmatizer() | Map word forms to WordNet lemmas |
| pos_tag(tokens) | Predict part-of-speech tags |
| ne_chunk(tagged_tokens) | Build a simple named-entity chunk tree |

Remember that POS tags and named-entity chunks are model predictions. They can be wrong, especially on domain-specific or multilingual text.
