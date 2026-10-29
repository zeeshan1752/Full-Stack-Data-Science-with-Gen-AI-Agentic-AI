# Tokenization

Tokenization is a fundamental preprocessing technique in Natural Language Processing (NLP). It divides text into smaller units called **tokens**. Depending on the task, these tokens can be sentences, words, punctuation marks, or subword units.

For example, consider the following sentence:

```text
NLP is interesting. I am learning Python!
```

After sentence tokenization:

```python
[
    "NLP is interesting.",
    "I am learning Python!"
]
```

After word tokenization:

```python
[
    "NLP", "is", "interesting", ".",
    "I", "am", "learning", "Python", "!"
]
```

Tokenization converts raw text into manageable units that can be processed by NLP algorithms.

## 1. Why Is Tokenization Important?

Computers need text to be represented in a structured form before many NLP operations can be performed. Tokenization is an important step in preparing text for further analysis.

Tokenization helps to:

- Prepare text for Bag of Words and TF-IDF.
- Count word frequencies.
- Identify sentence boundaries.
- Process reviews for sentiment analysis.
- Prepare text for chatbots and text classification.
- Process documents and social media posts.
- Prepare text for modern language models.

For example, a sentiment analysis system may tokenize the review:

```text
The product is very good!
```

Into:

```python
["The", "product", "is", "very", "good", "!"]
```

These tokens can then be converted into numerical features for machine learning.

## 2. Types of Tokenization

### 2.1 Sentence Tokenization

Sentence tokenization divides a paragraph into individual sentences.

**Example:**

```text
NLP is useful. Tokenization is important! Are you learning Python?
```

Output:

```python
[
    "NLP is useful.",
    "Tokenization is important!",
    "Are you learning Python?"
]
```

Using NLTK:

```python
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")

text = "NLP is useful. Tokenization is important! Are you learning Python?"

sentences = sent_tokenize(text)

print(sentences)
```

Sentence tokenization is useful when each sentence needs to be analyzed separately.

**Important:** Sentence boundaries are not always determined by periods alone. Abbreviations such as `Dr.`, decimal numbers such as `3.14`, and language-specific patterns can make sentence segmentation more challenging.

### 2.2 Word Tokenization

Word tokenization divides text into individual words and often separates punctuation marks.

**Example:**

```text
NLP is useful!
```

Output:

```python
["NLP", "is", "useful", "!"]
```

Using NLTK:

```python
from nltk.tokenize import word_tokenize

text = "NLP is useful!"

words = word_tokenize(text)

print(words)
```

Word tokenization is commonly used before word-frequency analysis, text representation, and traditional NLP workflows.

### 2.3 Whitespace Tokenization

Whitespace tokenization splits text wherever whitespace occurs, including spaces, tabs, and newlines.

**Example:**

```python
text = "NLP is useful"

tokens = text.split()

print(tokens)
```

Output:

```python
["NLP", "is", "useful"]
```

Whitespace tokenization is simple and does not require an external library.

However, punctuation usually remains attached to words.

```python
text = "Hello, world!"

print(text.split())
```

Output:

```python
["Hello,", "world!"]
```

### 2.4 Word-Punctuation Tokenization

NLTK provides `wordpunct_tokenize()`, which separates sequences of word characters from punctuation sequences.

**Example:**

```python
from nltk.tokenize import wordpunct_tokenize

text = "Hello, world!"

tokens = wordpunct_tokenize(text)

print(tokens)
```

Output:

```python
["Hello", ",", "world", "!"]
```

This method is useful when punctuation needs to be separated explicitly.

Unlike `word_tokenize()`, it does not perform the same language-aware sentence tokenization. Therefore, the two methods can produce different results for contractions and other complex text.

### 2.5 Subword Tokenization

Subword tokenization divides words into smaller units. It is widely used in modern language models.

For example, a tokenizer might divide a word into smaller pieces:

```text
unhappiness → un + happi + ness
```

This is an illustrative example; actual tokens depend on the tokenizer.

Subword tokenization helps language models process rare words, new words, and different word forms without requiring every complete word to be present in the vocabulary.

Common subword tokenization approaches include:

- Byte Pair Encoding (BPE)
- WordPiece
- Unigram language-model tokenization

These approaches are commonly used in transformer-based language models.

## 3. Comparison of Tokenization Methods

| Method | Purpose | Example input: `Hello, world!` |
|---|---|---|
| Sentence tokenization | Splits text into sentences | `["Hello, world!"]` |
| `word_tokenize()` | Splits text into words and punctuation | `["Hello", ",", "world", "!"]` |
| `str.split()` | Splits text using whitespace | `["Hello,", "world!"]` |
| `wordpunct_tokenize()` | Separates word and punctuation sequences | `["Hello", ",", "world", "!"]` |
| Subword tokenization | Splits text into model-specific units | Depends on the tokenizer |

No single method is best for every application. The appropriate tokenizer depends on the input text and the NLP task.

## 4. Complete Practical Example Using NLTK

The following program demonstrates sentence tokenization, word tokenization, and word-punctuation tokenization.

```python
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")

text = "NLP is useful. Tokenizers split text into units!"

print("Original Text:", text)

# Sentence Tokenization
sentences = sent_tokenize(text)
print("\nSentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("\nWords:", words)

# Word-Punctuation Tokenization
word_punctuation = wordpunct_tokenize(text)
print("\nWord-Punctuation Tokens:", word_punctuation)
```

**Expected output:**

```text
Original Text: NLP is useful. Tokenizers split text into units!

Sentences: ['NLP is useful.', 'Tokenizers split text into units!']

Words: ['NLP', 'is', 'useful', '.', 'Tokenizers', 'split', 'text', 'into', 'units', '!']

Word-Punctuation Tokens: ['NLP', 'is', 'useful', '.', 'Tokenizers', 'split', 'text', 'into', 'units', '!']
```

For this example, both word-based tokenizers return the same tokens. Their outputs can differ for other inputs.

## 5. Understanding the NLTK Functions

### `sent_tokenize()`

- Splits text into sentences.
- Returns a list of sentences.
- Uses NLTK's sentence-tokenization resources.

### `word_tokenize()`

- Splits text into word-level tokens and punctuation.
- Commonly uses sentence tokenization internally.
- May require additional NLTK data resources.

### `wordpunct_tokenize()`

- Separates word-character sequences from punctuation sequences.
- Returns a list of tokens.
- Does not require the same downloaded sentence-tokenization resources as the other two functions.

## 6. Installing and Configuring NLTK

Install NLTK using the following terminal command:

```bash
python -m pip install nltk
```

If NLTK reports a missing resource, download the resource named in the error message.

For example:

```python
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
```

You can also download a larger collection of popular NLTK datasets:

```bash
python -m nltk.downloader popular
```

The `popular` collection is not always necessary. Downloading only the resources required by your program is usually more efficient.

## 7. Practical Applications

### Sentiment Analysis

Tokenization prepares customer reviews for sentiment analysis.

```text
Review: The movie was amazing!
```

Tokens:

```python
["The", "movie", "was", "amazing", "!"]
```

### Search Engines

Search engines can tokenize queries before matching them against indexed documents.

```text
Query: best machine learning course
```

Tokens:

```python
["best", "machine", "learning", "course"]
```

### Chatbots

Tokenization is one of the steps used to process user messages and identify relevant language patterns.

### Text Classification

Spam detection, topic classification, and document categorization often use tokenization before converting text into numerical representations.

### Language Models

Modern language models generally process token IDs produced by their own tokenizers. These tokens may represent complete words, subwords, or other units.

## 8. Common Mistakes

- **Assuming every tokenizer produces the same output:** Different algorithms follow different rules.
- **Confusing sentence and word tokenization:** Sentence tokenization identifies sentences, while word tokenization identifies smaller units.
- **Assuming whitespace splitting removes punctuation:** Punctuation generally remains attached to words.
- **Ignoring contractions:** Words such as `don't` may be handled differently by different tokenizers.
- **Ignoring abbreviations:** Text such as `Dr. Kumar arrived.` can challenge sentence segmentation.
- **Assuming punctuation is always unnecessary:** Punctuation can carry useful information for sentiment analysis and other NLP tasks.
- **Forgetting NLTK data resources:** Installing NLTK does not necessarily install every tokenizer dataset.
- **Assuming subword tokenization has a universal output:** Results depend on the tokenizer and its vocabulary.

---

## 9. Related Topics

- [Text Cleaning](../01_Basics_and_Cleaning/) — Preparing raw text before tokenization.
- [Stop-Word Removal](../03_Stopwords_Stemming_Lemmatization/) — Removing selected common words when appropriate.
- [Bag of Words](../../03_Text_Representation/01_Bag_of_Words_and_NGrams/) — Representing text using word-frequency features.

---

## 10. Points to Remember

- Tokenization divides text into smaller units called tokens.
- Sentence tokenization identifies sentence boundaries.
- Word tokenization separates text into word-level units and often punctuation.
- Whitespace tokenization is simple but usually leaves punctuation attached to words.
- Word-punctuation tokenization separates word and punctuation sequences.
- Subword tokenization is commonly used in modern language models.
- Tokenization output depends on the selected method and input text.
- NLTK may require additional data resources beyond package installation.
- Tokenization is commonly followed by further preprocessing and text-representation techniques.

**Final takeaway:** Tokenization transforms raw text into structured units, making it easier to analyze, represent, and process natural language using NLP techniques.


## Example scripts

- [NLTK tokenization script](tokenization_nltk.py)
- [spaCy tokenization script](tokenization_spacy.py) (requires the `en_core_web_sm` model)
- [NLTK and spaCy comparison notebook](comparison.ipynb)
- [Cross-topic NLTK practice notebook](nltk_cross_topic_practice.ipynb)

---

## NLTK

NLTK is a Python toolkit for teaching and experimenting with natural-language processing. It provides tokenizers, stemming and lemmatization tools, corpus access, tagging, and chunking utilities.

### Existing practice

- [nltk_cross_topic_practice.ipynb](nltk_cross_topic_practice.ipynb) is the preserved cross-topic practical notebook. It includes tokenization, n-grams, stop words (including multilingual lookups), stemming, lemmatization, POS tagging, NER, and a WordCloud example.
- Cached outputs were cleared before public upload because they contained personal and environment metadata. Run the cells locally to regenerate outputs; optional Hindi/Kannada stop-word resources may need to be downloaded.
- The preserved practice notebook is available as [nltk_cross_topic_practice.ipynb](nltk_cross_topic_practice.ipynb).

The notebook's coverage shows practice in these areas; it does not by itself establish that every item was fully completed in class. Focused conceptual notes live in [preprocessing overview](../README.md), [n-grams](../../03_Text_Representation/01_Bag_of_Words_and_NGrams/README.md#n-grams), [POS tagging](../../02_Linguistic_Analysis/01_POS_Tagging/README.md), and [NER](../../02_Linguistic_Analysis/02_NER/README.md).

### Setup

Install NLTK with python -m pip install nltk. Download NLTK data only when required; see the official [NLTK data guide](https://www.nltk.org/data.html).
