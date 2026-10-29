# TF-IDF (Term Frequency–Inverse Document Frequency)

## 1. Introduction

**TF-IDF (Term Frequency–Inverse Document Frequency)** is a text representation technique used in Natural Language Processing (NLP) to convert text into numerical values.

It assigns a weight to each word based on two factors:

- **Term Frequency (TF):** How frequently a word appears in a document.
- **Inverse Document Frequency (IDF):** How uncommon the word is across a collection of documents.

The main idea is that a word is more informative when it appears frequently in a particular document but is relatively uncommon across the entire collection.

For example, consider a collection of product reviews:

- "This phone has a good camera."
- "This phone has a good battery."
- "The camera quality is excellent."

Words such as `this` and `good` may occur in multiple documents and provide limited information. Words such as `battery` or `excellent` may be more useful for distinguishing particular reviews.

TF-IDF reduces the relative importance of common terms and gives more weight to terms that help distinguish documents.

## 2. Why Do We Need TF-IDF?

A simple Bag of Words (BoW) model counts how often each word appears. However, it does not automatically account for how common a word is across all documents.

Consider these sentences:

- D1: `Python is easy to learn`
- D2: `Python is useful for data science`
- D3: `Machine learning uses Python`

Words such as `Python` appear in all three documents, while `easy` appears in only one.

TF-IDF helps represent this difference by considering both the frequency of a word within a document and its distribution across the collection.

### Main advantages

- Gives lower relative importance to terms that appear in many documents.
- Highlights terms that help distinguish one document from another.
- Produces numerical feature vectors suitable for machine learning.
- Supports information retrieval, document ranking, and text classification.

## 3. Understanding Term Frequency (TF)

Term Frequency measures how frequently a term occurs in a document.

A simple raw-count version is:

$$
TF(t,d)=\text{Count of term }t\text{ in document }d
$$

For example:

Document: `python is easy python is useful`

| Word | Frequency |
|---|---:|
| python | 2 |
| is | 2 |
| easy | 1 |
| useful | 1 |

The raw term frequency of `python` is 2.

Another common definition uses the proportion of tokens occupied by the term:

$$
TF(t,d)=\frac{\text{Count of }t\text{ in }d}{\text{Total tokens in }d}
$$

The document contains six tokens, so the normalized frequency of `python` is:

$$
TF(\text{python},d)=\frac{2}{6}=0.3333
$$

**Important:** Different implementations use different TF conventions. Some use raw counts, while others use normalized or logarithmically scaled frequencies.

## 4. Understanding Inverse Document Frequency (IDF)

Inverse Document Frequency measures how widely a term is distributed across a document collection.

A word appearing in almost every document usually has less power to distinguish one document from another. A word appearing in only a few documents can be more informative.

A commonly used smoothed IDF formula is:

$$
IDF(t)=\log\left(\frac{N+1}{DF(t)+1}\right)+1
$$

Where:

- \(N\) = total number of documents.
- \(DF(t)\) = number of documents containing term \(t\).
- \(\log\) = logarithm, commonly the natural logarithm in scikit-learn.

### Example

Suppose there are four documents:

| Term | Documents containing the term | Document frequency |
|---|---|---:|
| python | D1, D2, D3, D4 | 4 |
| camera | D1, D2 | 2 |
| robotics | D4 | 1 |

For `python`:

$$
IDF(\text{python})=\log\left(\frac{4+1}{4+1}\right)+1=1
$$

For `camera`:

$$
IDF(\text{camera})=\log\left(\frac{5}{3}\right)+1\approx1.5108
$$

For `robotics`:

$$
IDF(\text{robotics})=\log\left(\frac{5}{2}\right)+1\approx1.9163
$$

The rarer term `robotics` receives a higher IDF value than `camera` or `python`.

The smoothing prevents division by zero and keeps the IDF defined for terms with different document frequencies.

## 5. TF-IDF Formula

TF-IDF combines Term Frequency and Inverse Document Frequency.

$$
TFIDF(t,d)=TF(t,d)\times IDF(t)
$$

A higher score generally indicates that a term is relatively important to a document under the chosen TF-IDF convention.

### Worked example

Suppose the term `camera` occurs twice in a document containing ten tokens. It appears in two of four documents.

Using normalized TF and smoothed IDF:

$$
TF(\text{camera},d)=\frac{2}{10}=0.2
$$

$$
IDF(\text{camera})=\log\left(\frac{4+1}{2+1}\right)+1
$$

$$
IDF(\text{camera})\approx1.5108
$$

Therefore:

$$
TFIDF(\text{camera},d)=0.2\times1.5108
$$

$$
TFIDF(\text{camera},d)\approx0.3022
$$

This score combines the term's frequency in the document with its rarity across the collection.

## 6. TF-IDF Using Python

We can calculate TF-IDF using scikit-learn's `TfidfVectorizer`.

### Install the library

```bash
python -m pip install -U scikit-learn
```

### Example 1: Basic TF-IDF

```python
# TF-IDF

from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Python is easy to learn",
    "Python is useful for data science",
    "Machine learning uses Python"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
```

### Explanation

- `TfidfVectorizer()` creates a TF-IDF vectorizer.
- `fit_transform(documents)` learns the vocabulary and calculates TF-IDF values.
- `get_feature_names_out()` returns the vocabulary in column order.
- `toarray()` converts the sparse matrix into a regular NumPy array for display.

The matrix contains one row per document and one column per vocabulary term.

**Note:** scikit-learn applies its own IDF convention and L2-normalizes document vectors by default. Therefore, its final values may differ from manually calculated TF-IDF scores.

### Example 2: Display TF-IDF as a table

```python
# Display TF-IDF Values

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love Python",
    "I love machine learning",
    "Python is useful for machine learning"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=vectorizer.get_feature_names_out(),
    index=["Document 1", "Document 2", "Document 3"]
)

print(df.round(3))
```

This table makes it easier to compare the relative weight of each word across the documents.

Install pandas if needed:

```bash
python -m pip install -U pandas
```

## 7. Understanding the TF-IDF Matrix

Suppose the documents are:

- D1: `cat eats fish`
- D2: `cat drinks milk`

The vocabulary is:

`cat`, `drinks`, `eats`, `fish`, `milk`

The TF-IDF matrix has this general structure:

| Document | cat | drinks | eats | fish | milk |
|---|---:|---:|---:|---:|---:|
| D1 | Weight | 0 | Weight | Weight | 0 |
| D2 | Weight | Weight | 0 | 0 | Weight |

The actual values depend on the TF, IDF, and normalization settings.

A zero means the term is absent from that document. A nonzero value represents the term's calculated weight.

## 8. TF-IDF vs. Bag of Words

| Feature | Bag of Words | TF-IDF |
|---|---|---|
| Main purpose | Represents word counts | Represents weighted word importance |
| Common words | Can receive high counts | Usually receive lower relative weights |
| Rare words | Represented by their counts | Can receive higher IDF weights |
| Output | Numerical feature matrix | Numerical feature matrix |
| Captures word order | No, in the standard unigram model | No, in the standard unigram model |
| Typical uses | Text classification and counting | Search ranking, classification, document similarity |

TF-IDF is an alternative weighting method for a bag-of-words-style representation. It does not inherently understand the meaning of words or the order in which they appear.

## 9. TF-IDF vs. N-Grams vs. Word2Vec

| Technique | What it represents | Main characteristic |
|---|---|---|
| Bag of Words | Word counts | Counts terms |
| TF-IDF | Weighted word importance | Reduces the relative influence of widespread terms |
| N-Grams | Sequences of adjacent tokens | Can represent local word order |
| Word2Vec | Dense word vectors | Learns word representations from context |

For example, TF-IDF with unigrams treats `machine` and `learning` as separate features. Including bigrams can introduce a feature such as `machine learning`.

Word2Vec differs because it learns dense vector representations rather than document-level TF-IDF weights.

## 10. Applications of TF-IDF

### Search engines

TF-IDF can help rank documents by the importance of query terms, although modern search engines use many additional signals and methods.

### Document similarity

TF-IDF vectors can be compared using cosine similarity to estimate how similar two documents are in terms of their weighted vocabulary.

### Text classification

TF-IDF features can be supplied to machine learning algorithms such as Logistic Regression, Naive Bayes, and Support Vector Machines.

### Spam detection

Words that distinguish spam messages from ordinary messages can contribute useful features to a spam classifier.

### News and article categorization

TF-IDF can help represent documents for topic classification, clustering, and retrieval.

## 11. Common Mistakes

1. **Confusing term frequency with document frequency.** TF measures occurrences in one document; DF counts documents containing the term.
2. **Assuming rare words are always meaningful.** Rare words can also be misspellings, noise, or irrelevant identifiers.
3. **Ignoring preprocessing.** Inconsistent casing, punctuation, and tokenization can change the vocabulary.
4. **Expecting semantic understanding.** TF-IDF does not automatically recognize synonyms or understand context.
5. **Fitting on test data.** Fit the vectorizer on training data only, then transform validation and test data with the same fitted vectorizer.
6. **Comparing incompatible scores.** Different smoothing, TF conventions, and normalization settings can produce different values.
7. **Assuming every document vector has the same magnitude.** By default, scikit-learn applies L2 normalization, but other implementations may use different settings.

## 12. Points to Remember

- TF-IDF stands for Term Frequency–Inverse Document Frequency.
- TF measures a term's frequency within a document.
- IDF measures how uncommon a term is across a collection.
- TF-IDF combines both measurements into a term weight.
- The exact formula and final values depend on the implementation.
- `TfidfVectorizer` is a convenient way to generate TF-IDF features in Python.
- Fit the vectorizer on training data and reuse it to transform unseen data.
- TF-IDF is useful for text classification, retrieval, and document similarity, but it does not independently understand word meaning.

## 13. Related Topics

- [Bag of Words](../01_Bag_of_Words_and_NGrams/README.md#bag-of-words-bow)
- [N-Grams](../01_Bag_of_Words_and_NGrams/README.md#n-grams)
- [Text Tokenization](../../01_Preprocessing/02_Tokenization/README.md)
- [scikit-learn example](tfidf_sklearn.py)

## 14. References

- [scikit-learn: TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [scikit-learn: Feature Extraction from Text](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [scikit-learn: CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
