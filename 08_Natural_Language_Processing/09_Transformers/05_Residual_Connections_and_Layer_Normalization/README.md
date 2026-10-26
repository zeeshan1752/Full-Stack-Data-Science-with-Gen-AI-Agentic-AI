# Residual Connections and Layer Normalization

The original Transformer wraps every encoder and decoder sublayer with a residual connection and layer normalization:

~~~text
LayerNorm(x + Sublayer(x))
~~~

The sublayer output is added to its input, then normalized. The residual path helps information and gradients move through stacked layers. The original paper uses this order; other Transformer variants may use a different normalization arrangement.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
