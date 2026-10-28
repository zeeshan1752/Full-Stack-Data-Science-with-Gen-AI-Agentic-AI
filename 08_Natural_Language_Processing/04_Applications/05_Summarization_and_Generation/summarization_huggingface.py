"""Summarize a sample passage with a pretrained encoder-decoder model."""

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
TEXT = (
    "Natural language processing gives computers tools for working with human "
    "language. A typical workflow may clean text, split it into tokens, turn "
    "those tokens into numeric features, and then train a model for a task. "
    "Different tasks include classification, translation, question answering, "
    "and summarization. The quality of a result depends on the training data, "
    "the model, and how the result is evaluated."
)


def summarize_text(text: str, max_new_tokens=80) -> str:
    """Return a generated summary for one passage."""
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    inputs = tokenizer(
        text, return_tensors="pt", truncation=True, max_length=1024
    ).to(device)
    with torch.no_grad():
        output_ids = model.generate(**inputs, max_new_tokens=max_new_tokens)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


def main() -> None:
    print(summarize_text(TEXT))


if __name__ == "__main__":
    main()
