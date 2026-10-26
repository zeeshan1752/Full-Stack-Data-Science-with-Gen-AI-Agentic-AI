# Transformer Paper and Reading Resources

The trainer archive includes a copy of the original paper **Attention Is All You Need** (Vaswani et al., 2017). It introduces the Transformer architecture and explains the encoder/decoder stacks, scaled dot-product attention, multi-head attention, positional encoding, residual connections, layer normalization, and masking.

## Paper

- [Read the paper on arXiv](https://arxiv.org/abs/1706.03762)
- [Open the PDF](https://arxiv.org/pdf/1706.03762)

The original trainer file is named `transformer.pdf`. Keep the PDF in this `Resources` folder when adding it to the repository, using the descriptive filename `Attention_Is_All_You_Need.pdf`. This avoids mixing the paper with lesson notebooks and makes it easy to find from the Transformer module.

## Suggested reading order

1. Abstract and Introduction — why attention-only sequence modeling was proposed.
2. Encoder and Decoder Stacks — the overall model layout.
3. Scaled Dot-Product Attention and Multi-Head Attention — how queries, keys, and values are combined.
4. Positional Encoding — how token order is represented.
5. Masking — how the decoder avoids looking at future target tokens.
6. Experiments and Conclusion — the paper's original translation tasks and findings.

See the module's [Transformer notes](../README.md) for beginner-friendly explanations of these components.
