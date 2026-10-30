# 09. Transformers

The Transformer is a neural architecture built around attention rather than recurrence. It is the foundation for many modern language models, including encoder-only models such as BERT and decoder-only models such as GPT.

## Learning objectives

- Identify the main components of a Transformer block.
- Distinguish encoder and decoder roles.
- Explain positional information, masks, residual connections, and layer normalization.
- Understand the difference between an architecture lesson and using a pretrained model.

## Learning sequence

- [Transformer Architecture](README.md#transformer-architecture)
- [Encoder and Decoder](README.md#encoder-and-decoder)
- [Positional Encoding](README.md#positional-encoding)
- [Feed-Forward Networks](README.md#feed-forward-networks)
- [Residual Connections and Layer Normalization](README.md#residual-connections-and-layer-normalization)
- [Masking and Parallel Processing](README.md#masking-and-parallel-processing)
- [GPT-2 Chunking and Hugging Face Demos](../03_GPT2_And_HF_Demos/README.md) (supplementary trainer material)

## What happens in a Transformer block?

A typical block applies multi-head attention, then a position-wise feed-forward network, with residual connections and layer normalization around sublayers. Token embeddings need positional information because attention alone does not encode sequence order like recurrence does.

Encoder-only models build contextual representations of the input. Decoder-only models predict the next token using causal masking. Encoder-decoder models use an encoder for the input and a decoder for generated output.

## Important distinctions

- **Tokenization:** converts text into model-specific token IDs; tokens are not always whole words.
- **Context window:** limits how many tokens can be processed together.
- **Chunking:** splits longer content into smaller segments; it does not itself summarize or retrieve information.
- **Generation:** new tokens are selected from model predictions.
- **Fine-tuning:** updates model parameters on a task or dataset; using a pretrained model without updating weights is inference.

## Trainer notebooks

The GPT-2 demo notebooks are retained as supplementary material. The Hugging Face demo no longer includes a Colab Drive-mount cell. Check model limits and reserve space for generated tokens: if a prompt fills the context window, there may be no room for continuation.

## Next

Continue to [BERT](../../06_BERT/README.md). Optional packages are listed in Optional Hugging Face and PyTorch packages can be installed separately when needed..

## Trainer paper reference

The supplied PDF is the original Transformer paper, *Attention Is All You Need* (Vaswani et al., 2017). Its encoder-decoder architecture, attention, positional encoding, feed-forward layers, residual connections, normalization, and masking are reflected in the topic notes. See [the paper](https://arxiv.org/abs/1706.03762).

---

## Encoder and Decoder

### Encoder

The encoder converts input token representations into contextual representations. In the original Transformer, each of its six layers contains multi-head self-attention followed by a position-wise feed-forward network. Encoder self-attention can use information from every input position.

### Decoder

The decoder generates output tokens autoregressively. Each original decoder layer contains masked self-attention, encoder-decoder attention, and a position-wise feed-forward network. The causal mask blocks attention to future output positions; cross-attention uses encoder outputs as keys and values.

GPT-2 is decoder-only, so it is a useful contrast to the original encoder-decoder Transformer. See the trainer notebooks in 07_GPT2_Chunking_and_HF_Demos.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Feed-Forward Networks

Each original Transformer encoder and decoder layer contains a position-wise feed-forward network. It applies the same two linear transformations independently at each sequence position, with a ReLU activation between them:

~~~text
FFN(x) = max(0, x W_1 + b_1) W_2 + b_2
~~~

In the paper's base model, the hidden width is 2048 and the model width is 512. The transformation is shared across positions within a layer, while different layers have their own parameters.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Masking and Parallel Processing

### Causal masking

Decoder self-attention must not use future target tokens. Before softmax, the model masks scores for illegal future positions so those positions receive zero attention weight. This preserves autoregressive prediction.

### Parallel processing

Unlike an RNN, self-attention does not require one sequence position to wait for the previous position within the same layer. The original Transformer can compute attention across positions in parallel during training. The decoder still generates output tokens autoregressively at inference time.

Full self-attention compares every pair of positions, so its attention-score matrix grows quadratically with sequence length.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Positional Encoding

Self-attention alone does not encode token order. The original Transformer adds positional encodings to token embeddings at the bottom of the encoder and decoder stacks.

For position pos and model dimension d_model, the paper uses sine and cosine functions:

~~~text
PE(pos, 2i)   = sin(pos / 10000^(2i / d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
~~~

The encoding has the same dimension as the token embedding, so the two vectors can be added. The paper also reports experiments with learned positional embeddings.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Residual Connections and Layer Normalization

The original Transformer wraps every encoder and decoder sublayer with a residual connection and layer normalization:

~~~text
LayerNorm(x + Sublayer(x))
~~~

The sublayer output is added to its input, then normalized. The residual path helps information and gradients move through stacked layers. The original paper uses this order; other Transformer variants may use a different normalization arrangement.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Transformer Architecture

The original Transformer maps an input sequence through an encoder and generates an output sequence through a decoder. Both are stacks of attention and position-wise feed-forward sublayers.

The original paper uses six encoder layers and six decoder layers. Each encoder layer contains multi-head self-attention and a feed-forward network. Each decoder layer adds masked self-attention and encoder-decoder attention. Residual connections and layer normalization wrap each sublayer, and positional encodings supply sequence order.

These settings describe the 2017 paper's model; later Transformer variants change the number of layers and may omit the encoder. Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
