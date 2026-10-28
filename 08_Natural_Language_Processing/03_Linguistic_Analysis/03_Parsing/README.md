# Parsing

Status: The code has not been run locally.

## Install

    python -m pip install nltk spacy
    python -m spacy download en_core_web_sm

## Examples

- [Build a small constituency tree with NLTK](constituency_parser_nltk.py)
- [Read dependency relations with spaCy](dependency_parser_spacy.py)

## What you will learn

Constituency parsing groups words into phrase structures. Dependency parsing connects each word to a head word and labels the relationship. These are different parse views, so the examples demonstrate each view separately.

## Run

Run either script from the repository root:

    python 08_Natural_Language_Processing/03_Linguistic_Analysis/03_Parsing/constituency_parser_nltk.py
    python 08_Natural_Language_Processing/03_Linguistic_Analysis/03_Parsing/dependency_parser_spacy.py

## Common mistakes

- The NLTK grammar is deliberately small. A sentence outside its grammar may have no parse.
- spaCy's dependency labels are model predictions. Install the English model before running the spaCy example.
