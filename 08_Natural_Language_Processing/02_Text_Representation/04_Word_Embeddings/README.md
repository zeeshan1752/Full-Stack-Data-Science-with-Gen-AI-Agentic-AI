# 04. Word Embeddings

Word embeddings represent words as **dense numerical vectors**. Instead of assigning a separate count or indicator to every vocabulary word, an embedding maps each word to a relatively small vector whose values are learned from data.

This folder introduces the main ideas behind embeddings and provides Python and Jupyter Notebook demonstrations. The separate [Word2Vec lesson](../05_Word2Vec/README.md) covers Word2Vec in more depth, while [GloVe](../06_GloVe/README.md) is maintained as its own topic.

## Learning objectives

By the end of this topic, you should be able to:

- Explain why NLP systems need numerical representations of text.
- Compare one-hot encoding, Bag of Words, TF-IDF, and dense embeddings.
- Explain the distributional hypothesis and how context helps learn representations.
- Understand embedding dimensions, vocabulary indices, vector similarity, and cosine similarity.
- Distinguish static word embeddings from contextual transformer embeddings.
- Build a tiny illustrative embedding example and optionally train Word2Vec with Gensim.
- Explain sentence/document vector pooling and the limitations of averaged word vectors.

## 1. Why do we need word embeddings?

Machine-learning models operate on numerical data, but natural language is made of words, punctuation, and sentence structure. We therefore need a way to represent text as numbers.

Consider these words:

- `cat`
- `dog`
- `banana`
- `car`

A useful representation should allow a model to learn patterns from how words are used. For example, `cat` and `dog` may appear in similar contexts, while `banana` may appear in different contexts.

A word embedding maps each word to a vector such as:

`cat -> [0.21, -0.14, 0.72, ...]`

The values above are only illustrative. Real embedding values are learned from data, and individual dimensions usually do not have simple human-readable meanings.

## 2. Sparse representations vs. dense representations

### One-hot encoding

Suppose our vocabulary is `["cat", "dog", "banana"]`. One-hot encoding assigns each word a vector with one 1 and all other values 0.

| Word | Vector |
|---|---|
| cat | [1, 0, 0] |
| dog | [0, 1, 0] |
| banana | [0, 0, 1] |

These vectors are easy to understand, but they do not directly express similarity: the dot product between any two different one-hot vectors is zero. The representation also grows with vocabulary size.

### Bag of Words and TF-IDF

Bag of Words represents a document using token counts. TF-IDF weights terms according to their frequency in a document and their rarity across the document collection. Both are useful sparse representations, but they do not normally learn a dense semantic vector for each word.

### Dense word embeddings

An embedding might represent each word using 50, 100, 300, or another chosen number of dimensions. The vector is dense because many values are non-zero. The embedding dimension is usually much smaller than the vocabulary size.

| Method | Representation | Main idea |
|---|---|---|
| One-hot | Sparse vector | Word identity |
| Bag of Words | Sparse document vector | Token counts |
| TF-IDF | Sparse document vector | Weighted token importance |
| Word embeddings | Dense word vector | Learned patterns from usage/context |
| Transformer embeddings | Dense contextual vector | Representation depends on surrounding text |

## 3. The distributional hypothesis

A common intuition behind embeddings is the **distributional hypothesis**: words that occur in similar contexts tend to have related meanings or uses.

Compare:

- The **cat** sleeps on the sofa.
- The **dog** sleeps on the sofa.
- The **kitten** sleeps on the sofa.

The words `cat`, `dog`, and `kitten` appear in similar contexts. Algorithms can use these patterns to learn useful vector representations.

This does not mean that the model understands words exactly as humans do. It learns statistical regularities in the training data, and those regularities can include bias or misleading associations.

## 4. How are embeddings learned?

An embedding model starts with numerical parameters for vocabulary items and updates them during training. Depending on the method, training may use:

- Nearby words as context.
- A target word to predict its surrounding context.
- Surrounding context to predict a target word.
- Global word co-occurrence statistics.
- A language-model objective that predicts tokens using their context.

Word2Vec is a classic predictive approach. GloVe learns from global co-occurrence statistics. Transformer models learn contextual representations through neural-network training objectives.

See [Word2Vec](../05_Word2Vec/README.md) and [GloVe](../06_GloVe/README.md) for the dedicated lessons.

## 5. Word embedding matrix

A vocabulary with (V) words and embedding dimension (d) can be represented by an embedding matrix with shape (V \times d).

- (V): number of vocabulary entries.
- (d): number of numerical values used for each word.
- Each row corresponds to one vocabulary entry.

For example, if a vocabulary has 1,000 words and each word uses 50 numbers, the embedding matrix has shape `(1000, 50)`. A token's integer ID selects the corresponding row.

The integer token ID is not itself a semantic representation. It is an index used to look up the learned vector.

## 6. Similarity between embeddings

Word vectors can be compared with cosine similarity. For non-zero vectors (a) and (b):

`cosine_similarity(a, b) = (a · b) / (||a|| × ||b||)`

Cosine similarity measures the angle between vectors. Values closer to 1 indicate similar directions; values around 0 indicate near-orthogonal directions; values closer to -1 indicate opposite directions. The practical interpretation depends on how the vectors were trained and what the data contains.

Do not assume that any two words with similar vectors are synonyms. Related words, opposites, and words used in similar contexts can all be close in an embedding space.

## 7. Static vs. contextual embeddings

### Static embeddings

Traditional Word2Vec and GloVe generally assign one learned vector to each vocabulary word. A word therefore receives the same vector regardless of the sentence in which it appears.

For example, the word `bank` occurs in both:

- I deposited money at the **bank**.
- We sat on the river **bank**.

A static embedding cannot create a different token vector for each of these contexts.

### Contextual embeddings

Transformer-based models compute token representations using surrounding words. As a result, the representation of `bank` can differ between the financial and river examples.

Contextual representations are powerful, but their exact behaviour depends on the model, tokenizer, layer, and pooling strategy.

## 8. Practical examples in this folder

### Python script

Run the standalone demonstration:

```bash
python Word_Embeddings.py
```

It uses Python's standard library for illustrative dense vectors, vector similarity, vocabulary indexing, and sentence-vector averaging. The manually defined vectors are **teaching examples**, not pretrained embeddings.

### Jupyter Notebook

Open `Word_Embeddings.ipynb` for a longer lesson containing:

1. Text-to-number motivation.
2. One-hot and dense vector comparisons.
3. Vocabulary-to-index mapping and embedding matrices.
4. Vector arithmetic and cosine similarity.
5. Sentence vectors and average pooling.
6. A small corpus and context windows.
7. An optional Gensim Word2Vec section.
8. Static versus contextual embeddings.
9. Practical use cases, evaluation ideas, and limitations.

The optional Gensim cells require Gensim to be installed in the same Python environment as the notebook kernel:

```bash
python -m pip install gensim
```

If the import fails in Jupyter, check the kernel interpreter with `import sys; print(sys.executable)` and install Gensim into that environment. The tiny sample corpus is for demonstrating the API only; it is not large enough to produce reliable general-purpose vectors.

## 9. Turning words into sentence or document vectors

A simple baseline is to average the embeddings of the tokens in a sentence. If a sentence has token vectors (v_1, v_2, \ldots, v_n), its mean vector is:

`sentence_vector = (v1 + v2 + ... + vn) / n`

This produces a fixed-size vector regardless of sentence length. However, averaging loses word order and can blur negation or different meanings. For example, `good` and `not good` may end up with overly similar averaged vectors if the representation does not adequately model composition.

More advanced methods include weighted averages, recurrent models, convolutional models, transformer representations, and dedicated sentence-embedding models.

## 10. Where are embeddings used?

- Semantic search and retrieval.
- Similarity and duplicate-text detection.
- Recommendation and matching systems.
- Text classification and sentiment analysis.
- Clustering words, documents, or user queries.
- Ranking candidate answers or search results.
- As input representations in neural NLP systems.

An embedding is not a complete NLP solution by itself. The downstream model, training data, evaluation method, and task all matter.

## 11. Limitations and responsible use

- **Data dependence:** learned relationships reflect the training corpus.
- **Bias:** social or cultural biases in text may be encoded in vectors.
- **Out-of-vocabulary words:** older static models may not represent unseen words well.
- **Polysemy:** a single static vector may mix several senses of a word.
- **Domain shift:** vectors trained on one domain may perform poorly in another.
- **Evaluation:** a visually plausible similarity is not proof of task performance.
- **Small corpus warning:** toy examples illustrate code and concepts, not production quality.

For a real project, select the representation based on the task, measure performance on held-out data, and check whether errors affect user groups differently.

## 12. Recommended learning order

1. Review [Bag of Words](../01_Bag_of_Words/README.md), [N-Grams](../02_N_Grams/README.md), and [TF-IDF](../03_TF_IDF/README.md).
2. Understand dense vectors and cosine similarity in this folder.
3. Study [Word2Vec](../05_Word2Vec/README.md) for CBOW and Skip-gram.
4. Study [GloVe](../06_GloVe/README.md) for co-occurrence-based embeddings.
5. Continue to neural NLP and transformer-based contextual representations.

## Key points to remember

- Embeddings are learned dense vector representations.
- Similar contexts often produce related vector representations.
- Vector dimensions are usually not directly interpretable by themselves.
- Cosine similarity compares vector direction, not a guaranteed measure of human meaning.
- Static embeddings give a word a single vector; contextual models can represent it differently by context.
- Sentence vectors made by averaging are simple but lose word order and some meaning.
- Always evaluate embeddings on the task and data that matter.

## References

- [Word2Vec: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)
- [Gensim Word2Vec documentation](https://radimrehurek.com/gensim/models/word2vec.html)
- [scikit-learn cosine similarity documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
