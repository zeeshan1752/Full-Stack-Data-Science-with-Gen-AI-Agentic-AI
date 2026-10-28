# Transformer Architecture

The original Transformer maps an input sequence through an encoder and generates an output sequence through a decoder. Both are stacks of attention and position-wise feed-forward sublayers.

The original paper uses six encoder layers and six decoder layers. Each encoder layer contains multi-head self-attention and a feed-forward network. Each decoder layer adds masked self-attention and encoder-decoder attention. Residual connections and layer normalization wrap each sublayer, and positional encodings supply sequence order.

These settings describe the 2017 paper's model; later Transformer variants change the number of layers and may omit the encoder. Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
