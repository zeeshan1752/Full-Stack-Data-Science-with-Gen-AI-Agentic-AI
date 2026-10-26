# Named Entity Recognition

Named Entity Recognition (NER) identifies and classifies spans that refer to entities such as people, organizations, locations, dates, and quantities. Results depend on the model, language, and context.

## Existing evidence

The preserved [NLTK practice notebook](../../05_NLP_Libraries_and_Tools/01_NLTK/Tokens.ipynb) includes an NER section. Its existing saved work is preserved. The standalone example here has not been executed.

## Setup and run

Install NLTK with python -m pip install nltk. Follow the official [NLTK data guide](https://www.nltk.org/data.html) for any missing tokenizer, tagger, or named-entity resources. NLTK's chunker commonly expects POS-tagged tokens as input.

NER output is an automated prediction and may miss entities or assign an incorrect type. See [POS tagging](../01_POS_Tagging/README.md) and [NLTK notes](../../05_NLP_Libraries_and_Tools/01_NLTK/README.md).
