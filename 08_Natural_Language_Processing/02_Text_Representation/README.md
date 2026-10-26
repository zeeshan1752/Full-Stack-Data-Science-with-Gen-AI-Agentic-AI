# 02. Text Representation

Text representation converts words, sentences, and documents into numerical features that machine-learning models can process.

## Learning sequence

- [Bag of Words](01_Bag_of_Words/README.md) — Represent documents using token counts.
- [N-Grams](02_N_Grams/README.md) — Capture short sequences of adjacent tokens.
- [TF-IDF](03_TF_IDF/README.md) — Weight terms by document frequency.
- [Word Embeddings](04_Word_Embeddings/README.md) — Understand dense vectors, embedding dimensions, similarity, sentence pooling, and static vs contextual representations.
- [Word2Vec](05_Word2Vec/README.md) — Learn CBOW and Skip-gram word representations.
- [GloVe](06_GloVe/README.md) — Explore global word co-occurrence embeddings.

## Recommended order

Start with Bag of Words, N-Grams, and TF-IDF to understand sparse features. Then learn what dense word embeddings represent before studying Word2Vec and GloVe in detail.

The Word Embeddings folder includes a long Jupyter Notebook, a standard-library Python demonstration, and conceptual notes. The manually written vectors in introductory examples are illustrative, while the optional Gensim Word2Vec notebook section learns vectors from a tiny corpus only to demonstrate the API. It should not be treated as a source of reliable general-purpose embeddings.
