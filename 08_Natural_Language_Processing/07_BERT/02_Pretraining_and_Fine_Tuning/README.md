# Pretraining and Fine-Tuning

Status: The code has not been run locally.

## Install

    python -m pip install torch transformers

The first run downloads the compact BERT checkpoint from Hugging Face. The checkpoint is cached locally and is not committed to this repository.

## Examples

- [Take one masked-language-model training step](bert_mlm_pretraining_demo_huggingface.py)
- [Fine-tune BERT on shared synthetic reviews](bert_finetuning_huggingface.py)

## What you will learn

The first script demonstrates one toy masked-language-model update using shared sample sentences. It is an illustration, not full-scale pretraining. The second script fine-tunes an existing BERT checkpoint for review sentiment.

## Run

    python 08_Natural_Language_Processing/07_BERT/02_Pretraining_and_Fine_Tuning/bert_mlm_pretraining_demo_huggingface.py
    python 08_Natural_Language_Processing/07_BERT/02_Pretraining_and_Fine_Tuning/bert_finetuning_huggingface.py

## Common mistakes

- Pretraining a useful language model requires far more text and compute than the tiny demonstration.
- Fine-tuning on synthetic examples does not guarantee performance on real reviews.
- Keep pretrained model weights out of the repository; the library downloads them when needed.
