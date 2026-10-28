# RNN, LSTM, and GRU

Status: The code has not been run locally.

## Install

    python -m pip install torch

## Example

- [Compare the output shapes of recurrent layers](sequence_models_pytorch.py)

## What you will learn

RNN, LSTM, and GRU layers process an ordered sequence. This example sends the same small batch of numeric sequences through each layer and prints the output and hidden-state shapes.

## Run

    python 08_Natural_Language_Processing/05_Neural_Models/02_RNN_LSTM_GRU/sequence_models_pytorch.py

## Common mistakes

- The example uses random numbers to show tensor shapes, not meaningful language features.
- Check whether the batch dimension comes first when changing a layer's settings.
