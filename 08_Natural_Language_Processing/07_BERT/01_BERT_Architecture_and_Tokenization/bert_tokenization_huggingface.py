"""Inspect subword tokens and contextual output vectors from a small BERT."""

import torch
from transformers import AutoModel, AutoTokenizer


MODEL_NAME = "prajjwal1/bert-tiny"
TEXT = "Transformers represent words in context."


def main() -> None:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME)
    model.eval()
    encoded = tokenizer(TEXT, return_tensors="pt")
    with torch.no_grad():
        output = model(**encoded)
    print("Tokens:", tokenizer.convert_ids_to_tokens(encoded["input_ids"][0]))
    print("Input IDs:", encoded["input_ids"][0].tolist())
    print("Attention mask:", encoded["attention_mask"][0].tolist())
    print("Contextual output shape:", tuple(output.last_hidden_state.shape))


if __name__ == "__main__":
    main()
