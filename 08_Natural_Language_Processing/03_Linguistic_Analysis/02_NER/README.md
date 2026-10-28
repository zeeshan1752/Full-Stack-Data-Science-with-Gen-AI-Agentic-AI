# Named Entity Recognition

Named Entity Recognition (NER) identifies and classifies spans that refer to entities such as people, organizations, locations, dates, and quantities. Results depend on the model, language, and context.

## Existing evidence

The preserved [NLTK practice notebook](../../01_Preprocessing/02_Tokenization/nltk_cross_topic_practice.ipynb) includes an NER section. Its existing saved work is preserved. The standalone example here has not been executed.

## Setup and run

Install NLTK with python -m pip install nltk. Follow the official [NLTK data guide](https://www.nltk.org/data.html) for any missing tokenizer, tagger, or named-entity resources. NLTK's chunker commonly expects POS-tagged tokens as input.

NER output is an automated prediction and may miss entities or assign an incorrect type. See [POS tagging](../01_POS_Tagging/README.md) and [NLTK notes](../../01_Preprocessing/02_Tokenization/nltk_notes.md).


## Examples

- [NLTK named entity recognition](ner_nltk.py)
- [spaCy named entity recognition](ner_spacy.py) (requires the `en_core_web_sm` model)
- [Compare NLTK and spaCy](comparison.ipynb)
- [Original NLTK notebook](ner_nltk.ipynb)

Both [ner_nltk.py](ner_nltk.py) and [ner_spacy.py](ner_spacy.py) expose `extract_entities(text)` and return `(entity_text, label)` pairs, so their outputs can be compared directly.
