# N-Grams

An N-gram is a sequence of **n consecutive tokens** extracted from text. Tokens are usually words, but they can also be characters or other text units.

N-grams are used in Natural Language Processing (NLP) to capture local word order and identify common phrases.

For example, consider the sentence:

```text
Natural language processing is interesting.
```

After converting the sentence to lowercase and tokenizing it:

```python
["natural", "language", "processing", "is", "interesting"]
```

We can generate different types of N-grams from these tokens.

- **Unigrams:** One token at a time.
- **Bigrams:** Two consecutive tokens.
- **Trigrams:** Three consecutive tokens.
- **Four-grams:** Four consecutive tokens.
- **N-grams:** A general term for sequences of `n` consecutive tokens.

## 1. Types of N-Grams

### 1.1 Unigrams

A unigram contains one token, so `n = 1`.

Example:

```text
Sentence: Natural language processing is interesting.
```

Unigrams:

```python
[
    ("natural",),
    ("language",),
    ("processing",),
    ("is",),
    ("interesting",)
]
```

Unigrams are useful for counting individual words and creating basic text representations.

### 1.2 Bigrams

A bigram contains two consecutive tokens, so `n = 2`.

Example:

```text
Sentence: Natural language processing is interesting.
```

Bigrams:

```python
[
    ("natural", "language"),
    ("language", "processing"),
    ("processing", "is"),
    ("is", "interesting")
]
```

Bigrams capture short word combinations. For example, `machine learning` is a common two-word phrase.

### 1.3 Trigrams

A trigram contains three consecutive tokens, so `n = 3`.

Trigrams:

```python
[
    ("natural", "language", "processing"),
    ("language", "processing", "is"),
    ("processing", "is", "interesting")
]
```

Trigrams capture more local context than unigrams and bigrams, but they may occur less frequently in a dataset.

### 1.4 Four-Grams

A four-gram contains four consecutive tokens, so `n = 4`.

Four-grams:

```python
[
    ("natural", "language", "processing", "is"),
    ("language", "processing", "is", "interesting")
]
```

Longer N-grams can represent more specific phrases, but they generally require more data to occur frequently.

### 1.5 General N-Grams

An N-gram can contain any positive number of consecutive tokens.

For example, the sentence:

```text
I love learning Python today.
```

Has the following five-gram:

```python
("i", "love", "learning", "python", "today")
```

The value of `n` determines how many consecutive tokens are included in each N-gram.

## 2. Mathematical Formula

Suppose a sequence contains `T` tokens and we want to generate N-grams of size `n`.

The number of contiguous N-gram occurrences is:

\[
N = \max(0, T-n+1)
\]

Where:

- `T` is the total number of tokens.
- `n` is the size of each N-gram.
- `N` is the total number of N-gram occurrences.

For a sentence containing eight tokens:

| N-gram type | n | Number of occurrences |
|---|---:|---:|
| Unigrams | 1 | 8 |
| Bigrams | 2 | 7 |
| Trigrams | 3 | 6 |
| Four-grams | 4 | 5 |
| Five-grams | 5 | 4 |

This formula counts all occurrences, including repeated N-grams. It does not count only unique sequences.

## 3. How N-Grams Work

N-grams are generated using a sliding window that moves through the token sequence.

Consider these tokens:

```python
tokens = ["i", "love", "learning", "python"]
```

For bigrams, the window contains two tokens at a time:

```text
Step 1: i love
Step 2: love learning
Step 3: learning python
```

The resulting bigrams are:

```python
[
    ("i", "love"),
    ("love", "learning"),
    ("learning", "python")
]
```

Each step moves the window forward by one token. The sequences overlap, preserving the local order of the original text.

## 4. Implementing N-Grams Using Python

The following example uses Python's standard library and requires no third-party packages.

```python
# N-Grams

import re

text = "Natural language models learn from sequences of words."

# Convert text to lowercase and tokenize
tokens = re.findall(r"[a-z]+", text.lower())

print("Original Text:", text)
print("Tokens:", tokens)

# Generate unigrams
unigrams = [
    tuple(tokens[index:index + 1])
    for index in range(len(tokens))
]

print("\nUnigrams:")
print(unigrams)

# Generate bigrams
bigrams = [
    tuple(tokens[index:index + 2])
    for index in range(len(tokens) - 1)
]

print("\nBigrams:")
print(bigrams)

# Generate trigrams
trigrams = [
    tuple(tokens[index:index + 3])
    for index in range(len(tokens) - 2)
]

print("\nTrigrams:")
print(trigrams)

# Generate four-grams
n = 4

n_grams = [
    tuple(tokens[index:index + n])
    for index in range(len(tokens) - n + 1)
]

print(f"\n{n}-Grams:")
print(n_grams)

# Display the number of occurrences
print("\nNumber of Unigrams:", len(unigrams))
print("Number of Bigrams:", len(bigrams))
print("Number of Trigrams:", len(trigrams))
print(f"Number of {n}-Grams:", len(n_grams))
```

### Expected output

```text
Original Text: Natural language models learn from sequences of words.
Tokens: ['natural', 'language', 'models', 'learn', 'from', 'sequences', 'of', 'words']

Unigrams:
[('natural',), ('language',), ('models',), ('learn',), ('from',), ('sequences',), ('of',), ('words',)]

Bigrams:
[('natural', 'language'), ('language', 'models'), ('models', 'learn'), ('learn', 'from'), ('from', 'sequences'), ('sequences', 'of'), ('of', 'words')]

Trigrams:
[('natural', 'language', 'models'), ('language', 'models', 'learn'), ('models', 'learn', 'from'), ('learn', 'from', 'sequences'), ('from', 'sequences', 'of'), ('sequences', 'of', 'words')]

4-Grams:
[('natural', 'language', 'models', 'learn'), ('language', 'models', 'learn', 'from'), ('models', 'learn', 'from', 'sequences'), ('learn', 'from', 'sequences', 'of'), ('from', 'sequences', 'of', 'words')]

Number of Unigrams: 8
Number of Bigrams: 7
Number of Trigrams: 6
Number of 4-Grams: 5
```

The regular expression `r"[a-z]+"` extracts consecutive English letters after lowercasing. Punctuation is not included in the resulting tokens.

## 5. Generating N-Grams Using NLTK

NLTK provides the `ngrams()` utility for generating N-grams.

Install NLTK if necessary:

```bash
python -m pip install nltk
```

Example:

```python
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

text = "I love learning Python."

tokens = word_tokenize(text.lower())

# Generate bigrams
bigrams = list(ngrams(tokens, 2))

# Generate trigrams
trigrams = list(ngrams(tokens, 3))

print("Tokens:", tokens)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

Output:

```text
Tokens: ['i', 'love', 'learning', 'python', '.']
Bigrams: [('i', 'love'), ('love', 'learning'), ('learning', 'python'), ('python', '.')]
Trigrams: [('i', 'love', 'learning'), ('love', 'learning', 'python'), ('learning', 'python', '.')]
```

The second argument to `ngrams()` specifies the N-gram size and is required.

When using `word_tokenize()`, install or download the NLTK data resources required by your environment.

## 6. Counting N-Gram Frequencies

N-gram frequency counts show how often each sequence occurs in a text.

Example:

```python
import re
from collections import Counter

text = "I love Python. I love learning Python."

# Tokenize the text
tokens = re.findall(r"[a-z]+", text.lower())

# Generate bigrams
bigrams = [
    tuple(tokens[index:index + 2])
    for index in range(len(tokens) - 1)
]

# Count bigram occurrences
bigram_counts = Counter(bigrams)

print("Bigram Frequencies:")

for bigram, count in bigram_counts.items():
    print(bigram, ":", count)
```

Output:

```text
Bigram Frequencies:
('i', 'love') : 2
('love', 'python') : 1
('python', 'i') : 1
('love', 'learning') : 1
('learning', 'python') : 1
```

The bigram `("i", "love")` appears twice. Frequency counts can help identify common phrases, although frequent sequences are not necessarily meaningful.

## 7. N-Grams vs. Bag of Words

Bag of Words represents documents using word counts without preserving word order. N-grams represent consecutive token sequences and therefore retain local order.

Consider the following documents:

```text
Document 1: dogs chase cats
Document 2: cats chase dogs
```

Both documents contain the same unigram counts.

However, their bigrams differ:

| Document | Bigrams |
|---|---|
| Document 1 | `dogs chase`, `chase cats` |
| Document 2 | `cats chase`, `chase dogs` |

This allows bigram features to distinguish some word-order differences that standard Bag of Words cannot capture.

However, N-grams do not fully understand sentence meaning or long-distance relationships.

## 8. Advantages and Limitations

### Advantages

- Captures local word order.
- Represents common phrases as features.
- Is relatively easy to implement.
- Can improve traditional text classification models.
- Supports frequency analysis and statistical language modeling.

### Limitations

- The number of possible features can grow rapidly.
- Longer N-grams are often less frequent.
- Unseen sequences may not appear in the vocabulary.
- N-grams do not fully represent sentence meaning.
- Tokenization and punctuation handling affect the results.
- Fixed-size N-grams do not directly capture long-distance relationships.

## 9. Practical Applications

### Search Engines

Bigrams and trigrams can help identify phrases in search queries and documents.

### Text Classification

N-gram features can help distinguish documents using word combinations rather than isolated words.

### Autocomplete

N-gram language models can estimate likely next words based on preceding tokens.

### Spam Detection

Frequent phrases can help identify patterns associated with spam messages.

### Language Modeling

Statistical N-gram models estimate the probability of a word based on preceding tokens.

A bigram model estimates:

\[
P(w_i \mid w_{i-1})
\]

This represents the probability of the current word given the previous word.

A trigram model estimates:

\[
P(w_i \mid w_{i-2}, w_{i-1})
\]

It uses the previous two words as context.

These models learn statistical language patterns rather than understanding language in the human sense.

## 10. Common Mistakes

- **Using the wrong value of n:** Bigrams require `n=2`, and trigrams require `n=3`.
- **Ignoring tokenization:** Different tokenization methods produce different N-grams.
- **Assuming N-grams are unique:** The same sequence can occur multiple times.
- **Confusing occurrences with unique sequences:** Frequency and vocabulary size are different measurements.
- **Choosing very large N-grams without enough data:** Many features may occur rarely.
- **Ignoring punctuation decisions:** Including punctuation changes the resulting sequences.
- **Assuming N-grams understand meaning:** They capture local patterns, not complete semantics.

## 11. Exercises

### Exercise 1: Generate Unigrams

Given the sentence:

```text
I love learning Python
```

Write down all unigrams.

### Exercise 2: Generate Bigrams

Use the same sentence and list all bigrams.

### Exercise 3: Generate Trigrams

List all trigrams and compare their number with the number of bigrams.

### Exercise 4: General N-Grams

Use the sentence:

```text
Natural language processing is interesting
```

Generate four-grams and five-grams using Python.

### Exercise 5: Count Unique Bigrams

Compare the sentences:

```text
I love Python and I love coding.
I love learning and love Python.
```

Tokenize both sentences, generate bigrams, and count the total and unique bigrams.

### Exercise 6: Compare with Bag of Words

Compare:

```text
dogs chase cats
cats chase dogs
```

Explain why their unigram counts are identical but their bigram sequences differ.

### Exercise 7: Experiment with N

Use a sentence containing eight tokens. Generate N-grams for `n = 1, 2, 3, 4, 5`, then verify the formula for the number of occurrences.

## 12. Related Topics

- [Bag of Words](../01_Bag_of_Words/README.md) — Representing documents using word counts.
- [TF-IDF](../03_TF_IDF/README.md) — Weighting words according to their frequency and document rarity.
- [Word2Vec](../06_Word2Vec/README.md) — Learning word representations from contextual patterns.
- [Tokenization](../../01_Text_Preprocessing/04_Tokenization/README.md) — Splitting text into tokens.

## 13. Points to Remember

- An N-gram is a sequence of `n` adjacent tokens.
- Unigrams contain one token, bigrams two, and trigrams three.
- N-grams preserve local word order.
- The number of contiguous N-gram occurrences is `max(0, T - n + 1)`.
- Larger N-grams capture more local context but are often less frequent.
- Repeated N-grams can occur multiple times.
- N-grams can be generated manually or with NLTK.
- N-grams are useful features but do not fully capture sentence meaning.

**Final takeaway:** N-grams extend basic word-count representations by capturing local word order. They are a useful bridge between simple Bag of Words features and more advanced language representations.
