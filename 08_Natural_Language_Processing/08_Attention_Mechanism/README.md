# 08. Attention Mechanism

Attention lets a model assign different weights to different parts of an input when building a representation. Instead of compressing all earlier information into one fixed-size recurrent state, attention can directly compare positions in a sequence.

## Learning objectives

- Understand queries, keys, and values.
- Explain attention scores and normalized weights.
- Describe self-attention versus cross-attention.
- Explain why multi-head attention uses several attention projections.

## Learning sequence

- [Introduction to Attention](01_Introduction_to_Attention/README.md)
- [Query, Key and Value](02_Query_Key_and_Value/README.md)
- [Scaled Dot-Product Attention](03_Scaled_Dot_Product_Attention/README.md)
- [Self-Attention and Cross-Attention](04_Self_Attention_and_Cross_Attention/README.md)
- [Multi-Head Attention](05_Multi_Head_Attention/README.md)

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

Continue to [Transformers](../09_Transformers/README.md).

## Trainer paper reference

The supplied PDF is the original Transformer paper, *Attention Is All You Need* (Vaswani et al., 2017). Its attention equations and examples inform the notes in this module. See [the paper](https://arxiv.org/abs/1706.03762).
