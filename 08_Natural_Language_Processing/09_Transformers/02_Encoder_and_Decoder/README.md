# Encoder and Decoder

## Encoder

The encoder converts input token representations into contextual representations. In the original Transformer, each of its six layers contains multi-head self-attention followed by a position-wise feed-forward network. Encoder self-attention can use information from every input position.

## Decoder

The decoder generates output tokens autoregressively. Each original decoder layer contains masked self-attention, encoder-decoder attention, and a position-wise feed-forward network. The causal mask blocks attention to future output positions; cross-attention uses encoder outputs as keys and values.

GPT-2 is decoder-only, so it is a useful contrast to the original encoder-decoder Transformer. See the trainer notebooks in 07_GPT2_Chunking_and_HF_Demos.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
