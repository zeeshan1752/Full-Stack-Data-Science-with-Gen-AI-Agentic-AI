"""Fine-tune a compact pretrained BERT model on synthetic review labels."""

import csv
import random
from pathlib import Path

import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer


MODEL_NAME = "prajjwal1/bert-tiny"
DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "restaurant_reviews.tsv"
MAX_SAMPLES = 300
MAX_LENGTH = 64


def load_reviews():
    with DATA_FILE.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file, delimiter="\t"))
    random.Random(42).shuffle(rows)
    rows = rows[:MAX_SAMPLES]
    return [row["Review"] for row in rows], [int(row["Liked"]) for row in rows]


def main() -> None:
    torch.manual_seed(42)
    texts, labels = load_reviews()
    train_texts, test_texts, train_labels, test_labels = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    train_tokens = tokenizer(
        train_texts,
        padding="max_length",
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
    )
    test_tokens = tokenizer(
        test_texts,
        padding="max_length",
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt",
    )
    train_data = TensorDataset(
        train_tokens["input_ids"],
        train_tokens["attention_mask"],
        torch.tensor(train_labels, dtype=torch.long),
    )
    test_data = TensorDataset(
        test_tokens["input_ids"],
        test_tokens["attention_mask"],
        torch.tensor(test_labels, dtype=torch.long),
    )
    train_loader = DataLoader(train_data, batch_size=16, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=32)

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, num_labels=2
    )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)

    model.train()
    for batch in train_loader:
        input_ids, attention_mask, batch_labels = [
            item.to(device) for item in batch
        ]
        optimizer.zero_grad()
        result = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=batch_labels,
        )
        result.loss.backward()
        optimizer.step()
    print("Fine-tuning pass completed.")

    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for input_ids, attention_mask, batch_labels in test_loader:
            result = model(
                input_ids=input_ids.to(device),
                attention_mask=attention_mask.to(device),
            )
            predictions = result.logits.argmax(dim=1).cpu()
            correct += int((predictions == batch_labels).sum())
            total += len(batch_labels)
    print(f"Held-out accuracy: {correct / total:.3f}")


if __name__ == "__main__":
    main()
