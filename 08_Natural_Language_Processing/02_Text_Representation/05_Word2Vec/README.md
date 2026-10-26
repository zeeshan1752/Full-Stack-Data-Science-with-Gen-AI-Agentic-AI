# Word2Vec

## 1. Introduction

**Word2Vec** is a word embedding technique that learns dense numerical vector representations of words from their surrounding context in a text corpus.

Traditional text representation techniques, such as Bag of Words (BoW) and TF-IDF, represent words using counts or weights. Word2Vec learns vectors that can capture patterns in how words are used.

The main idea is that words appearing in similar contexts may develop similar vector representations.

Word2Vec is commonly associated with two architectures:

- **CBOW (Continuous Bag of Words):** Predicts a target word from its surrounding context words.
- **Skip-gram:** Predicts surrounding context words from a target word.

## 2. Why Do We Need Word2Vec?

Computers work with numerical data, so text often needs to be converted into numerical representations before machine learning models can process it.

Bag of Words and TF-IDF represent terms as document features. They do not inherently learn that words such as `cat` and `dog` may be related. Word2Vec learns word vectors from usage patterns in a corpus.

For example, `cat` and `dog` might occur near words such as `pet`, `food`, and `animal`, while `car` and `vehicle` might occur near `road`, `drive`, and `engine`. The vectors may reflect these relationships if the training corpus provides enough useful examples.

## 3. What Is a Word Embedding?

A **word embedding** is a numerical vector representing a word.

A hypothetical example:

- `cat` = `[0.21, -0.45, 0.78, 0.12]`
- `dog` = `[0.19, -0.39, 0.74, 0.16]`

These values are illustrative, not actual trained Word2Vec vectors.

Each number is a learned component of the representation. Individual dimensions usually do not have simple, human-readable meanings. Embeddings may contain tens, hundreds, or more dimensions, depending on the model configuration.

### Important characteristics

- Words are represented as dense vectors.
- Vector values are learned from a training corpus.
- Words used in similar contexts can have similar vectors.
- Embeddings can be used as features for downstream NLP tasks.
- Standard Word2Vec generally learns one vector per vocabulary word rather than a different vector for each occurrence.

## 4. How Does Word2Vec Work?

Consider the sentence:

`The cat sits on the mat.`

A training process examines words and their surrounding context according to a selected window size. For example, with a context window of two, the context around `sits` may include `The`, `cat`, `on`, and `the`, depending on the token positions and window convention.

A simplified workflow is:

1. Collect a text corpus.
2. Tokenize the text into words.
3. Build a vocabulary.
4. Generate training examples from word contexts.
5. Train a CBOW or Skip-gram model.
6. Extract the learned word vectors.
7. Use the vectors for similarity analysis or downstream NLP tasks.

The vectors are influenced by the corpus, tokenization, context window, vector dimension, and training parameters.

## 5. The Two Word2Vec Architectures

### 5.1 CBOW (Continuous Bag of Words)

CBOW predicts a target word using surrounding context words.

Example sentence:

`The cat drinks milk`

If `drinks` is the target word, the surrounding words can be used as context:

- Context: `The`, `cat`, `milk`
- Target: `drinks`

Simplified representation:

**Context words → Target word**

CBOW combines context information to predict the target word. It is often computationally efficient on suitable datasets.

### 5.2 Skip-gram

Skip-gram predicts surrounding context words using a target word.

For the same sentence:

- Target: `drinks`
- Possible context words: `The`, `cat`, `milk`

Simplified representation:

**Target word → Context words**

Skip-gram creates target-context training examples and can learn useful representations for less frequent words when the corpus and training settings support it.

### 5.3 CBOW vs. Skip-gram

| Feature | CBOW | Skip-gram |
|---|---|---|
| Input | Context words | Target word |
| Prediction | Target word | Context words |
| Training objective | Predict a word from context | Predict context from a word |
| Common characteristic | Often computationally efficient | Can be useful for less frequent words |
| Example | `cat`, `milk` → `drinks` | `drinks` → `cat`, `milk` |

Both approaches learn word vectors from context. Their effectiveness depends on the corpus, model settings, and task.

## 6. Important Word2Vec Parameters

| Parameter | Meaning |
|---|---|
| `vector_size` | Number of dimensions in each word vector |
| `window` | Maximum context distance used to generate training examples |
| `min_count` | Minimum frequency required for a word to be included |
| `sg` | Selects Skip-gram (`1`) or CBOW (`0`) |
| `epochs` | Number of training passes over the corpus |
| `workers` | Number of worker threads used for training |
| `negative` | Number of negative samples used per positive training example |
| `seed` | Random seed that can help make training more reproducible |

For Gensim's `Word2Vec`, `sg=0` selects CBOW and `sg=1` selects Skip-gram.

## 7. Word2Vec Using Python and Gensim

Gensim provides a Python implementation of Word2Vec.

### Installation

Install Gensim using:

```bash
python -m pip install --upgrade gensim
```

### Example 1: Train a Basic Skip-gram Model

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

print("\nVector dimensions:")
print(model.wv["cats"].shape)
```

**Example output:** The exact vocabulary order and vector values may vary.

```text
Vocabulary:
['cats', 'dogs', 'and', 'pets', 'chase', 'small', 'mice', 'like', 'playing', 'outside', 'are', 'need', 'food', 'care', 'spaces']

Vector for 'cats':
[... 50 floating-point values ...]

Vector dimensions:
(50,)
```

The vector is abbreviated above to keep the README readable. Running the code prints all 50 values. The vocabulary ordering shown is illustrative.

### Explanation

- `sentences` contains tokenized training sentences.
- `vector_size=50` creates 50-dimensional vectors.
- `window=3` sets the context window.
- `min_count=1` includes words that appear at least once.
- `sg=1` selects Skip-gram.
- `epochs=100` specifies the number of training passes.
- `model.wv["cats"]` retrieves the learned vector for `cats`.

**Important:** This corpus is intentionally tiny for demonstration. It is not large or varied enough to produce reliable, general-purpose word embeddings.

### Example 2: Train a CBOW Model

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

print("\nVector dimensions:")
print(model.wv["learning"].shape)
```

**Example output:** Vector values and vocabulary order may vary.

```text
Vocabulary:
['learning', 'data', 'machine', 'uses', 'science', 'deep', 'neural', 'networks', 'python', 'is', 'useful', 'for', 'statistics', 'can', 'analyze', 'text']

Vector for 'learning':
[... 50 floating-point values ...]

Vector dimensions:
(50,)
```

Here, `sg=0` selects CBOW. The model learns vectors by using context words to predict target words.

## 8. Finding Similar Words

Gensim's `most_similar()` method returns words with vectors closest to a query word under cosine similarity.

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

print("Words most similar to 'cat':")
print(model.wv.most_similar("cat", topn=3))
```

**Example output format:**

```text
Words most similar to 'cat':
[('dog', 0.XX), ('pet', 0.XX), ('milk', 0.XX)]
```

The `0.XX` values are placeholders, not measured scores. Run the code to obtain actual values in your environment. Because the corpus is small, results are only a demonstration.

## 9. Calculating Word Similarity

Word2Vec vectors can be compared using cosine similarity. For two nonzero vectors, cosine similarity is:

**Cosine similarity(A, B) = (A · B) / (||A|| × ||B||)**

Where:

- `A` and `B` are word vectors.
- `A · B` is their dot product.
- `||A||` and `||B||` are their magnitudes.

Cosine similarity ranges from `-1` to `1`. In many embedding applications, a larger value indicates greater directional similarity.

### Python Example

```python
from gensim.models import Word2Vec

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

similarity = model.wv.similarity("cats", "dogs")
print("Cosine similarity:", round(float(similarity), 4))
```

**Example output:**

```text
Cosine similarity: <a numeric value between -1 and 1>
```

The exact value is learned from this training run and corpus. The placeholder is descriptive; run the code to see the numeric result. Do not interpret the score as a universal measure of how similar two words are.

## 10. Word2Vec Vocabulary and Unknown Words

Standard Word2Vec generally learns vectors only for words retained in its training vocabulary. A word can be absent because it never appeared in the corpus or because it was removed by the `min_count` threshold.

```python
if "cats" in model.wv:
    print("The word is present in the vocabulary.")
    print("Vector dimensions:", model.wv["cats"].shape)
else:
    print("The word is not present in the vocabulary.")
```

**Example output when `cats` is present:**

```text
The word is present in the vocabulary.
Vector dimensions: (30,)
```

The shape depends on the `vector_size` used when training the model.

Standard Word2Vec is a static embedding method: a vocabulary word normally has one learned vector even when it appears in different contexts. Contextual models such as BERT can generate representations influenced by surrounding text.

## 11. Word2Vec vs. Bag of Words vs. TF-IDF

| Feature | Bag of Words | TF-IDF | Word2Vec |
|---|---|---|---|
| Representation | Sparse count vectors | Sparse weighted vectors | Dense word vectors |
| Main purpose | Count vocabulary terms | Weight terms by document distribution | Learn word representations from context |
| Learns word-context relationships | No, not in the standard method | No, not in the standard method | Yes |
| Captures semantic patterns | Not inherently | Not inherently | Can capture patterns in usage |
| Typical representation unit | Document | Document | Word |
| Training data | Learns vocabulary from documents | Learns vocabulary and IDF from documents | Learns word vectors from a corpus |
| Common applications | Text classification | Search and document retrieval | Similarity features and downstream NLP |

These methods solve different problems. Word2Vec learns word-level representations, whereas Bag of Words and TF-IDF are commonly used to represent documents.

## 12. Word2Vec vs. Contextual Embeddings

Word2Vec is a **static embedding** technique. A word normally receives one vector after training, regardless of the sentence in which it appears.

Consider:

- `The bank approved the loan.`
- `We sat beside the river bank.`

Word2Vec does not normally produce separate context-dependent vectors for these two occurrences of `bank`.

Contextual models such as BERT generate representations influenced by surrounding words.

| Feature | Word2Vec | Contextual Embeddings |
|---|---|---|
| Vector depends on sentence context | No, not for the standard word vector | Yes |
| Representation | Static word vector | Context-dependent token representation |
| Typical architecture | Shallow neural network | Often a Transformer |
| Computational requirements | Often relatively modest | Often higher |
| Example use | Word similarity | Context-sensitive language understanding |

## 13. Applications of Word2Vec

### Word Similarity

Find words with similar learned vector representations.

### Recommendation Systems

Represent terms or items that occur in similar contexts, depending on how the model is trained and applied.

### Text Classification

Use word vectors as features for sentiment classification, topic classification, or other text tasks.

### Document Representation

Combine word vectors into document-level features. More advanced approaches can use weighting or neural architectures.

### Information Retrieval

Represent query terms and document vocabulary for similarity-based retrieval systems.

### Semantic Analysis

Explore patterns of word usage in a corpus. Similarity does not guarantee that words are interchangeable.

## 14. Limitations of Word2Vec

1. **Requires suitable training data:** Useful vectors depend on the corpus.
2. **Static representations:** A word normally has the same vector in different contexts.
3. **Out-of-vocabulary words:** Standard Word2Vec cannot directly return learned vectors for words absent from its vocabulary.
4. **Corpus dependence:** Learned relationships reflect the training data.
5. **Bias:** Embeddings can reproduce biases present in the corpus.
6. **Limited understanding:** Vector similarity is not the same as human language understanding.
7. **Rare-word limitations:** Infrequent words may have unreliable vectors.
8. **Small-corpus limitations:** A tiny corpus is useful for learning the API but not for producing robust general-purpose embeddings.

## 15. Common Mistakes

- Confusing CBOW with Skip-gram.
- Assuming embedding dimensions have obvious human-readable meanings.
- Assuming a high similarity score proves two words have identical meanings.
- Training on too little data and expecting reliable general-purpose results.
- Trying to retrieve a vector for a word missing from the vocabulary.
- Assuming Word2Vec generates a different vector for every occurrence of a word.
- Treating Word2Vec as a text-generation model.
- Comparing scores from separately trained models without considering their different vector spaces.

## 16. Points to Remember

- Word2Vec learns dense word vectors from word-context relationships.
- CBOW predicts a target word from surrounding context.
- Skip-gram predicts context words from a target word.
- `vector_size` determines the number of vector dimensions.
- Gensim provides a convenient Python implementation.
- `most_similar()` retrieves words with similar learned vectors.
- Vectors depend on the corpus and training configuration.
- Standard Word2Vec produces static word vectors, not context-dependent representations.
- A tiny corpus is useful for practicing code but not for reliable general-purpose embeddings.

## 17. References

- [Gensim Word2Vec Documentation](https://radimrehurek.com/gensim/models/word2vec.html)
- [Gensim Documentation](https://radimrehurek.com/gensim/)
- [Original Word2Vec Paper: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- [Distributed Representations of Words and Phrases and their Compositionality](https://arxiv.org/abs/1310.4546)
