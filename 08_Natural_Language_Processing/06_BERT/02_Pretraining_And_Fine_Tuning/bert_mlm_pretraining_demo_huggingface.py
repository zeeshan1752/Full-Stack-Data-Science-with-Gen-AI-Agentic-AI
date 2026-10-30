"""Demonstrate one masked-language-model training step on shared sample text."""

from pathlib import Path

import torch
from transformers import AutoModelForMaskedLM, AutoTokenizer


MODEL_NAME = "prajjwal1/bert-tiny"
DATA_FILE = Path(__file__).resolve().parents[2] / "01_Preprocessing" / "sample_texts.txt"


def main() -> None:
    torch.manual_seed(42)
    texts = [
        line.strip()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForMaskedLM.from_pretrained(MODEL_NAME)
    encoded = tokenizer(
        texts, return_tensors="pt", padding=True, truncation=True, max_length=64
    )
    input_ids = encoded["input_ids"]
    attention_mask = encoded["attention_mask"]
    special_tokens = torch.tensor(
        [
            tokenizer.get_special_tokens_mask(row, already_has_special_tokens=True)
            for row in input_ids.tolist()
        ],
        dtype=torch.bool,
    )
    selected = (
        (torch.rand(input_ids.shape) < 0.15)
        & attention_mask.bool()
        & ~special_tokens
    )
    if not selected.any():
        selected[0, 1] = True

    labels = input_ids.clone()
    labels[~selected] = -100
    masked_ids = input_ids.clone()
    masked_ids[selected] = tokenizer.mask_token_id

    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
    model.train()
    optimizer.zero_grad()
    result = model(
        input_ids=masked_ids,
        attention_mask=attention_mask,
        labels=labels,
    )
    result.loss.backward()
    optimizer.step()
    print(f"One masked-token training step completed; loss={result.loss.item():.4f}")


if __name__ == "__main__":
    main()
