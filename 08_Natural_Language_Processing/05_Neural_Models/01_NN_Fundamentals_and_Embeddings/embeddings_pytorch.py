"""Create and inspect a trainable embedding layer in PyTorch."""

import torch
from torch import nn


def main() -> None:
    torch.manual_seed(42)
    embedding = nn.Embedding(num_embeddings=8, embedding_dim=4)
    token_ids = torch.tensor([[1, 2, 3], [4, 0, 1]])
    vectors = embedding(token_ids)
    print("Token ID shape:", tuple(token_ids.shape))
    print("Embedding output shape:", tuple(vectors.shape))
    print("Vector for the first sentence:")
    print(vectors[0])


if __name__ == "__main__":
    main()
