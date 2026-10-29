# BERT Applications

Status: The code has not been run locally.

## Install

    python -m pip install torch transformers

The first run downloads the model checkpoint from Hugging Face.

## Example

- [Classify sentiment with a fine-tuned DistilBERT model](bert_sentiment_huggingface.py)

## What you will learn

DistilBERT is a smaller model in the BERT family. This example uses a checkpoint already fine-tuned for positive and negative sentiment, then predicts a label for new text.

## Run

    python 08_Natural_Language_Processing/06_BERT/03_BERT_Applications/bert_sentiment_huggingface.py

## Common mistakes

- The model is intended for English sentiment classification; other languages and tasks need a suitable checkpoint.
- A model prediction is not a guarantee that the review is truly positive or negative.
