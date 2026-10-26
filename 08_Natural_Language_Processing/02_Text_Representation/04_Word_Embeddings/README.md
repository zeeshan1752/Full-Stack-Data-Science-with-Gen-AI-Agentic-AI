# 04. Word Embeddings

Word embeddings represent words as **dense numerical vectors** learned from data. They help NLP systems represent usage patterns beyond a word's identity or raw frequency.

This folder contains conceptual notes, a standard-library Python demonstration, and an extended Jupyter Notebook. The notebook uses direct, inline code rather than custom `def` function definitions, and saved outputs are included for the examples.

## Learning objectives

- Explain why NLP systems need numerical text representations.
- Compare one-hot encoding, Bag of Words, TF-IDF, and dense embeddings.
- Understand vocabulary indices, embedding dimensions, and embedding matrices.
- Calculate vector operations and cosine similarity.
- Rank nearest neighbours and create sentence vectors with mean or weighted pooling.
- Explain context windows and the distributional hypothesis.
- Understand Word2Vec CBOW and Skip-gram at a high level.
- Distinguish static word embeddings from contextual transformer embeddings.
- Identify embedding applications, limitations, and evaluation concerns.

## Files

- [Extended Jupyter Notebook](Word_Embeddings.ipynb) — long lesson with explanations, code cells, and saved outputs.
- [Python examples](Word_Embeddings.py) — standalone standard-library demonstrations.
- [Word2Vec lesson](../05_Word2Vec/README.md) — dedicated Word2Vec coverage.
- [GloVe lesson](../06_GloVe/README.md) — dedicated GloVe coverage.

## Topics covered in the notebook

1. Why text must be represented numerically.
2. One-hot encoding and its limitations.
3. Bag of Words and TF-IDF recap.
4. Dense vectors and embedding dimensions.
5. Vocabulary-to-index mapping and embedding matrix lookup.
6. Vector addition, subtraction, and scaling.
7. Cosine similarity with a worked calculation.
8. Similarity scores and nearest-neighbour ranking.
9. Sentence vectors using mean pooling.
10. Weighted sentence-vector pooling.
11. Context windows and target-context pairs.
12. Preparing a small text corpus.
13. Optional Word2Vec training using Gensim.
14. CBOW and Skip-gram.
15. Static vs. contextual embeddings.
16. Representation-method comparison.
17. Applications, evaluation, limitations, and references.

## How to run

Open `Word_Embeddings.ipynb` in Jupyter Notebook or JupyterLab and run the cells from top to bottom.

To run the standalone script:

```bash
python Word_Embeddings.py
```

For the optional Gensim examples, install the package in the same Python environment as the active notebook kernel:

```bash
python -m pip install gensim
```

If the import fails, check the interpreter using `import sys; print(sys.executable)` and install Gensim into that environment. If Gensim is unavailable, the notebook skips the model-training cells gracefully.

## Important notes

- The manually written vectors are illustrative values, not pretrained embeddings.
- Cosine similarity measures vector direction; it is not a universal score of human meaning.
- Mean pooling loses word order and may blur negation or multiple senses.
- Word2Vec and GloVe generally provide static vectors, while transformer models can create contextual representations.
- The notebook's tiny Word2Vec corpus demonstrates the API only. Use a larger, representative corpus or a suitable pretrained model for real applications.

## References

- [Word2Vec: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)
- [Gensim Word2Vec documentation](https://radimrehurek.com/gensim/models/word2vec.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [scikit-learn cosine similarity documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
