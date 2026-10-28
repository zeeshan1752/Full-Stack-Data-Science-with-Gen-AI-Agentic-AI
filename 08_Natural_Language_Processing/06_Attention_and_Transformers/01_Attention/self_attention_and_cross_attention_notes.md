# Self-Attention and Cross-Attention

## Self-attention

Queries, keys, and values come from the same sequence. Each position can use information from other allowed positions in that sequence. Encoder self-attention can attend across the input; decoder self-attention uses a causal mask so each position cannot see future output tokens.

## Cross-attention

Queries come from the decoder, while keys and values come from the encoder output. This lets each decoder position select information from the input sequence.

These are the three attention uses described for the original Transformer: encoder self-attention, masked decoder self-attention, and encoder-decoder attention. Reference: [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762).
