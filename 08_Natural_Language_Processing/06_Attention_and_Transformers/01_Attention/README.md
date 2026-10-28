# 08. Attention Mechanism

Attention lets a model assign different weights to different parts of an input when building a representation. Instead of compressing all earlier information into one fixed-size recurrent state, attention can directly compare positions in a sequence.

## Learning objectives

- Understand queries, keys, and values.
- Explain attention scores and normalized weights.
- Describe self-attention versus cross-attention.
- Explain why multi-head attention uses several attention projections.

## Learning sequence

- [Introduction to Attention](README.md#introduction-to-attention)
- [Query, Key and Value](README.md#query-key-and-value-2)
- [Scaled Dot-Product Attention](README.md#scaled-dot-product-attention)
- [Self-Attention and Cross-Attention](README.md#self-attention-and-cross-attention)
- [Multi-Head Attention](README.md#multi-head-attention)

## Query, key, and value

For each token, the model projects its representation into a query, key, and value vector. A query is compared with keys to produce scores. Scores are normalized with softmax to obtain weights, and those weights combine the value vectors.

Scaled dot-product attention is commonly written as:

\[
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Here, d_k is the key-vector dimension. Scaling helps keep dot-product scores from becoming too large as the dimension grows.

## Types of attention

- **Self-attention:** queries, keys, and values come from the same sequence.
- **Cross-attention:** queries come from one sequence while keys and values come from another, as in an encoder-decoder model.
- **Multi-head attention:** several learned attention operations run in parallel, allowing the model to represent different relationships.

## Intuition

In “The animal did not cross the road because it was tired”, the representation of “it” may need to connect to “animal”. Attention provides a mechanism for modeling such relationships; it does not guarantee correct interpretation.

## Practical notes

Attention weights can help inspect model behavior, but they are not automatically a complete explanation of a model’s decision. Masks can prevent attention to padding or future tokens in autoregressive generation.

## Next

Continue to [Transformers](../02_Transformer_Architecture/README.md).

## Trainer paper reference

The supplied PDF is the original Transformer paper, *Attention Is All You Need* (Vaswani et al., 2017). Its attention equations and examples inform the notes in this module. See [the paper](https://arxiv.org/abs/1706.03762).

---

## Introduction to Attention

Attention maps a query and a set of key-value pairs to an output. A compatibility score compares the query with each key; a softmax turns the scores into weights; the output is a weighted sum of the values.

Attention lets a position gather information from other positions in a sequence. In self-attention, the query, key, and value vectors come from the same sequence representation.

The original Transformer paper replaces recurrence with attention layers so sequence positions can be processed in parallel within a layer. See [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Multi-Head Attention

Multi-head attention runs several attention operations on learned projections of Q, K, and V. Their outputs are concatenated and projected to the model dimension.

~~~text
head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
~~~

Different heads can represent different relationships or positions. In the original paper's base model, h=8 and each head uses key and value dimensions of 64. These are paper settings, not universal requirements.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Query, Key and Value

For each token representation, learned projections produce a query (Q), key (K), and value (V).

- A query represents what a position is looking for.
- A key represents what a position offers for matching.
- A value contains the information that can be passed to other positions.

Attention scores compare queries against keys. The normalized scores weight the corresponding values. The query, key, and value analogy is only an intuition; the computation uses learned vectors and matrix operations.

The original Transformer packs queries, keys, and values into matrices Q, K, and V. Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Scaled Dot-Product Attention

The original Transformer computes:

~~~text
Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V
~~~

QK^T scores the compatibility of each query with every key. Dividing by sqrt(d_k) controls score scale before softmax. Softmax converts the scores to weights, and multiplying by V forms weighted value summaries.

A mask can set disallowed scores to negative infinity before softmax. This is used in a decoder to prevent a position from reading future target tokens.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).

---

## Self-Attention and Cross-Attention

### Self-attention

Queries, keys, and values come from the same sequence. Each position can use information from other allowed positions in that sequence. Encoder self-attention can attend across the input; decoder self-attention uses a causal mask so each position cannot see future output tokens.

### Cross-attention

Queries come from the decoder, while keys and values come from the encoder output. This lets each decoder position select information from the input sequence.

These are the three attention uses described for the original Transformer: encoder self-attention, masked decoder self-attention, and encoder-decoder attention. Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
