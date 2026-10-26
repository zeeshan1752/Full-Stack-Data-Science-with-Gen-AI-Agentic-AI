# 10. BERT

BERT (Bidirectional Encoder Representations from Transformers) is an encoder-only Transformer model pretrained to build contextual representations of text. Its representations can be adapted to tasks such as text classification and named-entity recognition.

## Learning objectives

- Explain bidirectional context for an encoder.
- Describe WordPiece tokenization and special tokens.
- Explain masked language modeling at a high level.
- Distinguish pretraining from task-specific fine-tuning.

## Learning sequence

- [BERT Architecture](01_BERT_Architecture/README.md)
- [Bidirectional Contextual Representations](02_Bidirectional_Contextual_Representations/README.md)
- [WordPiece Tokenization](03_WordPiece_Tokenization/README.md)
- [Masked Language Modeling](04_Masked_Language_Modeling/README.md)
- [Pretraining and Fine-Tuning](05_Pretraining_and_Fine_Tuning/README.md)
- [BERT for Text Classification and NER](06_BERT_for_Text_Classification_and_NER/README.md)
- [Hugging Face Transformers](07_Hugging_Face_Transformers/README.md)

## How BERT is used

1. A tokenizer converts text into token IDs and adds model-specific special tokens.
2. The encoder uses self-attention to build contextual representations.
3. A task-specific head maps those representations to labels or spans.
4. Fine-tuning updates the model for a labeled task, followed by evaluation on held-out data.

BERT was originally pretrained using masked language modeling and, in the original setup, next sentence prediction. A token can use left and right context in its encoder representation; this differs from causal next-token generation.

## Common terminology

| Term | Meaning |
|---|---|
| [CLS] | Special token often used as a sequence-level representation |
| [SEP] | Special token used to separate sequences or mark a boundary |
| WordPiece | Subword tokenization method used by many BERT tokenizers |
| Masked language modeling | Predicting selected masked tokens during pretraining |
| Fine-tuning | Updating pretrained weights for a downstream task |

## Practical notes

Use the tokenizer that belongs to the selected model checkpoint. Check truncation, padding, label mapping, class balance, and evaluation metrics. Do not assume a BERT model will be accurate for a domain or language without evaluating it on representative data.

## Next

Review the [Transformers module](../09_Transformers/README.md) and optional dependencies in [requirements-nlp.txt](../requirements-nlp.txt).
