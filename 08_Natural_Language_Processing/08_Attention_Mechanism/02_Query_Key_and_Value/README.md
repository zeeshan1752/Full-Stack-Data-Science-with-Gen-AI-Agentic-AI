# Query, Key and Value

For each token representation, learned projections produce a query (Q), key (K), and value (V).

- A query represents what a position is looking for.
- A key represents what a position offers for matching.
- A value contains the information that can be passed to other positions.

Attention scores compare queries against keys. The normalized scores weight the corresponding values. The query, key, and value analogy is only an intuition; the computation uses learned vectors and matrix operations.

The original Transformer packs queries, keys, and values into matrices Q, K, and V. Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
