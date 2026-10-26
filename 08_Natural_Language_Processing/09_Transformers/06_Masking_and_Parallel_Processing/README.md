# Masking and Parallel Processing

## Causal masking

Decoder self-attention must not use future target tokens. Before softmax, the model masks scores for illegal future positions so those positions receive zero attention weight. This preserves autoregressive prediction.

## Parallel processing

Unlike an RNN, self-attention does not require one sequence position to wait for the previous position within the same layer. The original Transformer can compute attention across positions in parallel during training. The decoder still generates output tokens autoregressively at inference time.

Full self-attention compares every pair of positions, so its attention-score matrix grows quadratically with sequence length.

Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
