"""A small local Streamlit interface for pretrained text summarization."""

import streamlit as st
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


MODEL_NAME = "sshleifer/distilbart-cnn-12-6"


@st.cache_resource
def load_summarizer():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    return tokenizer, model, device


def summarize_text(text: str) -> str:
    tokenizer, model, device = load_summarizer()
    inputs = tokenizer(
        text, return_tensors="pt", truncation=True, max_length=1024
    ).to(device)
    with torch.no_grad():
        output_ids = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


def main() -> None:
    st.title("Text Summarizer")
    st.write("Paste a passage to create a short summary with a local model.")
    text = st.text_area("Text to summarize", height=220)
    if st.button("Summarize"):
        if not text.strip():
            st.warning("Enter some text first.")
        else:
            with st.spinner("Loading the model and creating a summary..."):
                st.subheader("Summary")
                st.write(summarize_text(text))


if __name__ == "__main__":
    main()
