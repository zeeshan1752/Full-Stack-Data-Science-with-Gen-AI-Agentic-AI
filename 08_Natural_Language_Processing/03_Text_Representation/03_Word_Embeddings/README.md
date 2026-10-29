# Word Embeddings

Word embeddings represent words with dense vectors. This topic currently includes a Word2Vec example implemented with Gensim.

- [Word2Vec notes](README.md#word2vec)
- [Gensim Word2Vec script](word2vec_gensim.py)
- [Gensim Word2Vec notebook](word2vec_gensim.ipynb)

---

## Gensim

Gensim provides models for word embeddings, document similarity, and topic modeling.

Install Gensim using:

```bash
python -m pip install --upgrade gensim
```

The other Gensim topic folders are planned.

---

## Word2Vec

### 1. Introduction

**Word2Vec** is a word embedding technique that learns dense numerical vector representations of words from their surrounding context in a text corpus.

Traditional text representation techniques, such as Bag of Words and TF-IDF, represent words using counts or weights. Word2Vec instead learns vectors that can capture patterns in how words are used.

The main idea is that words appearing in similar contexts may have similar vector representations.

For example, words such as `king`, `queen`, `prince`, and `princess` may exhibit related patterns in a suitable training corpus.

Word2Vec was introduced by researchers at Google and is commonly associated with two architectures:

- **CBOW (Continuous Bag of Words):** Predicts a target word from its surrounding context words.
- **Skip-gram:** Predicts surrounding context words from a target word.

Word2Vec is a foundational technique in Natural Language Processing (NLP) and helps explain how text can be represented as numerical vectors.

### 2. Why Do We Need Word2Vec?

Computers work with numerical data, so words need to be represented numerically before many machine learning algorithms can process them.

Consider these words:

- `cat`
- `dog`
- `car`
- `vehicle`

A simple Bag of Words model represents terms as separate vocabulary features. TF-IDF assigns weights based on term frequency and document frequency. Neither technique inherently learns that `cat` and `dog` are semantically related.

Word2Vec learns vector representations from word usage patterns. When words occur in similar contexts, their vectors may become similar.

For example:

- `cat` and `dog` may occur near words such as `pet`, `food`, and `animal`.
- `car` and `vehicle` may occur near words such as `road`, `drive`, and `engine`.

The learned vectors can reflect these contextual relationships, depending on the training corpus and model settings.

### 3. What Is a Word Embedding?

A **word embedding** is a numerical vector representing a word.

For example, a hypothetical embedding might represent `cat` as:

$$
\text{cat}=[0.21,-0.45,0.78,0.12]
$$

And `dog` as:

$$
\text{dog}=[0.19,-0.39,0.74,0.16]
$$

These values are illustrative, not actual trained Word2Vec vectors.

Each number is a learned component of the representation. The individual dimensions generally do not have simple, human-readable meanings.

In practice, embeddings often contain tens, hundreds, or more dimensions. Their size depends on the model configuration.

#### Important Characteristics

- Words are represented as dense vectors.
- Vector values are learned from a training corpus.
- Words used in similar contexts can have similar vectors.
- Embeddings can be used as features for downstream NLP tasks.
- Word2Vec generally produces one learned vector per vocabulary word, rather than a different contextual vector for each occurrence.

### 4. How Does Word2Vec Work?

Word2Vec learns by examining the relationships between words in a text corpus.

Consider this sentence:

`The cat sits on the mat.`

A training process examines words and their surrounding context according to a selected window size.

For example, with a context window of two, the context around `sits` may include:

`The`, `cat`, `on`, `the`

The model uses training examples derived from such relationships to learn word representations.

A simplified workflow is:

1. Collect a text corpus.
2. Tokenize the text into words.
3. Build a vocabulary.
4. Generate training examples from word contexts.
5. Train a CBOW or Skip-gram model.
6. Extract the learned word vectors.
7. Use the vectors in similarity analysis or downstream NLP tasks.

The resulting vectors are influenced by the corpus, tokenization, context window, vector dimension, and training parameters.

### 5. The Two Word2Vec Architectures

#### 5.1 CBOW (Continuous Bag of Words)

CBOW predicts a target word using the surrounding context words.

Example sentence:

`The cat drinks milk`

Suppose the target word is `drinks`.

**Context words:**

`The`, `cat`, `milk`

**Target word:**

`drinks`

The model learns to predict the target word from the context.

Simplified representation:

$$
\text{Context Words}\rightarrow\text{Target Word}
$$

CBOW combines information from the context to predict the missing target word.

**Characteristics:**

- Predicts a target word from surrounding words.
- Often trains efficiently on suitable datasets.
- Uses context information without treating context order as the central prediction objective.
- Can work well for learning representations of frequent words.

#### 5.2 Skip-gram

Skip-gram predicts surrounding context words using a target word.

Using the same sentence:

`The cat drinks milk`

**Target word:**

`drinks`

**Possible context words:**

`The`, `cat`, `milk`

Simplified representation:

$$
\text{Target Word}\rightarrow\text{Context Words}
$$

The model learns which words are likely to appear near the target word.

**Characteristics:**

- Predicts context words from a target word.
- Generates training examples from target-context relationships.
- Can be useful for learning representations of less frequent words, given a suitable corpus and training configuration.
- May require more training examples than CBOW.

#### 5.3 CBOW vs. Skip-gram

| Feature | CBOW | Skip-gram |
|---|---|---|
| Input | Context words | Target word |
| Prediction | Target word | Context words |
| Training objective | Predict a word from context | Predict context from a word |
| Common advantage | Often computationally efficient | Can learn useful representations for less frequent words |
| Example | `cat`, `milk` → `drinks` | `drinks` → `cat`, `milk` |

Both approaches learn word vectors from context. Their effectiveness depends on the corpus, model settings, and intended task.

### 6. Important Word2Vec Parameters

Several parameters influence the learned embeddings.

| Parameter | Meaning |
|---|---|
| `vector_size` | Number of dimensions in each word vector |
| `window` | Maximum context distance used when generating training examples |
| `min_count` | Minimum frequency required for a word to be included in the vocabulary |
| `sg` | Selects Skip-gram (`1`) or CBOW (`0`) |
| `epochs` | Number of training passes over the corpus |
| `workers` | Number of worker threads used for training |
| `negative` | Number of negative samples used per positive training example |
| `seed` | Random seed that can help make training more reproducible |

For Gensim's `Word2Vec`, `sg=0` selects CBOW and `sg=1` selects Skip-gram.

### 7. Word2Vec Using Python and Gensim

Gensim provides an implementation of Word2Vec.

#### Installation

Install Gensim using:

```bash
python -m pip install --upgrade gensim
```

#### Example 1: Train a Basic Word2Vec Model

```python
from gensim.models import Word2Vec

sentences = [
    ["cats", "chase", "small", "mice"],
    ["dogs", "chase", "cats"],
    ["mice", "like", "small", "spaces"],
    ["dogs", "like", "playing", "outside"],
    ["cats", "and", "dogs", "are", "pets"],
    ["pets", "need", "food", "and", "care"]
]

model = Word2Vec(
    sentences=sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1,
    sg=1,
    epochs=100,
    seed=42
)

print("Vocabulary:")
print(model.wv.index_to_key)

print("\nVector for 'cats':")
print(model.wv["cats"])

print("\nVector Dimensions:")
print(model.wv["cats"].shape)
```

#### Explanation

- `sentences` contains tokenized training sentences.
- `vector_size=50` creates vectors with 50 dimensions.
- `window=3` sets the context window.
- `min_count=1` includes words that appear at least once.
- `sg=1` selects Skip-gram.
- `epochs=100` specifies the number of training passes.
- `model.wv["cats"]` retrieves the learned vector for `cats`.

**Important:** This corpus is intentionally tiny for demonstration. It is not large or varied enough to produce reliable, general-purpose word embeddings. A real application generally requires a substantially larger corpus.

#### Example 2: Train a CBOW Model

```python
from gensim.models import Word2Vec

sentences = [
    ["machine", "learning", "uses", "data"],
    ["deep", "learning", "uses", "neural", "networks"],
    ["data", "science", "uses", "statistics"],
    ["python", "is", "useful", "for", "data", "science"],
    ["machine", "learning", "can", "analyze", "text"]
]

model = Word2Vec(
    sentences=sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1,
    sg=0,
    epochs=100,
    seed=42
)

print("Vocabulary:")
print(model.wv.index_to_key)

print("\nVector for 'learning':")
print(model.wv["learning"])

print("\nVector Dimensions:")
print(model.wv["learning"].shape)
```

In this example, `sg=0` selects CBOW. The model learns vectors using context words to predict target words.

### 8. Finding Similar Words

One use of Word2Vec is to find vocabulary items whose learned vectors are similar.

Gensim provides `most_similar()` for this purpose.

```python
from gensim.models import Word2Vec

sentences = [
    ["cat", "is", "a", "pet"],
    ["dog", "is", "a", "pet"],
    ["cat", "likes", "milk"],
    ["dog", "likes", "food"],
    ["bird", "can", "fly"],
    ["fish", "can", "swim"]
]

model = Word2Vec(
    sentences=sentences,
    vector_size=30,
    window=3,
    min_count=1,
    workers=1,
    sg=1,
    epochs=200,
    seed=42
)

print("Words Most Similar to 'cat':")
print(model.wv.most_similar("cat", topn=3))
```

The output depends on the training data and random initialization. Because the corpus is small, the results should be treated as a demonstration rather than a reliable measure of real-world semantic similarity.

### 9. Calculating Word Similarity

Word2Vec vectors can be compared using cosine similarity.

Cosine similarity measures the cosine of the angle between two vectors.

$$
\text{cosine similarity}(A,B)=
\frac{A\cdot B}{\|A\|\|B\|}
$$

Where:

- \(A\) and \(B\) are word vectors.
- \(A\cdot B\) is their dot product.
- \(\|A\|\) and \(\|B\|\) are their vector magnitudes.

For nonzero vectors, cosine similarity ranges from \(-1\) to \(1\). In many embedding applications, larger values indicate greater directional similarity.

**Example:**

```python
from gensim.models import Word2Vec
from numpy import dot
from numpy.linalg import norm

sentences = [
    ["cats", "are", "pets"],
    ["dogs", "are", "pets"],
    ["cats", "drink", "milk"],
    ["dogs", "eat", "food"],
    ["cars", "drive", "roads"],
    ["trucks", "drive", "roads"]
]

model = Word2Vec(
    sentences=sentences,
    vector_size=30,
    window=3,
    min_count=1,
    workers=1,
    sg=1,
    epochs=200,
    seed=42
)

vector1 = model.wv["cats"]
vector2 = model.wv["dogs"]

similarity = dot(vector1, vector2) / (
    norm(vector1) * norm(vector2)
)

print("Cosine Similarity:", round(float(similarity), 4))
```

The resulting value is learned from this particular training run and corpus. It should not be interpreted as a universal measure of how similar two words are.

### 10. Word2Vec Vocabulary and Unknown Words

Word2Vec generally learns vectors only for words included in its training vocabulary.

For example, if the corpus contains:

`["cats", "chase", "mice"]`

The model will learn vectors for the vocabulary it retains. A word that never appears in that vocabulary cannot be retrieved as a normal trained word vector.

With Gensim, you can check whether a word is present:

```python
if "cats" in model.wv:
    print("The word is present in the vocabulary.")
    print(model.wv["cats"])
else:
    print("The word is not present in the vocabulary.")
```

A word may be absent because it never appeared in the training data or because it was removed by the `min_count` threshold.

Word2Vec is a static word embedding method: the same vocabulary word normally has one learned vector, even when it appears in different contexts. Contextual models such as BERT can generate different representations for a word depending on its surrounding text.

### 11. Word2Vec vs. Bag of Words vs. TF-IDF

| Feature | Bag of Words | TF-IDF | Word2Vec |
|---|---|---|---|
| Representation | Sparse count vectors | Sparse weighted vectors | Dense word vectors |
| Main purpose | Count vocabulary terms | Weight terms by document distribution | Learn word representations from context |
| Learns word-context relationships | No, in the standard model | No, in the standard model | Yes |
| Captures semantic patterns | Not inherently | Not inherently | Can capture patterns in usage |
| Representation unit | Usually document | Usually document | Word |
| Depends on a training corpus | Learns vocabulary from documents | Learns vocabulary and IDF from documents | Learns word vectors from a corpus |
| Common applications | Text classification | Search and document retrieval | Similarity features and downstream NLP |

These techniques solve different problems. Word2Vec learns word-level representations, whereas Bag of Words and TF-IDF are commonly used to represent documents.

### 12. Word2Vec vs. Contextual Embeddings

Word2Vec is a **static embedding** technique.

A word normally receives one vector after training. The vector does not automatically change based on the sentence in which the word appears.

Consider:

- `The bank approved the loan.`
- `We sat beside the river bank.`

Word2Vec does not normally produce separate context-dependent vectors for these two occurrences of `bank`.

Contextual embedding models, such as BERT, generate representations influenced by surrounding words. They are better suited to tasks where the meaning of a word depends strongly on context.

| Feature | Word2Vec | Contextual Embeddings |
|---|---|---|
| Vector depends on sentence context | No, not for the standard word vector | Yes |
| Representation | Static word vector | Context-dependent token representation |
| Typical architecture | Shallow neural network | Often a transformer |
| Computational requirements | Often relatively modest | Often higher |
| Example use | Word similarity | Context-sensitive language understanding |

### 13. Applications of Word2Vec

#### Word Similarity

Identify words with similar learned vector representations.

#### Recommendation Systems

Word embeddings can help represent items or terms that occur in similar contexts, depending on how the model is trained and applied.

#### Text Classification

Word vectors can be used as features for tasks such as sentiment classification or topic classification.

#### Document Representation

Word vectors can be combined or aggregated to produce document-level features. More advanced approaches can use additional weighting or neural architectures.

#### Information Retrieval

Embeddings can help represent query terms and document vocabulary for similarity-based retrieval systems.

#### Semantic Analysis

Word2Vec can reveal patterns of word usage in a corpus, although it does not provide dictionary definitions or guarantee that words with similar vectors are interchangeable.

### 14. Limitations of Word2Vec

1. **Requires training data.** Useful vectors depend on having a suitable corpus.
2. **Static representations.** A word normally has the same vector in different contexts.
3. **Out-of-vocabulary words.** Standard Word2Vec cannot directly return learned vectors for words absent from its vocabulary.
4. **Corpus dependence.** The learned relationships reflect the data used for training.
5. **Bias.** Embeddings can reproduce social and other biases present in the training corpus.
6. **Limited understanding of meaning.** Similarity between vectors is not the same as true language understanding.
7. **Rare-word limitations.** Infrequent words may have unreliable vectors.
8. **Small-corpus limitations.** A tiny corpus generally cannot provide robust general-purpose embeddings.

### 15. Common Mistakes

- Confusing CBOW with Skip-gram.
- Assuming the individual dimensions of a word vector have obvious meanings.
- Assuming that a higher similarity score proves two words have identical meanings.
- Training a model on too little data and expecting useful general-purpose results.
- Trying to retrieve vectors for words missing from the vocabulary.
- Assuming Word2Vec generates a different vector for every occurrence of a word.
- Treating Word2Vec as a complete language model that can generate coherent text.
- Comparing vector results from independently trained models without considering their different learned spaces.

### 16. Points to Remember

- Word2Vec learns dense word vectors from word-context relationships.
- CBOW predicts a target word from its surrounding context.
- Skip-gram predicts context words from a target word.
- `vector_size` determines the number of vector dimensions.
- Gensim provides a convenient Python implementation.
- `most_similar()` can retrieve words with similar learned vectors.
- Word2Vec's vectors depend on the training corpus and configuration.
- Standard Word2Vec produces static word vectors rather than context-dependent representations.
- A tiny training corpus is useful for learning the code but not for producing reliable general-purpose embeddings.

### 17. References

- [Gensim Word2Vec Documentation](https://radimrehurek.com/gensim/models/word2vec.html)
- [Gensim Documentation](https://radimrehurek.com/gensim/)
- [Original Word2Vec Paper: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- [Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546)
