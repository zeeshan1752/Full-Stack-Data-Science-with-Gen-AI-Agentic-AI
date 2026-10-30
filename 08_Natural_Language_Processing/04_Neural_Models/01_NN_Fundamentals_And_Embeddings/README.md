# Neural Network Fundamentals and Embeddings

Status: The code has not been run locally.

## Install

    python -m pip install torch

## Example

- [Look up trainable word vectors with PyTorch](embeddings_pytorch.py)

## What you will learn

An embedding layer maps integer token IDs to learned numeric vectors. The vector values start from random initialization and can change during training.

## Run

    python 08_Natural_Language_Processing/04_Neural_Models/01_NN_Fundamentals_And_Embeddings/embeddings_pytorch.py

## Common mistakes

- Token IDs are indexes into a vocabulary; they are not word meanings by themselves.
- A random embedding is only a demonstration until a learning task updates its values.
