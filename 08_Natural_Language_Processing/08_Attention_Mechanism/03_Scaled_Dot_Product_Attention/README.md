# Scaled Dot-Product Attention

The original Transformer computes:

~~~text
Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V
~~~

QK^T scores the compatibility of each query with every key. Dividing by sqrt(d_k) controls score scale before softmax. Softmax converts the scores to weights, and multiplying by V forms weighted value summaries.

A mask can set disallowed scores to negative infinity before softmax. This is used in a decoder to prevent a position from reading future target tokens.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
