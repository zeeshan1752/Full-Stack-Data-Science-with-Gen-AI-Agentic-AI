# Positional Encoding

Self-attention alone does not encode token order. The original Transformer adds positional encodings to token embeddings at the bottom of the encoder and decoder stacks.

For position pos and model dimension d_model, the paper uses sine and cosine functions:

~~~text
PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
~~~

The encoding has the same dimension as the token embedding, so the two vectors can be added. The paper also reports experiments with learned positional embeddings.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
