"""Run sentiment inference with a pretrained DistilBERT checkpoint."""

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
TEXT = "The service was kind and the meal was excellent."


def predict_sentiment(text: str):
    """Return the model's predicted label and its softmax score."""
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    model.eval()
    encoded = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = model(**encoded).logits
        probabilities = torch.softmax(logits, dim=1)[0]
    label_id = int(probabilities.argmax())
    label = model.config.id2label[label_id]
    return label, float(probabilities[label_id])


def main() -> None:
    label, score = predict_sentiment(TEXT)
    print(f"Prediction: {label} (model score {score:.3f})")


if __name__ == "__main__":
    main()
