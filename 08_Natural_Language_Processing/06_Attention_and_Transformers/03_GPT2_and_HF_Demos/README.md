# GPT-2 Chunking and Hugging Face Demos

**Status: Trainer examples are present; cached outputs were cleared before publication, and the notebooks have not been rerun.**

These two notebooks were copied from the supplied trainer archive:

- gpt2_chunking.ipynb
- gpt2_huggingface_chunking.ipynb

They show GPT-2 tokenization, text continuation, and a simple token-slicing example. They do not implement summarization or retrieval. In the chunking example, max_length controls the total generated sequence length; a full 512-token input chunk leaves no room for new tokens. Run the notebooks locally to generate fresh outputs.

For Transformer architecture background, see [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
