# GloVe (Global Vectors for Word Representation)

## 1. What Is GloVe?

**GloVe** is a word-embedding method that learns dense word vectors from global word co-occurrence statistics in a text corpus. It was introduced by researchers at Stanford.

The name means **Global Vectors for Word Representation**. GloVe combines information from how often words occur together across a corpus with a model that learns vector representations.

Word2Vec learns from local context prediction tasks (CBOW or Skip-gram). GloVe instead builds and factorizes information from a word–word co-occurrence matrix.

## 2. Why Use GloVe?

A text corpus contains useful information about which words tend to appear near each other. For example, a corpus about pets may often place *cat*, *dog*, *pet*, and *animal* in related contexts.

GloVe attempts to encode these statistical relationships in a vector space. Words with related usage may end up with similar vectors, depending on the training data and configuration.

Embeddings are learned from data; individual vector dimensions usually do not have simple human-readable meanings.

## 3. How GloVe Works

A simplified training workflow is:

1. Collect and tokenize a text corpus.
2. Build a vocabulary.
3. Count how often words co-occur within a chosen context window.
4. Store these counts in a word–word co-occurrence matrix.
5. Learn word and context vectors whose dot products model the logarithm of co-occurrence counts.
6. Use the learned word vectors in downstream NLP tasks.

The co-occurrence matrix can be large and sparse for a large vocabulary, so practical implementations use efficient data structures and weighting.

## 4. A Small Co-occurrence Example

Suppose the toy corpus contains:

- `cats chase mice`
- `dogs chase cats`
- `cats like pets`

Using a context window and a simplified counting rule, a co-occurrence table might contain counts such as:

| Word | cats | chase | mice | dogs | pets |
|---|---:|---:|---:|---:|---:|
| cats | — | 2 | 1 | 1 | 1 |
| chase | 2 | — | 1 | 1 | 0 |
| mice | 1 | 1 | — | 0 | 0 |
| dogs | 1 | 1 | 0 | — | 0 |
| pets | 1 | 0 | 0 | 0 | — |

This table is **illustrative**, not the output of a fully specified counting program. Exact counts depend on tokenization, context-window size, directionality, and whether self-co-occurrences are included.

The key idea is that GloVe uses corpus-wide co-occurrence information rather than treating each word independently.

## 5. The GloVe Objective

Let `X_ij` be the number of times word `j` appears in the context of word `i`. GloVe learns word vectors `w_i`, context vectors `w̃_j`, and bias terms `b_i` and `b̃_j`.

Its core relationship is commonly written as:

`w_i^T ~{w}_j + b_i + ~{b}_j \approx \log(X_{ij})`

A weighted least-squares objective is used to fit these relationships:

`J = \sum_{i,j} f(X_{ij}) (w_i^T \tilde{w}_j + b_i + \tilde{b}_j - \log X_{ij})^2`

Here, `f(X_ij)` is a weighting function that limits the influence of extremely frequent co-occurrences and reduces the effect of very rare counts. Implementations handle zero counts without taking the logarithm of zero.

You do not need to memorize the objective first. Understand the sequence: **co-occurrence counts → weighted objective → learned vectors**.

## 6. GloVe vs. Word2Vec

| Feature | GloVe | Word2Vec |
|---|---|---|
| Main learning signal | Global word co-occurrence counts | Local context prediction |
| Common architectures/objectives | Weighted factorization-style objective | CBOW and Skip-gram |
| Training representation | Co-occurrence matrix/statistics | Target-context training examples |
| Output | Dense word vectors | Dense word vectors |
| Context-specific vector for every occurrence | No, standard GloVe is static | No, standard Word2Vec is static |

Neither method guarantees that similar words will always have similar vectors. The result depends on the corpus, vocabulary, hyperparameters, and training process.

## 7. Using a Pretrained GloVe Vector File

The GloVe research release provides pretrained vector files. Download a compatible vector file from the official project page, then load it locally. This example expects a text-format vector file where each line contains a word followed by its vector values.

```python
from pathlib import Path
import numpy as np

vector_path = Path("glove.6B.50d.txt")
embeddings = {}

with vector_path.open("r", encoding="utf-8") as file:
    for line in file:
        values = line.rstrip().split()
        word = values[0]
        vector = np.asarray(values[1:], dtype=np.float32)
        embeddings[word] = vector

print("Vocabulary size:", len(embeddings))

word = "king"
if word in embeddings:
    print("Vector shape:", embeddings[word].shape)
    print("First five values:", embeddings[word][:5])
else:
    print(f"{word!r} is not in this vocabulary.")
```

**Important:** Download the vector file separately and follow its license and usage terms. The example loads the file into memory, so use a smaller vector file if your machine has limited RAM. This code has not been executed as part of this documentation update.

## 8. Limitations

- Standard GloVe vectors are static: a word usually has the same vector in different sentences.
- Out-of-vocabulary words have no vector unless handled separately.
- Large pretrained vector files can require substantial memory.
- Biases and gaps in the training corpus may be reflected in the learned vectors.
- Similarity in vector space is a statistical relationship, not proof that two words mean exactly the same thing.

## 9. Points to Remember

- GloVe stands for **Global Vectors for Word Representation**.
- It learns embeddings using global word–word co-occurrence statistics.
- Word2Vec learns from context prediction; GloVe learns from co-occurrence statistics.
- Both are classic static word-embedding methods.
- The corpus and training configuration strongly affect embedding quality.

## 10. References

- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)
- [GloVe paper (Pennington, Socher, and Manning, 2014)](https://aclanthology.org/D14-1162/)
