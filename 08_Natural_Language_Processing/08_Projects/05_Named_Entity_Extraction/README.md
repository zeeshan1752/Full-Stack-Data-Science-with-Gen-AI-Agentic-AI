# Named Entity Extraction

Status: The code has not been run locally.

## Install

    python -m pip install spacy
    python -m spacy download en_core_web_sm

## Run

    python 08_Natural_Language_Processing/08_Projects/05_Named_Entity_Extraction/named_entity_extraction_spacy.py

The script uses the shared sample text file and prints each entity with its predicted label.

## What you will learn

Named entity recognition finds spans that may refer to people, organizations, places, dates, and other named things. The example exposes extract_entities(text), returning a list of (entity text, label) pairs.

## Common mistakes

- Entity labels depend on the language model and may be incorrect or incomplete.
- The English model is not suitable for text in every language.
