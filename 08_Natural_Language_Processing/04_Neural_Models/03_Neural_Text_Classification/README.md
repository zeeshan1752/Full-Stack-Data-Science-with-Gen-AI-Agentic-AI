# Neural Text Classification

Status: The code has not been run locally.

## Install

    python -m pip install torch

## Example

- [Train an embedding-based review classifier](neural_text_classification_pytorch.py)

The example reads the shared synthetic reviews from 08_Natural_Language_Processing/04_Neural_Models/restaurant_reviews.tsv.

## Run

    python 08_Natural_Language_Processing/04_Neural_Models/03_Neural_Text_Classification/neural_text_classification_pytorch.py

## What you will learn

The model maps word IDs to vectors, averages the vectors in a review, and predicts one of two labels. It prints the accuracy calculated on a held-out split.

## Common mistakes

- This small model is a learning example and its measured score applies only to the held-out synthetic examples.
- Words not present in the training vocabulary use the unknown-word ID.
