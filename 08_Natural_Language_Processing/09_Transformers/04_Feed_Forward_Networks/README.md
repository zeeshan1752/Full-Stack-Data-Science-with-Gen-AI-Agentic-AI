# Feed-Forward Networks

Each original Transformer encoder and decoder layer contains a position-wise feed-forward network. It applies the same two linear transformations independently at each sequence position, with a ReLU activation between them:

~~~text
FFN(x) = max(0, x W_1 + b_1) W_2 + b_2
~~~

In the paper's base model, the hidden width is 2048 and the model width is 512. The transformation is shared across positions within a layer, while different layers have their own parameters.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
