# Text Normalization in NLP

## 1. Introduction

**Text Normalization** is the process of converting text into a consistent and standardized form so that different variations of the same word or expression can be handled more consistently by an NLP system.

People write the same words in different ways. For example:

- `HELLO WORLD`
- `Hello World`
- `hello world`

In many NLP tasks, these sentences have the same meaning. Normalization can convert them into a consistent representation:

`hello world`

Text normalization helps reduce unnecessary variations in text and can make downstream text processing more effective.

It is commonly used in Natural Language Processing (NLP), text classification, sentiment analysis, search engines, chatbots, and other language-processing applications.

## 2. Why Is Text Normalization Important?

Consider these examples:

| Original Text | Normalized Text |
|---|---|
| `HELLO PYTHON` | `hello python` |
| `  natural   language  ` | `natural language` |
| `I don't know` | `i do not know` |
| `Python!!!` | `python!!!` |
| `u r gr8` | `you are great` |

The transformations above use different techniques. Not every normalization pipeline performs all of them, and punctuation is intentionally retained in the fourth example.

Without suitable normalization, the same expression may appear in multiple forms, increasing vocabulary variation and making comparisons more difficult.

For example, a simple word-counting system may treat `Python` and `python` as different tokens unless it normalizes case or uses a case-insensitive approach.

## 3. Common Text Normalization Techniques

### 3.1 Lowercasing

Lowercasing converts uppercase letters to lowercase.

Example:

Original:

`Natural Language Processing Is Interesting`

Normalized:

`natural language processing is interesting`

Python example:

```python
text = "Natural Language Processing Is Interesting"

normalized_text = text.lower()

print(normalized_text)
```

Output:

```text
natural language processing is interesting
```

**Why use it?**

- Reduces differences caused by capitalization.
- Helps combine words such as `Python` and `python`.
- Can reduce the number of distinct tokens in a vocabulary.

**Limitation:** Capitalization can carry meaning. For example, `apple` may refer to a fruit, while `Apple` may refer to a company. Lowercasing should depend on the task.

### 3.2 Uppercasing

Uppercasing converts letters to uppercase.

Example:

`natural language processing` → `NATURAL LANGUAGE PROCESSING`

Python example:

```python
text = "natural language processing"

normalized_text = text.upper()

print(normalized_text)
```

Output:

```text
NATURAL LANGUAGE PROCESSING
```

Uppercasing is useful for some text-matching tasks, but lowercasing is more common in traditional text-processing pipelines.

### 3.3 Whitespace Normalization

Text may contain extra spaces, tabs, or newline characters.

Original:

`"Natural    Language     Processing"`

Normalized:

`"Natural Language Processing"`

Python example:

```python
import re

text = "   Natural    Language \n Processing   "

normalized_text = re.sub(r"\s+", " ", text).strip()

print(normalized_text)
```

Output:

```text
Natural Language Processing
```

Explanation:

- `\s+` matches one or more whitespace characters.
- `re.sub()` replaces matching sequences with a single space.
- `strip()` removes whitespace at the beginning and end.

Whitespace normalization is useful when text comes from copied documents, web pages, or inconsistent user input.

### 3.4 Contraction Expansion

A contraction is a shortened form of two or more words.

Examples:

- `don't` → `do not`
- `can't` → `cannot`
- `I'm` → `I am`
- `they're` → `they are`
- `it's` → `it is` or `it has`, depending on context

Python example:

```python
text = "I don't know why they're waiting."

text = text.replace("don't", "do not")
text = text.replace("they're", "they are")

print(text)
```

Output:

```text
I do not know why they are waiting.
```

**Important:** Simple replacements are suitable for selected examples, but they do not handle every contraction or contextual ambiguity. A dedicated normalization tool or carefully designed rules may be needed for larger datasets.

### 3.5 Standardizing Informal Language

Informal text often contains abbreviations, slang, and shortened expressions.

Examples:

| Informal Form | Standardized Form |
|---|---|
| `u` | `you` |
| `r` | `are` |
| `gr8` | `great` |
| `pls` | `please` |
| `thx` | `thanks` |

Python example:

```python
text = "u r gr8"

normalization_map = {
    "u": "you",
    "r": "are",
    "gr8": "great"
}

words = text.split()

normalized_words = [
    normalization_map.get(word, word)
    for word in words
]

normalized_text = " ".join(normalized_words)

print(normalized_text)
```

Output:

```text
you are great
```

This approach uses a dictionary to map known informal expressions to standard forms.

**Limitation:** Informal expressions can have multiple meanings. Avoid replacing words blindly, especially when meaning or context matters.

### 3.6 Unicode Normalization

Unicode allows some characters to be represented in more than one underlying way. For example, an accented character can be represented as a single character or as a base character followed by a combining accent.

Unicode normalization standardizes these representations.

Python example:

```python
import unicodedata

text = "café"

normalized_text = unicodedata.normalize("NFC", text)

print(normalized_text)
```

Output:

```text
café
```

Common Unicode normalization forms include:

- **NFC:** Combines characters into canonical composed forms where possible.
- **NFD:** Decomposes characters into canonical forms.
- **NFKC:** Applies compatibility normalization and may combine characters that are considered compatibility-equivalent.
- **NFKD:** Applies compatibility decomposition.

Compatibility normalization can change the representation of some characters, so choose the form based on your data and application.

### 3.7 Spelling Normalization

Spelling normalization standardizes selected spelling variations or corrects misspellings.

Examples:

- `teh` → `the`
- `recieve` → `receive`

These transformations usually require a dictionary, spelling-correction library, or context-aware method.

Automatic correction should be used carefully because names, technical terms, abbreviations, and regional spellings may otherwise be changed incorrectly.

### 3.8 Repeated Character Normalization

Informal messages sometimes contain repeated characters for emphasis.

Examples:

- `soooo good` → `soo good`
- `heyyyy` → `heyy`

A simple regular expression can reduce repeated characters:

```python
import re

text = "This is sooo good!!!"

normalized_text = re.sub(r"(.)\1{2,}", r"\1\1", text)

print(normalized_text)
```

Output:

```text
This is soo good!!
```

This example limits sequences of three or more identical characters to two. Such rules may be useful for informal text but can damage meaningful spellings, names, or intentional expressions if applied indiscriminately.

## 4. Text Normalization vs. Text Cleaning

Text normalization and text cleaning are related, but their primary purposes differ.

| Feature | Text Cleaning | Text Normalization |
|---|---|---|
| Main purpose | Remove unwanted or noisy content | Standardize text representations |
| Typical operations | Remove HTML tags, unwanted symbols, or irrelevant markup | Lowercasing, whitespace standardization, contraction expansion |
| Example | `<p>Hello</p>` → `Hello` | `HELLO` → `hello` |
| Main goal | Improve the quality of input text | Improve consistency of text |
| Overlap | May include standardization | May include cleaning-like transformations |

The distinction is not absolute. Different courses, libraries, and projects may classify some operations differently.

For example, removing punctuation may be considered text cleaning, but it is not always part of normalization.

## 5. Text Normalization vs. Tokenization

**Normalization** standardizes text, while **tokenization** splits text into smaller units such as words or sentences.

Example:

Original text:

`"HELLO    WORLD!"`

After normalization:

`"hello world!"`

After word tokenization:

`["hello", "world", "!"]`

The exact tokens depend on the tokenizer used.

Normalization and tokenization are separate operations, although they are often used together in a text preprocessing pipeline.

## 6. Text Normalization vs. Stemming and Lemmatization

Stemming and lemmatization are commonly taught alongside text normalization because they reduce variations in word forms.

### Stemming

Stemming uses rules to reduce words to stems, which may not be valid dictionary words.

Examples:

- `playing` → `play`
- `connected` → `connect`
- `studies` → `studi` with some stemming algorithms

The result depends on the algorithm.

### Lemmatization

Lemmatization uses vocabulary and linguistic information to return a word's dictionary form, called a lemma.

Examples:

- `running` → `run`
- `cars` → `car`
- `better` → `good` when the word is analyzed as an adjective in the appropriate context

Lemmatization may require part-of-speech information for the correct result.

### Comparison

| Technique | Purpose | Example |
|---|---|---|
| Lowercasing | Standardizes capitalization | `HELLO` → `hello` |
| Whitespace normalization | Standardizes spacing | Multiple spaces → one space |
| Stemming | Reduces words using rules | `studies` → `studi` |
| Lemmatization | Finds a dictionary form | `cars` → `car` |
| Tokenization | Splits text into units | Sentence → word tokens |

## 7. Complete Text Normalization Pipeline in Python

The following example combines lowercasing, contraction expansion, whitespace normalization, and selected informal-word replacements.

```python
# Text Normalization

import re
import unicodedata

text = "   HELLO!!!   I don't know   why u r waiting.   "

print("Original Text:", repr(text))

# Apply Unicode normalization
text = unicodedata.normalize("NFC", text)

# Convert text to lowercase
text = text.lower()

# Expand selected contractions
text = text.replace("don't", "do not")

# Standardize selected informal words
normalization_map = {
    "u": "you",
    "r": "are"
}

words = text.split()

normalized_words = [
    normalization_map.get(word, word)
    for word in words
]

text = " ".join(normalized_words)

# Normalize whitespace
text = re.sub(r"\s+", " ", text).strip()

print("Normalized Text:", text)
```

Output:

```text
Original Text: "   HELLO!!!   I don't know   why u r waiting.   "
Normalized Text: hello!!! i do not know why you are waiting.
```

### Explanation

1. Unicode normalization standardizes compatible character representations.
2. Lowercasing makes capitalization consistent.
3. Contraction expansion replaces a selected shortened expression.
4. Dictionary-based replacements standardize selected informal words.
5. Whitespace normalization removes unnecessary spacing.

This pipeline deliberately keeps punctuation. Additional cleaning steps should be added only when the task requires them.

## 8. When Should You Use Text Normalization?

Normalization is useful in many applications.

### Search Engines

Normalization helps a search system match queries and documents with consistent representations.

### Sentiment Analysis

Lowercasing and selected text standardization can reduce variation in review text. However, punctuation and capitalization may express emotion and should sometimes be preserved.

### Chatbots

Normalization can help standardize informal user messages before intent classification or other processing.

### Text Classification

Consistent text representations can reduce unnecessary vocabulary variation and make model features more consistent.

### Social Media Analysis

Normalization can help process abbreviations, repeated characters, inconsistent spacing, and informal expressions.

### Information Retrieval

Normalization can improve matching between a query and documents when they contain equivalent textual forms.

## 9. Common Mistakes

1. **Removing all punctuation automatically.** Punctuation may carry meaning, especially in sentiment analysis or conversational text.
2. **Assuming every task needs lowercasing.** Capitalization can distinguish names, abbreviations, and other important information.
3. **Expanding contractions without considering context.** Expressions such as `it's` can have different expansions.
4. **Replacing informal words blindly.** Short forms may have multiple meanings.
5. **Confusing normalization with tokenization.** One standardizes text; the other splits it into units.
6. **Confusing stemming with lemmatization.** Stemming applies rules, while lemmatization aims to produce dictionary forms.
7. **Over-normalizing text.** Excessive transformations may remove important information or alter meaning.
8. **Applying inconsistent transformations.** Training and inference data should follow compatible preprocessing rules.
9. **Ignoring language-specific requirements.** Rules that work for English may not work for other languages.

## 10. Practice Exercises

### Beginner Level

**Exercise 1:** Convert `"HELLO WORLD"` into lowercase.

**Exercise 2:** Convert `"natural language processing"` into uppercase.

**Exercise 3:** Normalize the spaces in `"  Python    is   useful  "`.

**Exercise 4:** Expand the contraction `"don't"` into `"do not"`.

### Intermediate Level

**Exercise 5:** Create a dictionary to normalize `u`, `r`, and `gr8`.

**Exercise 6:** Use `unicodedata.normalize()` with NFC on a string containing an accented character.

**Exercise 7:** Write a program that combines lowercasing and whitespace normalization.

**Exercise 8:** Normalize a short social media message while preserving punctuation.

### Conceptual Questions

1. What is text normalization?
2. Why is normalization useful in NLP?
3. What is the difference between text normalization and text cleaning?
4. What is the difference between normalization and tokenization?
5. Why might lowercasing be harmful in some applications?
6. What is Unicode normalization?
7. How are stemming and lemmatization related to normalization?
8. Why should normalization rules depend on the NLP task?

## 11. Points to Remember

- Text normalization converts text into a consistent representation.
- Lowercasing and whitespace normalization are common techniques.
- Contraction expansion and informal-word standardization require suitable rules or tools.
- Unicode normalization handles different representations of Unicode text.
- Spelling correction and repeated-character normalization should be applied carefully.
- Normalization is related to text cleaning, but the two terms are not identical.
- Tokenization splits text into units; normalization standardizes text.
- Stemming and lemmatization reduce word-form variations.
- Not every normalization technique is appropriate for every NLP task.
- Preprocessing rules should be consistent between training and inference.

## 12. References

- [Python: `str` Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python: `re` — Regular Expression Operations](https://docs.python.org/3/library/re.html)
- [Python: `unicodedata`](https://docs.python.org/3/library/unicodedata.html)
- [NLTK Documentation](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/usage)

---

**Next topic:** [Tokenization](../02_Tokenization/README.md)

