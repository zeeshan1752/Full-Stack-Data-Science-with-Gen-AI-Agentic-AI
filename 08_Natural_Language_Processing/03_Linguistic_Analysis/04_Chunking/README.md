# Chunking and Chinking

Chunking is a shallow syntactic analysis step. It groups part-of-speech-tagged tokens into phrases, such as noun phrases (NP), verb phrases (VP), and prepositional phrases (PP). Chinking removes selected tags from a chunk.

## Trainer lesson

The trainer's NLTK example has been adapted into [Chunking and Chinking](chunking_nltk.ipynb). It includes a phrase grammar and a separate chinking rule. The notebook does not run or download NLTK data automatically.

## Requirements

Install NLTK with:

~~~bash
python -m pip install nltk
~~~

If the tokenizer or tagger reports a missing NLTK resource, follow the [NLTK data guide](https://www.nltk.org/data.html) and install the named resource.

## Keep the two meanings of chunking distinct

- **Syntactic chunking** groups tokens into shallow grammatical phrases.
- **Long-text chunking** divides text into pieces that fit a model's token limit. The trainer's GPT-2 demonstration for this is in [the Transformer supplement](../../06_Attention_and_Transformers/03_GPT2_and_HF_Demos/README.md).

Rule-based chunks are only as accurate as the POS tags and grammar rules. For full sentence structure, study constituency parsing and dependency parsing.

