# Summarization and Text Generation

Status: The code has not been run locally.

## Install

    python -m pip install torch transformers

The first run downloads the selected pretrained model weights from Hugging Face. The weights are cached on your computer and are not included here.

## Examples

- [Summarize an input passage](summarization_huggingface.py)
- [Continue a prompt with DistilGPT2](text_generation_huggingface.py)

## Run

    python 08_Natural_Language_Processing/04_Applications/05_Summarization_and_Generation/summarization_huggingface.py
    python 08_Natural_Language_Processing/04_Applications/05_Summarization_and_Generation/text_generation_huggingface.py

## What you will learn

Summarization produces a shorter version of an input. Text generation continues from a prompt. Both examples use pretrained models and may produce inaccurate or biased text.

## Common mistakes

- Model files can be large and the first run needs an internet connection.
- Generated text is model output, not a verified source. Check facts before relying on it.
