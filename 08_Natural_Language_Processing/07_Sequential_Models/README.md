# 07. Sequential Models

Sequential models process ordered inputs such as words in a sentence. Order matters: “dog bites person” and “person bites dog” contain similar words but express different events.

## Learning objectives

- Explain why sequence order matters in language.
- Describe recurrent hidden state at a high level.
- Compare RNN, LSTM, and GRU architectures.
- Recognize why long-range dependencies are difficult for basic RNNs.

## Learning sequence

- [RNN](01_RNN/README.md)
- [LSTM](02_LSTM/README.md)
- [GRU](03_GRU/README.md)

## Core idea

At each time step, a recurrent network combines the current input with information carried from earlier steps. This hidden state is updated as the sequence is read. In a basic RNN, the learning signal may shrink or grow excessively over long sequences.

An LSTM uses gates and a cell state to help retain or discard information. A GRU uses a smaller set of gates and often has fewer parameters than an LSTM. The best choice depends on the task, data, and compute budget.

## Comparison

| Model | Main idea | Useful context |
|---|---|---|
| RNN | Reuses a hidden state at each step | Simple sequence-model baseline |
| LSTM | Uses gates with a cell state | Helps with longer dependencies |
| GRU | Uses update and reset gates | Simpler gated alternative to LSTM |

## Where they are used

Recurrent networks have been used for language modeling, sequence labeling, and sequence-to-sequence tasks. Transformers are now common for many large-scale NLP tasks because attention can connect distant positions and allows more parallel processing during training.

## Implementation note

Document the tokenizer, vocabulary size, padding strategy, sequence length, and evaluation split. Do not compare models using different data splits without noting the difference.

## Next

Continue to [Attention Mechanism](../08_Attention_Mechanism/README.md).
