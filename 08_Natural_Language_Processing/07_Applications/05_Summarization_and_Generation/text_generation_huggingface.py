"""Generate a short continuation with a pretrained causal language model."""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_NAME = "distilbert/distilgpt2"
PROMPT = "A useful way to study language is"


def generate_text(prompt: str, max_new_tokens=50) -> str:
    """Return only the generated continuation after the prompt."""
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id,
        )
    continuation = output_ids[0, inputs["input_ids"].shape[1] :]
    return tokenizer.decode(continuation, skip_special_tokens=True).strip()


def main() -> None:
    print("Prompt:", PROMPT)
    print("Continuation:", generate_text(PROMPT))


if __name__ == "__main__":
    main()
