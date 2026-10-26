# GPT-2 Chunking and Hugging Face Demos

**Status: Trainer examples are present; saved outputs have not been rerun here.**

These two notebooks were copied from the supplied trainer archive:

- LLM___CHUNK___GPT2_.ipynb
- LLM___CHUNK___GPT2_HF.ipynb

They show GPT-2 tokenization, text continuation, and a simple token-slicing example. The saved outputs repeat much of the prompt, and the notebooks do not implement summarization or retrieval. In the chunking example, max_length controls the total generated sequence length; a full 512-token input chunk leaves no room for new tokens.

For Transformer architecture background, see [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
