# Bag of Words and N-Grams

Bag of Words represents documents with token counts. N-Grams extend the feature set to sequences of adjacent tokens.

- [Manual Bag of Words script](bag_of_words_manual.py)
- [scikit-learn Bag of Words example](bag_of_words_sklearn.py)
- [N-Gram example](n_grams.py)

---

## Bag of Words (BoW)

Bag of Words (BoW) is a text representation technique in Natural Language Processing (NLP) that converts text into numerical features based on the occurrence or frequency of words.

It creates a vocabulary of unique words from a collection of documents and represents each document using the counts of those words.

BoW is simple, easy to understand, and commonly used as a baseline for text classification and other NLP tasks.

### 1. Why Is Bag of Words Important?

Machine learning algorithms generally require numerical input. Bag of Words converts text into numbers that can be used by these algorithms.

Consider two documents:

```text
Document 1: cats chase mice
Document 2: dogs chase cats
```

The vocabulary contains the unique words:

```text
cats, chase, dogs, mice
```

Each document can then be represented as a vector of word counts.

This allows text to be processed using numerical techniques instead of working directly with raw sentences.

BoW is useful for:

- Text classification.
- Spam detection.
- Sentiment analysis.
- Document similarity.
- Information retrieval.
- Baseline machine learning models.

### 2. How Does Bag of Words Work?

Bag of Words generally follows three steps.

#### Step 1: Collect the Documents

Consider the following three documents:

```text
D1: cats chase small mice
D2: dogs chase cats
D3: mice like small spaces
```

Each document is a separate text sample.

#### Step 2: Create the Vocabulary

The vocabulary contains all unique words found across the documents.

```text
cats, chase, dogs, like, mice, small, spaces
```

For this example, the vocabulary is sorted alphabetically.

Each vocabulary word corresponds to one column in the numerical representation.

#### Step 3: Count the Words

Count how many times each vocabulary word appears in each document.

| Document | cats | chase | dogs | like | mice | small | spaces |
|---|---:|---:|---:|---:|---:|---:|---:|
| D1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| D2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| D3 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |

The resulting numerical table is called a **document-term matrix**.

Each row represents a document, and each column represents a vocabulary term.

### 3. Mathematical Representation

Suppose there are \(m\) documents and \(n\) unique words in the vocabulary.

The Bag of Words representation is a matrix:

\[
X \in \mathbb{R}^{m \times n}
\]

where:

- \(m\) is the number of documents.
- \(n\) is the number of unique vocabulary terms.
- \(X_{ij}\) is the count of word \(j\) in document \(i\).

For example:

\[
X =
\begin{bmatrix}
1 & 1 & 0 & 0 & 1 & 1 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1
\end{bmatrix}
\]

The columns follow the vocabulary order:

```text
cats, chase, dogs, like, mice, small, spaces
```

A value of `0` means the word does not appear in the document, while a positive value represents its frequency.

### 4. Implementing Bag of Words Manually

The following example uses Python's standard library and regular expressions to build a vocabulary and count matrix.

```python
## Bag of Words

import re
from collections import Counter

## Sample documents
documents = [
    "cats chase small mice",
    "dogs chase cats",
    "mice like small spaces"
]

## Tokenize documents
tokenized_documents = [
    re.findall(r"[a-z]+", document.lower())
    for document in documents
]

## Create the vocabulary
vocabulary = sorted({
    word
    for words in tokenized_documents
    for word in words
})

print("Vocabulary:", vocabulary)

## Create the count matrix
print("\nCount Matrix:")

for words in tokenized_documents:
    counts = Counter(words)
    print([counts[word] for word in vocabulary])
```

#### Expected output

```text
Vocabulary: ['cats', 'chase', 'dogs', 'like', 'mice', 'small', 'spaces']

Count Matrix:
[1, 1, 0, 0, 1, 1, 0]
[1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 1, 1]
```

#### Understanding the code

- `re.findall()` extracts alphabetic words from each document.
- `.lower()` converts text to lowercase.
- `set()` removes duplicate vocabulary words.
- `sorted()` creates a consistent alphabetical order.
- `Counter()` counts word occurrences in each document.
- The list comprehension constructs a numerical vector following the vocabulary order.

This implementation makes the relationship between vocabulary terms and matrix columns explicit.

### 5. Bag of Words Using Scikit-Learn

In practical machine learning projects, `CountVectorizer` from scikit-learn provides a convenient way to construct a Bag of Words representation.

Install scikit-learn if necessary:

```bash
python -m pip install scikit-learn
```

#### Example

```python
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "cats chase small mice",
    "dogs chase cats",
    "mice like small spaces"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:", vectorizer.get_feature_names_out())
print("\nCount Matrix:")
print(X.toarray())
```

#### Expected output

```text
Vocabulary: ['cats' 'chase' 'dogs' 'like' 'mice' 'small' 'spaces']

Count Matrix:
[[1 1 0 0 1 1 0]
 [1 1 1 0 0 0 0]
 [0 0 0 1 1 1 1]]
```

`CountVectorizer` typically lowercases text and uses its tokenization rules to extract terms. Its default token pattern differs from the simple regular expression used in the manual implementation.

For larger datasets, the vectorizer stores a sparse matrix, which is generally more memory-efficient than converting the complete matrix to a dense NumPy array.

### 6. Binary Bag of Words vs. Word Counts

Bag of Words can represent word occurrence in different ways.

#### Count-Based Representation

Each value represents the number of times a word appears.

```text
Document: cats cats chase mice
```

The counts are:

```text
cats = 2
chase = 1
mice = 1
```

#### Binary Representation

Each value indicates whether a word appears at least once.

```text
cats = 1
chase = 1
mice = 1
```

With scikit-learn, binary representation can be enabled using `binary=True`.

```python
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "cats cats chase mice",
    "dogs chase cats"
]

vectorizer = CountVectorizer(binary=True)

X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

Binary representation can be useful when the presence of a word matters more than its frequency.

### 7. Limitations of Bag of Words

#### 7.1 It Ignores Word Order

Consider:

```text
Document 1: dogs chase cats
Document 2: cats chase dogs
```

Both documents contain the same words with the same frequencies. Standard Bag of Words therefore produces identical vectors for both documents.

However, the meanings of the sentences differ.

#### 7.2 It Does Not Understand Meaning

Words such as `car` and `automobile` are treated as separate vocabulary terms, even though they have similar meanings.

#### 7.3 It Can Produce High-Dimensional Matrices

Large collections of documents may contain thousands or millions of unique terms. This creates a large feature space.

#### 7.4 It Produces Sparse Matrices

Most documents contain only a small fraction of the entire vocabulary, so most matrix entries are zero.

Sparse matrix representations help reduce memory usage.

#### 7.5 It Does Not Understand Context

The word `bank` may refer to a financial institution or the side of a river. Standard BoW treats both occurrences as the same token.

#### 7.6 Vocabulary Is Limited to the Fitted Data

A word not present in the fitted vocabulary cannot contribute a new feature to that vectorizer. During inference, unseen words are generally ignored.

For machine learning, fit the vectorizer on training data and reuse it for validation, test, and future data. This preserves a consistent vocabulary and avoids data leakage.

### 8. Bag of Words vs. Other Text Representation Techniques

| Technique | Main idea | Word order | Contextual meaning |
|---|---|---|---|
| Bag of Words | Counts vocabulary terms | Ignored | Not represented directly |
| N-Grams | Represents sequences of adjacent tokens | Partially captured | Limited |
| TF-IDF | Weights terms by frequency and document rarity | Usually ignored | Not represented directly |
| Word2Vec | Learns dense word vectors from context | Used during training | Captures some word relationships |
| Transformer embeddings | Produces context-sensitive representations | Captured through model architecture | Captured to varying degrees |

Bag of Words is often a useful baseline because it is simple, interpretable, and computationally efficient.

### 9. Practical Applications

#### Spam Detection

Words such as `winner`, `prize`, and `claim` can become features for a spam classifier.

#### Sentiment Analysis

Word-count features can help a classifier learn patterns associated with positive and negative reviews, although BoW alone does not reliably capture negation or context.

#### Document Classification

BoW can represent documents numerically for tasks such as topic classification and categorization.

#### Information Retrieval

Word-count representations can help compare documents and search queries.

#### News Categorization

A classifier can use vocabulary counts to distinguish between categories such as sports, technology, and business.

### 10. Exercises

#### Exercise 1: Build a Vocabulary

Consider the documents:

```text
D1: cat dog cat
D2: dog bird
```

Tasks:

1. Convert the documents into lowercase tokens.
2. Create a sorted vocabulary.
3. Construct the document-term count matrix.

Expected vocabulary:

```text
['bird', 'cat', 'dog']
```

#### Exercise 2: Calculate the Count Matrix

Using the vocabulary from Exercise 1, calculate the matrix manually.

Remember that every row must follow the same vocabulary order.

#### Exercise 3: Add Another Document

Add the document:

```text
D3: bird cat fish
```

Recalculate the vocabulary and document-term matrix. Observe how the addition of `fish` changes the feature space.

#### Exercise 4: Count vs. Binary Representation

Use this document:

```text
python python machine learning
```

Create both a count-based representation and a binary representation.

Explain why their values differ.

#### Exercise 5: Word Order

Compare:

```text
D1: dogs chase cats
D2: cats chase dogs
```

Explain why standard Bag of Words cannot distinguish the sentence order.

#### Exercise 6: Use Scikit-Learn

Use `CountVectorizer` on at least four documents.

Print the vocabulary and count matrix, then explain the meaning of each row and column.

### 11. Points to Remember

- Bag of Words converts text into numerical word-frequency features.
- The vocabulary contains unique terms from the fitted documents.
- Each row represents a document, and each column represents a vocabulary term.
- Standard BoW ignores word order and does not directly capture semantic meaning.
- Binary BoW records word presence, while count-based BoW records frequency.
- `CountVectorizer` provides a convenient implementation in scikit-learn.
- Sparse matrices are useful for large text datasets.
- Always reuse the vocabulary learned from training data when transforming new documents.

### 12. Related Topics

- [Text Cleaning](../../01_Preprocessing/01_Basics_and_Cleaning/README.md#text-cleaning) — Preparing raw text for further processing.
- [Tokenization](../../01_Preprocessing/02_Tokenization/README.md) — Splitting text into tokens.
- [N-Grams](README.md#n-grams) — Representing sequences of adjacent words.
- [TF-IDF](../02_TF_IDF/README.md) — Weighting terms according to their frequency and document rarity.
- [Word2Vec](../03_Word_Embeddings/README.md#word2vec) — Learning dense word representations from context.

**Final takeaway:** Bag of Words is a foundational NLP technique that transforms documents into numerical word-count vectors. It is an excellent starting point for understanding how text becomes machine-learning input, while its limitations motivate more advanced representation techniques.

---

## N-Grams

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

### 1. Types of N-Grams

#### 1.1 Unigrams

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

#### 1.2 Bigrams

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

#### 1.3 Trigrams

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

#### 1.4 Four-Grams

A four-gram contains four consecutive tokens, so `n = 4`.

Four-grams:

```python
[
    ("natural", "language", "processing", "is"),
    ("language", "processing", "is", "interesting")
]
```

Longer N-grams can represent more specific phrases, but they generally require more data to occur frequently.

#### 1.5 General N-Grams

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

### 2. Mathematical Formula

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

### 3. How N-Grams Work

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

### 4. Implementing N-Grams Using Python

The following example uses Python's standard library and requires no third-party packages.

```python
## N-Grams

import re

text = "Natural language models learn from sequences of words."

## Convert text to lowercase and tokenize
tokens = re.findall(r"[a-z]+", text.lower())

print("Original Text:", text)
print("Tokens:", tokens)

## Generate unigrams
unigrams = [
    tuple(tokens[index:index + 1])
    for index in range(len(tokens))
]

print("\nUnigrams:")
print(unigrams)

## Generate bigrams
bigrams = [
    tuple(tokens[index:index + 2])
    for index in range(len(tokens) - 1)
]

print("\nBigrams:")
print(bigrams)

## Generate trigrams
trigrams = [
    tuple(tokens[index:index + 3])
    for index in range(len(tokens) - 2)
]

print("\nTrigrams:")
print(trigrams)

## Generate four-grams
n = 4

n_grams = [
    tuple(tokens[index:index + n])
    for index in range(len(tokens) - n + 1)
]

print(f"\n{n}-Grams:")
print(n_grams)

## Display the number of occurrences
print("\nNumber of Unigrams:", len(unigrams))
print("Number of Bigrams:", len(bigrams))
print("Number of Trigrams:", len(trigrams))
print(f"Number of {n}-Grams:", len(n_grams))
```

#### Expected output

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

### 5. Generating N-Grams Using NLTK

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

## Generate bigrams
bigrams = list(ngrams(tokens, 2))

## Generate trigrams
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

### 6. Counting N-Gram Frequencies

N-gram frequency counts show how often each sequence occurs in a text.

Example:

```python
import re
from collections import Counter

text = "I love Python. I love learning Python."

## Tokenize the text
tokens = re.findall(r"[a-z]+", text.lower())

## Generate bigrams
bigrams = [
    tuple(tokens[index:index + 2])
    for index in range(len(tokens) - 1)
]

## Count bigram occurrences
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

### 7. N-Grams vs. Bag of Words

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

### 8. Advantages and Limitations

#### Advantages

- Captures local word order.
- Represents common phrases as features.
- Is relatively easy to implement.
- Can improve traditional text classification models.
- Supports frequency analysis and statistical language modeling.

#### Limitations

- The number of possible features can grow rapidly.
- Longer N-grams are often less frequent.
- Unseen sequences may not appear in the vocabulary.
- N-grams do not fully represent sentence meaning.
- Tokenization and punctuation handling affect the results.
- Fixed-size N-grams do not directly capture long-distance relationships.

### 9. Practical Applications

#### Search Engines

Bigrams and trigrams can help identify phrases in search queries and documents.

#### Text Classification

N-gram features can help distinguish documents using word combinations rather than isolated words.

#### Autocomplete

N-gram language models can estimate likely next words based on preceding tokens.

#### Spam Detection

Frequent phrases can help identify patterns associated with spam messages.

#### Language Modeling

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

### 10. Common Mistakes

- **Using the wrong value of n:** Bigrams require `n=2`, and trigrams require `n=3`.
- **Ignoring tokenization:** Different tokenization methods produce different N-grams.
- **Assuming N-grams are unique:** The same sequence can occur multiple times.
- **Confusing occurrences with unique sequences:** Frequency and vocabulary size are different measurements.
- **Choosing very large N-grams without enough data:** Many features may occur rarely.
- **Ignoring punctuation decisions:** Including punctuation changes the resulting sequences.
- **Assuming N-grams understand meaning:** They capture local patterns, not complete semantics.

### 11. Exercises

#### Exercise 1: Generate Unigrams

Given the sentence:

```text
I love learning Python
```

Write down all unigrams.

#### Exercise 2: Generate Bigrams

Use the same sentence and list all bigrams.

#### Exercise 3: Generate Trigrams

List all trigrams and compare their number with the number of bigrams.

#### Exercise 4: General N-Grams

Use the sentence:

```text
Natural language processing is interesting
```

Generate four-grams and five-grams using Python.

#### Exercise 5: Count Unique Bigrams

Compare the sentences:

```text
I love Python and I love coding.
I love learning and love Python.
```

Tokenize both sentences, generate bigrams, and count the total and unique bigrams.

#### Exercise 6: Compare with Bag of Words

Compare:

```text
dogs chase cats
cats chase dogs
```

Explain why their unigram counts are identical but their bigram sequences differ.

#### Exercise 7: Experiment with N

Use a sentence containing eight tokens. Generate N-grams for `n = 1, 2, 3, 4, 5`, then verify the formula for the number of occurrences.

### 12. Related Topics

- [Bag of Words](README.md#bag-of-words-bow) — Representing documents using word counts.
- [TF-IDF](../02_TF_IDF/README.md) — Weighting words according to their frequency and document rarity.
- [Word2Vec](../03_Word_Embeddings/README.md#word2vec) — Learning word representations from contextual patterns.
- [Tokenization](../../01_Preprocessing/02_Tokenization/README.md) — Splitting text into tokens.

### 13. Points to Remember

- An N-gram is a sequence of `n` adjacent tokens.
- Unigrams contain one token, bigrams two, and trigrams three.
- N-grams preserve local word order.
- The number of contiguous N-gram occurrences is `max(0, T - n + 1)`.
- Larger N-grams capture more local context but are often less frequent.
- Repeated N-grams can occur multiple times.
- N-grams can be generated manually or with NLTK.
- N-grams are useful features but do not fully capture sentence meaning.

**Final takeaway:** N-grams extend basic word-count representations by capturing local word order. They are a useful bridge between simple Bag of Words features and more advanced language representations.
