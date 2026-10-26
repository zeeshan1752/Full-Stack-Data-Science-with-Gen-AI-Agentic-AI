# NLTK

NLTK is a Python toolkit for teaching and experimenting with natural-language processing. It provides tokenizers, stemming and lemmatization tools, corpus access, tagging, and chunking utilities.

## Existing practice

- [Tokens.ipynb](Tokens.ipynb) is the preserved cross-topic practical notebook. It includes tokenization, n-grams, stop words (including multilingual lookups), stemming, lemmatization, POS tagging, NER, and a WordCloud example.
- Its saved outputs include an n-gram call error from a missing argument and missing Hindi/Kannada stop-word resources. Those saved outputs remain unchanged as a record of the original notebook.
- The notebook checkpoint is kept separately under [.ipynb_checkpoints](.ipynb_checkpoints/).

The notebook's coverage shows practice in these areas; it does not by itself establish that every item was fully completed in class. Focused conceptual notes live in [text preprocessing](../../01_Text_Preprocessing/README.md), [n-grams](../../02_Text_Representation/02_N_Grams/README.md), [POS tagging](../../03_Linguistic_Analysis/01_POS_Tagging/README.md), and [NER](../../03_Linguistic_Analysis/02_Named_Entity_Recognition/README.md).

## Setup

Install NLTK with python -m pip install nltk. Download NLTK data only when required; see the official [NLTK data guide](https://www.nltk.org/data.html).
