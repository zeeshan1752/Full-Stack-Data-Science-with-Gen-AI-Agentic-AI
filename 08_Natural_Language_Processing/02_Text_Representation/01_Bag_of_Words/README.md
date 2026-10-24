# Bag of Words (BoW)

Bag of Words (BoW) is a text representation technique in Natural Language Processing (NLP) that converts text into numerical features based on the occurrence or frequency of words.

It creates a vocabulary of unique words from a collection of documents and represents each document using the counts of those words.

BoW is simple, easy to understand, and commonly used as a baseline for text classification and other NLP tasks.

## 1. Why Is Bag of Words Important?

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

## 2. How Does Bag of Words Work?

Bag of Words generally follows three steps.

### Step 1: Collect the Documents

Consider the following three documents:

```text
D1: cats chase small mice
D2: dogs chase cats
D3: mice like small spaces
```

Each document is a separate text sample.

### Step 2: Create the Vocabulary

The vocabulary contains all unique words found across the documents.

```text
cats, chase, dogs, like, mice, small, spaces
```

For this example, the vocabulary is sorted alphabetically.

Each vocabulary word corresponds to one column in the numerical representation.

### Step 3: Count the Words

Count how many times each vocabulary word appears in each document.

| Document | cats | chase | dogs | like | mice | small | spaces |
|---|---:|---:|---:|---:|---:|---:|---:|
| D1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| D2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| D3 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |

The resulting numerical table is called a **document-term matrix**.

Each row represents a document, and each column represents a vocabulary term.

## 3. Mathematical Representation

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

## 4. Implementing Bag of Words Manually

The following example uses Python's standard library and regular expressions to build a vocabulary and count matrix.

```python
# Bag of Words

import re
from collections import Counter

# Sample documents
documents = [
    "cats chase small mice",
    "dogs chase cats",
    "mice like small spaces"
]

# Tokenize documents
tokenized_documents = [
    re.findall(r"[a-z]+", document.lower())
    for document in documents
]

# Create the vocabulary
vocabulary = sorted({
    word
    for words in tokenized_documents
    for word in words
})

print("Vocabulary:", vocabulary)

# Create the count matrix
print("\nCount Matrix:")

for words in tokenized_documents:
    counts = Counter(words)
    print([counts[word] for word in vocabulary])
```

### Expected output

```text
Vocabulary: ['cats', 'chase', 'dogs', 'like', 'mice', 'small', 'spaces']

Count Matrix:
[1, 1, 0, 0, 1, 1, 0]
[1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 1, 1]
```

### Understanding the code

- `re.findall()` extracts alphabetic words from each document.
- `.lower()` converts text to lowercase.
- `set()` removes duplicate vocabulary words.
- `sorted()` creates a consistent alphabetical order.
- `Counter()` counts word occurrences in each document.
- The list comprehension constructs a numerical vector following the vocabulary order.

This implementation makes the relationship between vocabulary terms and matrix columns explicit.

## 5. Bag of Words Using Scikit-Learn

In practical machine learning projects, `CountVectorizer` from scikit-learn provides a convenient way to construct a Bag of Words representation.

Install scikit-learn if necessary:

```bash
python -m pip install scikit-learn
```

### Example

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

### Expected output

```text
Vocabulary: ['cats' 'chase' 'dogs' 'like' 'mice' 'small' 'spaces']

Count Matrix:
[[1 1 0 0 1 1 0]
 [1 1 1 0 0 0 0]
 [0 0 0 1 1 1 1]]
```

`CountVectorizer` typically lowercases text and uses its tokenization rules to extract terms. Its default token pattern differs from the simple regular expression used in the manual implementation.

For larger datasets, the vectorizer stores a sparse matrix, which is generally more memory-efficient than converting the complete matrix to a dense NumPy array.

## 6. Binary Bag of Words vs. Word Counts

Bag of Words can represent word occurrence in different ways.

### Count-Based Representation

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

### Binary Representation

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

## 7. Limitations of Bag of Words

### 7.1 It Ignores Word Order

Consider:

```text
Document 1: dogs chase cats
Document 2: cats chase dogs
```

Both documents contain the same words with the same frequencies. Standard Bag of Words therefore produces identical vectors for both documents.

However, the meanings of the sentences differ.

### 7.2 It Does Not Understand Meaning

Words such as `car` and `automobile` are treated as separate vocabulary terms, even though they have similar meanings.

### 7.3 It Can Produce High-Dimensional Matrices

Large collections of documents may contain thousands or millions of unique terms. This creates a large feature space.

### 7.4 It Produces Sparse Matrices

Most documents contain only a small fraction of the entire vocabulary, so most matrix entries are zero.

Sparse matrix representations help reduce memory usage.

### 7.5 It Does Not Understand Context

The word `bank` may refer to a financial institution or the side of a river. Standard BoW treats both occurrences as the same token.

### 7.6 Vocabulary Is Limited to the Fitted Data

A word not present in the fitted vocabulary cannot contribute a new feature to that vectorizer. During inference, unseen words are generally ignored.

For machine learning, fit the vectorizer on training data and reuse it for validation, test, and future data. This preserves a consistent vocabulary and avoids data leakage.

## 8. Bag of Words vs. Other Text Representation Techniques

| Technique | Main idea | Word order | Contextual meaning |
|---|---|---|---|
| Bag of Words | Counts vocabulary terms | Ignored | Not represented directly |
| N-Grams | Represents sequences of adjacent tokens | Partially captured | Limited |
| TF-IDF | Weights terms by frequency and document rarity | Usually ignored | Not represented directly |
| Word2Vec | Learns dense word vectors from context | Used during training | Captures some word relationships |
| Transformer embeddings | Produces context-sensitive representations | Captured through model architecture | Captured to varying degrees |

Bag of Words is often a useful baseline because it is simple, interpretable, and computationally efficient.

## 9. Practical Applications

### Spam Detection

Words such as `winner`, `prize`, and `claim` can become features for a spam classifier.

### Sentiment Analysis

Word-count features can help a classifier learn patterns associated with positive and negative reviews, although BoW alone does not reliably capture negation or context.

### Document Classification

BoW can represent documents numerically for tasks such as topic classification and categorization.

### Information Retrieval

Word-count representations can help compare documents and search queries.

### News Categorization

A classifier can use vocabulary counts to distinguish between categories such as sports, technology, and business.

## 10. Exercises

### Exercise 1: Build a Vocabulary

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

### Exercise 2: Calculate the Count Matrix

Using the vocabulary from Exercise 1, calculate the matrix manually.

Remember that every row must follow the same vocabulary order.

### Exercise 3: Add Another Document

Add the document:

```text
D3: bird cat fish
```

Recalculate the vocabulary and document-term matrix. Observe how the addition of `fish` changes the feature space.

### Exercise 4: Count vs. Binary Representation

Use this document:

```text
python python machine learning
```

Create both a count-based representation and a binary representation.

Explain why their values differ.

### Exercise 5: Word Order

Compare:

```text
D1: dogs chase cats
D2: cats chase dogs
```

Explain why standard Bag of Words cannot distinguish the sentence order.

### Exercise 6: Use Scikit-Learn

Use `CountVectorizer` on at least four documents.

Print the vocabulary and count matrix, then explain the meaning of each row and column.

## 11. Points to Remember

- Bag of Words converts text into numerical word-frequency features.
- The vocabulary contains unique terms from the fitted documents.
- Each row represents a document, and each column represents a vocabulary term.
- Standard BoW ignores word order and does not directly capture semantic meaning.
- Binary BoW records word presence, while count-based BoW records frequency.
- `CountVectorizer` provides a convenient implementation in scikit-learn.
- Sparse matrices are useful for large text datasets.
- Always reuse the vocabulary learned from training data when transforming new documents.

## 12. Related Topics

- [Text Cleaning](../../01_Text_Preprocessing/02_Text_Cleaning/README.md) — Preparing raw text for further processing.
- [Tokenization](../../01_Text_Preprocessing/04_Tokenization/README.md) — Splitting text into tokens.
- [N-Grams](../02_N_Grams/README.md) — Representing sequences of adjacent words.
- [TF-IDF](../03_TF_IDF/README.md) — Weighting terms according to their frequency and document rarity.
- [Word2Vec](../06_Word2Vec/README.md) — Learning dense word representations from context.

**Final takeaway:** Bag of Words is a foundational NLP technique that transforms documents into numerical word-count vectors. It is an excellent starting point for understanding how text becomes machine-learning input, while its limitations motivate more advanced representation techniques.
