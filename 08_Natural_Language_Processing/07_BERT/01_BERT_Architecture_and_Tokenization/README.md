# BERT Architecture and Tokenization

Status: The code has not been run locally.

## Install

    python -m pip install torch transformers

The first run downloads the compact pretrained checkpoint from Hugging Face.

## Example

- [Tokenize text and inspect BERT output](bert_tokenization_huggingface.py)

## What you will learn

The tokenizer converts text to token IDs and an attention mask. BERT then returns a contextual vector for each input position.

## Run

    python 08_Natural_Language_Processing/07_BERT/01_BERT_Architecture_and_Tokenization/bert_tokenization_huggingface.py

## Common mistakes

- A token can be only part of a word because BERT uses subword tokenization.
- The hidden-state numbers are learned representations, not human-readable labels.
