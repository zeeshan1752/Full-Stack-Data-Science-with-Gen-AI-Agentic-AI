# 06. Neural Networks for NLP

Neural NLP models learn numerical representations from examples. Unlike a manually designed keyword rule, a trained model can learn patterns from labeled or unlabeled text. Training quality depends on data, model design, and evaluation.

## Learning objectives

- Explain why words or tokens must be represented numerically.
- Distinguish one-hot representations from learned embeddings.
- Describe the basic flow of a neural text classifier.
- Identify the roles of training, validation, loss, and optimization.

## Learning sequence

- [Neural Network Fundamentals](01_Neural_Network_Fundamentals/README.md)
- [Word Embeddings in Neural Networks](02_Word_Embeddings_in_Neural_Networks/README.md)
- [Neural Text Classification](03_Neural_Text_Classification/README.md)

## A simple classification pipeline

A sentiment classifier can take “The service was excellent”, map tokens to IDs or vectors, and predict a label such as positive or negative. The prediction is compared with the known training label using a loss function; an optimizer adjusts model parameters to reduce that loss.

1. Prepare labeled text and split it into training, validation, and test sets.
2. Build a vocabulary or select a tokenizer.
3. Convert tokens to numeric IDs or embeddings.
4. Pass representations through a neural network.
5. Train on the training set and monitor validation performance.
6. Evaluate on held-out test data.

## Important terms

| Term | Meaning |
|---|---|
| Embedding | A learned dense vector representing a token |
| Logits | Raw model scores before conversion to probabilities |
| Loss | A numerical measure of prediction error |
| Epoch | One pass through the training examples |
| Overfitting | The model fits training examples but generalizes poorly |
| Padding mask | Indicates which positions are padding rather than real tokens |

## Practical guidance

Start with a small reproducible dataset. Keep the test set separate from model selection, and compare against a baseline such as TF-IDF with logistic regression. A neural network is not automatically better for every dataset.

## Next

Continue to [Sequential Models](../07_Sequential_Models/README.md), then [Attention Mechanism](../08_Attention_Mechanism/README.md).
