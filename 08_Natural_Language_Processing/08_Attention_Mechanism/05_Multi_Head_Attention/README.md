# Multi-Head Attention

Multi-head attention runs several attention operations on learned projections of Q, K, and V. Their outputs are concatenated and projected to the model dimension.

~~~text
head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
~~~

Different heads can represent different relationships or positions. In the original paper's base model, h=8 and each head uses key and value dimensions of 64. These are paper settings, not universal requirements.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
