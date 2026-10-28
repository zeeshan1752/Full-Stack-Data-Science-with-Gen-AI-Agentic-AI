# Introduction to Attention

Attention maps a query and a set of key-value pairs to an output. A compatibility score compares the query with each key; a softmax turns the scores into weights; the output is a weighted sum of the values.

Attention lets a position gather information from other positions in a sequence. In self-attention, the query, key, and value vectors come from the same sequence representation.

The original Transformer paper replaces recurrence with attention layers so sequence positions can be processed in parallel within a layer. See [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
