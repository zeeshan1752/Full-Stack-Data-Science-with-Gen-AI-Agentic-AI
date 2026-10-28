"""Train a small embedding-based neural classifier on synthetic reviews."""

import csv
import random
import re
from pathlib import Path

import torch
from torch import nn


DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "restaurant_reviews.tsv"
PAD_TOKEN = "<pad>"
UNKNOWN_TOKEN = "<unk>"
MAX_LENGTH = 40


def read_reviews():
    with DATA_FILE.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file, delimiter="\t"))
    return [(row["Review"], int(row["Liked"])) for row in rows]


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def build_vocabulary(training_rows):
    vocabulary = {PAD_TOKEN: 0, UNKNOWN_TOKEN: 1}
    for text, _ in training_rows:
        for word in tokenize(text):
            if word not in vocabulary:
                vocabulary[word] = len(vocabulary)
    return vocabulary


def encode_text(text, vocabulary):
    token_ids = [
        vocabulary.get(word, vocabulary[UNKNOWN_TOKEN])
        for word in tokenize(text)
    ][:MAX_LENGTH]
    token_ids += [vocabulary[PAD_TOKEN]] * (MAX_LENGTH - len(token_ids))
    return token_ids


class ReviewClassifier(nn.Module):
    def __init__(self, vocabulary_size, embedding_size=24):
        super().__init__()
        self.embedding = nn.EmbeddingBag(
            vocabulary_size, embedding_size, mode="mean", padding_idx=0
        )
        self.output = nn.Linear(embedding_size, 1)

    def forward(self, token_ids):
        return self.output(self.embedding(token_ids)).squeeze(1)


def main() -> None:
    torch.manual_seed(42)
    rows = read_reviews()
    random.Random(42).shuffle(rows)
    split_at = int(len(rows) * 0.8)
    training_rows = rows[:split_at]
    test_rows = rows[split_at:]
    vocabulary = build_vocabulary(training_rows)

    x_train = torch.tensor(
        [encode_text(text, vocabulary) for text, _ in training_rows],
        dtype=torch.long,
    )
    y_train = torch.tensor(
        [label for _, label in training_rows], dtype=torch.float32
    )
    x_test = torch.tensor(
        [encode_text(text, vocabulary) for text, _ in test_rows],
        dtype=torch.long,
    )
    y_test = torch.tensor(
        [label for _, label in test_rows], dtype=torch.float32
    )

    model = ReviewClassifier(len(vocabulary))
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_function = nn.BCEWithLogitsLoss()

    for epoch in range(8):
        model.train()
        optimizer.zero_grad()
        logits = model(x_train)
        loss = loss_function(logits, y_train)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch + 1}: loss={loss.item():.4f}")

    model.eval()
    with torch.no_grad():
        predictions = (torch.sigmoid(model(x_test)) >= 0.5).float()
        accuracy = (predictions == y_test).float().mean().item()
    print(f"Held-out accuracy: {accuracy:.3f}")


if __name__ == "__main__":
    main()
