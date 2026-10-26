# Word Embeddings

## 1. Introduction to Word Embeddings

Word embeddings are numerical representations of words in the form of vectors. Machine learning models cannot directly understand text, so words must be converted into numerical values before they can be processed.

Traditional methods such as Bag of Words (BoW) and TF-IDF represent words using sparse vectors. Word embeddings represent words using dense vectors, where each word is mapped to a fixed-size vector of numerical values.

For example:

```python
# Example of a word embedding
cat = [0.21, 0.45, -0.18, 0.72]
dog = [0.19, 0.41, -0.12, 0.68]
car = [-0.55, 0.13, 0.82, -0.24]
```

These are illustrative vectors, not actual pretrained embeddings.

The vectors for `cat` and `dog` are relatively similar because these words have related meanings, while `car` may have a different representation.

### Why Do We Need Word Embeddings?

Consider the following sentences:

- The cat is sleeping.
- The dog is sleeping.
- I am driving a car.

Traditional text representations can identify which words occur in each sentence, but they do not inherently capture semantic relationships between words.

Word embeddings help models learn relationships between words based on their usage and surrounding context.

### Key Characteristics

- Each word is represented as a numerical vector.
- Vectors are usually dense and contain real-valued numbers.
- Similar words can have similar vector representations.
- Embeddings can capture semantic and syntactic relationships.
- Embeddings are useful in NLP tasks such as sentiment analysis, text classification, search, and machine translation.

---

## 2. From Text to Numerical Representation

Before understanding word embeddings, it is useful to understand the text representation methods that came before them.

### 2.1 One-Hot Encoding

One-hot encoding represents each word using a vector whose length equals the vocabulary size. Only one position contains `1`; all other positions contain `0`.

Suppose the vocabulary is:

```python
vocabulary = ["cat", "dog", "car"]
```

The representations are:

| Word | Vector |
|---|---|
| cat | `[1, 0, 0]` |
| dog | `[0, 1, 0]` |
| car | `[0, 0, 1]` |

One-hot encoding is simple, but it has some limitations:

- The vector becomes large when the vocabulary is large.
- Most values are zero, making it sparse.
- Different words have the same distance from one another under the usual one-hot representation.
- It does not directly capture semantic similarity.

### 2.2 Bag of Words

Bag of Words represents a document using word occurrence counts.

Consider:

```text
D1 = "cat dog cat"
D2 = "dog bird"
```

Vocabulary:

```text
bird, cat, dog
```

The resulting count vectors are:

| Document | bird | cat | dog |
|---|---:|---:|---:|
| D1 | 0 | 2 | 1 |
| D2 | 1 | 0 | 1 |

Bag of Words is useful for representing text, but it does not inherently capture the meaning or context of words.

### 2.3 TF-IDF

TF-IDF stands for **Term Frequency–Inverse Document Frequency**. It gives higher importance to terms that are frequent in a document but relatively uncommon across the document collection.

The general formula is:

TF-IDF = Term Frequency × Inverse Document Frequency

A common IDF formula is:

IDF(t) = log(N / df(t))

Where:

- `N` is the total number of documents.
- `df(t)` is the number of documents containing term `t`.

TF-IDF improves upon simple word counts by reducing the importance of words that occur in many documents. However, it does not inherently learn semantic relationships between words.

---

## 3. What Makes Word Embeddings Different?

Word embeddings use a dense vector to represent a word.

For example:

```python
cat = [0.2, 0.5, -0.1, 0.7]
dog = [0.3, 0.4, -0.2, 0.6]
car = [-0.6, 0.1, 0.8, -0.3]
```

Each number represents one dimension in the learned vector space. These dimensions generally do not have simple human-readable meanings.

| Feature | One-Hot Encoding | Bag of Words | TF-IDF | Word Embeddings |
|---|---|---|---|---|
| Representation | Sparse vector | Sparse count vector | Sparse weighted vector | Dense vector |
| Captures word counts | No | Yes | Weighted counts | Not directly |
| Learns semantic relationships | No | No | No | Often, depending on training |
| Vector size | Vocabulary size | Vocabulary size | Vocabulary size | Usually a chosen embedding dimension |
| Context-dependent meaning | No | No | No | Depends on the embedding method |
| Typical examples | One-hot vectors | CountVectorizer | TfidfVectorizer | Word2Vec, GloVe |

**Important:** Word embeddings do not automatically understand meaning like a human. They learn statistical patterns and relationships from data.

---

## 4. Dense Vectors and Embedding Dimensions

An embedding dimension is the number of numerical values used to represent each word.

For example:

```python
word_embedding = [0.25, -0.14, 0.62, 0.38]
```

This vector has four dimensions.

A model might use 50, 100, 300, or another number of dimensions. Modern neural models can use much larger embedding dimensions.

### Embedding Matrix

If a vocabulary contains 1,000 words and each word has a 100-dimensional embedding, the embedding matrix has the shape:

```text
(1000, 100)
```

Each row represents one word, and each column represents one embedding dimension.

The number of trainable values in this matrix is:

1,000 × 100 = 100,000

### Python Example

```python
import numpy as np

embedding_matrix = np.array([
    [0.2, 0.5, -0.1],
    [0.3, 0.4, -0.2],
    [-0.6, 0.1, 0.8]
])

print("Embedding matrix:")
print(embedding_matrix)

print("Shape:", embedding_matrix.shape)
print("Number of values:", embedding_matrix.size)
```

Output:

```text
Embedding matrix:
[[ 0.2  0.5 -0.1]
 [ 0.3  0.4 -0.2]
 [-0.6  0.1  0.8]]
Shape: (3, 3)
Number of values: 9
```

This example uses a small, manually created matrix for demonstration.

---

## 5. Vocabulary and Word-to-Index Mapping

An embedding model generally needs a way to map each word to an integer index. The index is used to retrieve that word's vector from the embedding matrix.

Example:

```python
vocabulary = {
    "cat": 0,
    "dog": 1,
    "car": 2
}

embedding_matrix = [
    [0.2, 0.5, -0.1],
    [0.3, 0.4, -0.2],
    [-0.6, 0.1, 0.8]
]

word = "dog"
index = vocabulary[word]

print("Word:", word)
print("Index:", index)
print("Embedding:", embedding_matrix[index])
```

Output:

```text
Word: dog
Index: 1
Embedding: [0.3, 0.4, -0.2]
```

The index is not the embedding itself. It is used to look up the corresponding vector.

In a real system, the vocabulary and embedding matrix are typically created or learned as part of the model pipeline.

---

## 6. How Are Word Embeddings Learned?

Word embeddings are commonly learned from large text collections. During training, a model adjusts vector values to perform a learning task, such as predicting a word from its context or predicting surrounding words from a target word.

The basic intuition is that words appearing in similar contexts often acquire related representations.

For example:

```text
The cat drinks milk.
The dog drinks water.
```

The words `cat` and `dog` appear in similar grammatical positions. A model trained on enough text may learn that they share some contextual properties.

### Distributional Hypothesis

The distributional hypothesis is the idea that words occurring in similar contexts tend to have similar meanings or usage.

Word2Vec uses this principle to learn word vectors by predicting relationships between words and their contexts.

**Note:** Similar contexts do not guarantee identical meanings. Words can be related, opposite, or used in different senses despite sharing contexts.

---

## 7. Word2Vec

Word2Vec is a popular method for learning word embeddings. It was introduced by researchers at Google and is commonly associated with two training architectures:

1. Continuous Bag of Words (CBOW)
2. Skip-gram

Word2Vec learns dense word vectors by using the surrounding words in a text corpus.

### 7.1 Continuous Bag of Words (CBOW)

CBOW predicts a target word using its surrounding context words.

Example sentence:

```text
I love learning Python
```

With a suitable context window, the surrounding words help the model predict a missing target word.

Conceptually:

```text
Context words → CBOW model → Target word
```

CBOW is often computationally efficient and works well for many frequent words.

### 7.2 Skip-gram

Skip-gram predicts surrounding context words from a target word.

Conceptually:

```text
Target word → Skip-gram model → Context words
```

For the same sentence, a target such as `learning` may be used to predict nearby words such as `love` and `Python`, depending on the selected context window.

Skip-gram is often useful for learning representations of less frequent words, although actual performance depends on the corpus and training configuration.

### CBOW vs Skip-gram

| Feature | CBOW | Skip-gram |
|---|---|---|
| Main task | Predict target word | Predict context words |
| Input | Surrounding context | Target word |
| Output | Target word | Surrounding words |
| Training examples | Combines context for a target | Creates target-context pairs |
| Typical characteristic | Often faster | Can learn useful representations for infrequent words |
| Example | `love`, `Python` → `learning` | `learning` → `love`, `Python` |

---

## 8. Context Window

A context window determines how many surrounding words are considered during training.

Consider:

```text
I love learning Python today
```

If the target word is `learning` and the context window covers one word on each side, the context is:

```text
love, Python
```

With a larger window, more surrounding words can be included.

The selected window size affects which relationships the model learns. Smaller windows tend to emphasize local relationships, while larger windows can capture broader contextual associations.

---

## 9. Training Word2Vec with Gensim

Gensim provides an implementation of Word2Vec that can be used to train embeddings from tokenized text.

Install Gensim if it is not already available in your Python environment:

```bash
pip install gensim
```

### Complete Example

```python
import re
from gensim.models import Word2Vec

sentences = [
    "cats chase small mice",
    "dogs chase small cats",
    "mice hide in small spaces",
    "dogs and cats are animals",
    "birds fly in the sky",
    "fish swim in water"
]

tokenized_sentences = [
    re.findall(r"[a-z]+", sentence.lower())
    for sentence in sentences
]

model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1,
    sg=1,
    seed=42,
    epochs=100
)

print("Vocabulary:")
print(model.wv.index_to_key)

print("\nEmbedding for 'cats':")
print(model.wv["cats"])

print("\nMost similar words to 'cats':")
print(model.wv.most_similar("cats", topn=3))
```

### Understanding the Parameters

| Parameter | Meaning |
|---|---|
| `sentences` | Tokenized training sentences |
| `vector_size` | Number of dimensions in each word vector |
| `window` | Maximum context distance around a target word |
| `min_count` | Minimum word frequency required for inclusion |
| `workers` | Number of worker threads |
| `sg=0` | Selects CBOW |
| `sg=1` | Selects Skip-gram |
| `seed` | Helps make initialization reproducible |
| `epochs` | Number of passes through the training data |

The example selects Skip-gram because `sg=1`.

**Important:** This corpus is intentionally tiny and is only for learning how the API works. The resulting embeddings are not reliable general-purpose language representations. Training results and the nearest words can vary with the data and configuration.

### Accessing an Embedding

```python
word_vector = model.wv["cats"]

print(word_vector)
print("Vector dimensions:", word_vector.shape)
```

### Finding Similar Words

```python
similar_words = model.wv.most_similar("cats", topn=5)

for word, score in similar_words:
    print(word, score)
```

The score indicates vector similarity under the model's similarity measure. It does not prove that two words are interchangeable in every sentence.

---

## 10. Vector Similarity and Cosine Similarity

Once words have vector representations, we can compare those vectors.

Cosine similarity measures the cosine of the angle between two nonzero vectors.

The formula is:

Cosine Similarity(A, B) = (A · B) / (||A|| × ||B||)

Where:

- `A · B` is the dot product of vectors A and B.
- `||A||` is the magnitude of vector A.
- `||B||` is the magnitude of vector B.

For ordinary nonzero real-valued vectors, cosine similarity lies between -1 and 1.

- A value close to `1` indicates that the vectors point in similar directions.
- A value close to `0` indicates little directional similarity.
- A value close to `-1` indicates opposite directions.

For learned word embeddings, cosine similarity is commonly used to find words with related representations.

### Python Example

```python
import numpy as np

cat = np.array([0.8, 0.6])
dog = np.array([0.7, 0.7])
car = np.array([-0.8, 0.6])

similarity_cat_dog = np.dot(cat, dog) / (
    np.linalg.norm(cat) * np.linalg.norm(dog)
)

similarity_cat_car = np.dot(cat, car) / (
    np.linalg.norm(cat) * np.linalg.norm(car)
)

print("Cat-Dog similarity:", round(similarity_cat_dog, 3))
print("Cat-Car similarity:", round(similarity_cat_car, 3))
```

Output:

```text
Cat-Dog similarity: 0.99
Cat-Car similarity: -0.28
```

These are manually chosen vectors to demonstrate the calculation. They are not trained word embeddings.

### Finding Similar Words with Gensim

```python
similar_words = model.wv.most_similar("cats", topn=3)
print(similar_words)
```

Gensim calculates similarities using the vectors learned by the model.

---

## 11. Nearest-Neighbor Search

Nearest-neighbor search finds words whose vectors are closest to a query vector under a chosen distance or similarity measure.

For example, a word search system may return words whose embeddings are most similar to the embedding for `king`.

In Gensim:

```python
model.wv.most_similar("cats", topn=5)
```

The method returns a list of words with their similarity scores.

Nearest-neighbor search is useful in:

- Semantic search
- Related-word discovery
- Vocabulary exploration
- Recommendation and retrieval systems
- Finding potentially similar terms in a corpus

Results depend on the training data. A small or biased corpus may produce unexpected neighbors.

---

## 12. Word Vector Arithmetic

Some Word2Vec models learn vector relationships that support meaningful arithmetic patterns.

A commonly discussed example is:

```text
king - man + woman ≈ queen
```

This illustrates how a vector operation may approximate a semantic relationship in a particular embedding space.

It is not a universal rule. Results depend on the training corpus, model, vocabulary, and vector geometry.

### Gensim Example

```python
result = model.wv.most_similar(
    positive=["king", "woman"],
    negative=["man"],
    topn=5
)

print(result)
```

This code requires `king`, `woman`, and `man` to exist in the trained vocabulary. The small example corpus above does not contain these words, so this query will not work with that model unless the training corpus is expanded.

---

## 13. Mean Pooling: Creating a Sentence Vector

Word embeddings represent individual words, but many applications require a single vector for an entire sentence or document.

Mean pooling combines word vectors by taking their element-wise average.

For word vectors \(v_1, v_2, \ldots, v_n\):

Sentence Vector = (v₁ + v₂ + ... + vₙ) / n

### Python Example

```python
import numpy as np

word_vectors = np.array([
    [0.2, 0.4, 0.6],
    [0.4, 0.6, 0.8],
    [0.6, 0.8, 1.0]
])

sentence_vector = np.mean(word_vectors, axis=0)

print("Sentence vector:", sentence_vector)
```

Output:

```text
Sentence vector: [0.4 0.6 0.8]
```

Mean pooling is simple and can work as a baseline. However, it ignores word order and may lose important information about negation or the different roles of words.

For example, these sentences contain similar words but have different meanings:

```text
The movie was good.
The movie was not good.
```

A simple average of static word embeddings may not adequately represent the difference.

---

## 14. Weighted Pooling

Mean pooling gives every word the same weight. Weighted pooling assigns different weights to words before combining their vectors.

The general formula is:

Sentence Vector = Σ(wᵢ × vᵢ) / Σwᵢ

Where:

- `vᵢ` is the embedding for word `i`.
- `wᵢ` is the weight assigned to word `i`.

### Python Example

```python
import numpy as np

word_vectors = np.array([
    [0.2, 0.4, 0.6],
    [0.4, 0.6, 0.8],
    [0.6, 0.8, 1.0]
])

weights = np.array([1.0, 2.0, 3.0])

sentence_vector = np.average(
    word_vectors,
    axis=0,
    weights=weights
)

print("Weighted sentence vector:", sentence_vector)
```

Output:

```text
Weighted sentence vector: [0.46666667 0.66666667 0.86666667]
```

The weights may come from TF-IDF, an attention mechanism, or another scoring method. Weighted pooling can emphasize important words, but its effectiveness depends on how the weights are chosen.

---

## 15. Static vs Contextual Word Embeddings

A major limitation of traditional Word2Vec embeddings is that each word has one learned vector, regardless of the sentence in which it appears.

Consider the word `bank`:

```text
I deposited money in the bank.
We sat beside the river bank.
```

The word has different meanings in the two sentences.

### Static Embeddings

Methods such as Word2Vec and GloVe generally assign one learned vector to each vocabulary word.

Advantages:

- Relatively simple to understand and use.
- Can be efficient for many NLP tasks.
- Can be trained on a specific domain's text.
- Useful when a compact word-level representation is sufficient.

Limitations:

- One word generally has one vector regardless of its context.
- Different meanings of the same word are not directly represented separately.
- Out-of-vocabulary words may require special handling.

### Contextual Embeddings

Contextual models generate representations based on the surrounding text. The same word can receive different representations in different sentences.

Examples include:

- BERT
- RoBERTa
- ELMo
- Transformer-based language models

For example, a contextual model can use the surrounding words to distinguish the financial meaning of `bank` from the geographical meaning.

| Feature | Static Embeddings | Contextual Embeddings |
|---|---|---|
| Representation | Generally fixed per word | Depends on the input context |
| Word meaning | Does not directly vary by sentence | Can vary with sentence context |
| Examples | Word2Vec, GloVe | BERT, RoBERTa |
| Typical computation | Often relatively lightweight | Usually requires more model computation |
| Best suited for | Many word-level baselines and lightweight applications | Tasks needing richer contextual understanding |

Contextual embeddings are often produced by Transformer architectures, which use attention mechanisms to process relationships between tokens.

---

## 16. GloVe

GloVe stands for **Global Vectors for Word Representation**. It is a method for learning word vectors using statistical information about how often words co-occur across a corpus.

Word2Vec learns by predicting target words or context words. GloVe uses global word co-occurrence statistics as part of its training objective.

Both methods produce dense word vectors and can capture semantic relationships.

| Feature | Word2Vec | GloVe |
|---|---|---|
| Main approach | Predictive training | Global co-occurrence statistics |
| Input information | Local contexts from text | Word co-occurrence counts |
| Output | Dense word vectors | Dense word vectors |
| Contextual by itself | No | No |
| Example use | Word similarity and downstream NLP | Word similarity and downstream NLP |

GloVe vectors are commonly used as pretrained embeddings, although they can also be trained on suitable corpora.

---

## 17. FastText

FastText is an embedding method that represents words using character-level subword information, including character n-grams.

For example, related forms such as:

```text
play
player
playing
```

share character patterns. FastText can use these patterns when learning word representations.

### Advantages

- Can represent some words that were not seen during training by using their character n-grams.
- Can help with morphologically rich languages.
- Can capture relationships between words that share subword structure.

FastText does not guarantee that every unseen word will receive a useful vector. Its performance depends on the learned subword representations and the input word.

---

## 18. Applications of Word Embeddings

Word embeddings are used in many NLP applications.

### Sentiment Analysis

Embeddings can provide word representations to a model that predicts whether a review is positive or negative.

Example:

```text
"The product is excellent."
```

The resulting representation can be used as input to a sentiment classifier.

### Text Classification

Embeddings can help classify messages into categories such as spam, promotions, support requests, or complaints.

### Semantic Search

Search systems can compare vector representations to retrieve text that is conceptually related to a query, even when the wording differs.

### Machine Translation

Embedding layers are commonly used in neural machine translation systems to represent source and target tokens.

### Chatbots

Embeddings can help represent text for intent classification, retrieval, and other language-processing components.

### Recommendation Systems

Text embeddings can represent product descriptions, user reviews, and other textual information to support similarity-based recommendations.

### Information Retrieval

Embeddings can help identify semantically related documents and passages. Practical systems may use sentence or document embeddings rather than individual word vectors.

---

## 19. Limitations of Word Embeddings

Although word embeddings are useful, they have limitations.

1. **Dependence on training data:** The learned vectors reflect patterns in the corpus.
2. **Bias:** Social and cultural biases in the training text may be encoded in the representations.
3. **Polysemy:** Traditional static embeddings use one vector for a word with multiple meanings.
4. **Out-of-vocabulary words:** Traditional vocabulary-based embeddings may not represent unseen words directly.
5. **Limited interpretability:** Individual vector dimensions usually do not have straightforward human-readable meanings.
6. **Context loss in pooling:** Averaging word vectors ignores word order and may lose important sentence-level information.
7. **Domain mismatch:** Embeddings trained on general text may not work as well for specialized domains.
8. **Evaluation challenges:** A high similarity score does not necessarily imply that two words are interchangeable.

The best embedding method depends on the task, training data, computational resources, and accuracy requirements.

---

## 20. Practical Comparison of Text Representation Methods

| Method | Representation | Main Strength | Main Limitation |
|---|---|---|---|
| One-Hot Encoding | Binary vector | Simple and easy to understand | No semantic similarity |
| Bag of Words | Word counts | Simple document representation | Ignores word order and meaning |
| TF-IDF | Weighted word counts | Highlights informative terms | Does not inherently learn semantics |
| Word2Vec | Dense word vectors | Learns word relationships from contexts | Static representations |
| GloVe | Dense word vectors | Uses global co-occurrence statistics | Static representations |
| FastText | Dense vectors with subword information | Can handle many unseen word forms | Still generally static at the word level |
| BERT | Contextual token representations | Represents words using context | More computationally demanding |

---

## 21. Important Points to Remember

- Word embeddings convert words into dense numerical vectors.
- One-hot encoding, Bag of Words, and TF-IDF do not inherently learn semantic word representations.
- Embedding dimensions determine the length of each word vector.
- An embedding matrix stores a vector for each indexed vocabulary item.
- Word2Vec has two major architectures: CBOW and Skip-gram.
- CBOW predicts a target word from surrounding context words.
- Skip-gram predicts surrounding context words from a target word.
- Context window size influences which relationships are learned.
- Cosine similarity is commonly used to compare word vectors.
- Nearest-neighbor search can find words with similar vector representations.
- Mean pooling and weighted pooling can combine word vectors into a sentence representation.
- Word2Vec and GloVe generally use static word embeddings.
- BERT and similar Transformer models generate contextual representations.
- Embeddings reflect their training data and may contain biases.
- Similarity does not necessarily mean that two words have identical meanings.

---

## 22. Important Formula Summary

### TF-IDF

TF-IDF(t, d) = TF(t, d) × IDF(t)

A common inverse document frequency formula is:

IDF(t) = log(N / df(t))

### Cosine Similarity

Cosine Similarity(A, B) = (A · B) / (||A|| × ||B||)

### Mean Pooling

Sentence Vector = (v₁ + v₂ + ... + vₙ) / n

### Weighted Pooling

Sentence Vector = Σ(wᵢ × vᵢ) / Σwᵢ

### Embedding Matrix Size

Number of Parameters = Vocabulary Size × Embedding Dimension

---

## 23. References

- [Word2Vec: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)
- [FastText](https://fasttext.cc/)
- [Gensim Word2Vec Documentation](https://radimrehurek.com/gensim/models/word2vec.html)
- [Stanford CS224N: Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
