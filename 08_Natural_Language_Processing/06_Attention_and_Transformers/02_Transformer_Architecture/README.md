# 09. Transformers

The Transformer is a neural architecture built around attention rather than recurrence. It is the foundation for many modern language models, including encoder-only models such as BERT and decoder-only models such as GPT.

## Learning objectives

- Identify the main components of a Transformer block.
- Distinguish encoder and decoder roles.
- Explain positional information, masks, residual connections, and layer normalization.
- Understand the difference between an architecture lesson and using a pretrained model.

## Learning sequence

- [Transformer Architecture](transformer_architecture_notes.md)
- [Encoder and Decoder](encoder_and_decoder_notes.md)
- [Positional Encoding](positional_encoding_notes.md)
- [Feed-Forward Networks](feed_forward_networks_notes.md)
- [Residual Connections and Layer Normalization](residual_connections_and_layer_normalization_notes.md)
- [Masking and Parallel Processing](masking_and_parallel_processing_notes.md)
- [GPT-2 Chunking and Hugging Face Demos](../03_GPT2_and_HF_Demos/README.md) (supplementary trainer material)

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

The GPT-2 demo notebooks are retained as supplementary material. Some cells are specific to Google Colab and may require changes in a local environment. Check model limits and reserve space for generated tokens: if a prompt fills the context window, there may be no room for continuation.

## Next

Continue to [BERT](../../07_BERT/README.md). Optional packages are listed in Optional Hugging Face and PyTorch packages can be installed separately when needed..

## Trainer paper reference

The supplied PDF is the original Transformer paper, *Attention Is All You Need* (Vaswani et al., 2017). Its encoder-decoder architecture, attention, positional encoding, feed-forward layers, residual connections, normalization, and masking are reflected in the topic notes. See [the paper](https://arxiv.org/abs/1706.03762).

