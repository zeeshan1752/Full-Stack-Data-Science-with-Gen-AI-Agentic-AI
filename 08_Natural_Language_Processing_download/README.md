# Natural Language Processing Syllabus

The current, reorganized course lives in [08_Natural_Language_Processing](../08_Natural_Language_Processing/README.md). That README is the progress checklist; this file is the high-level syllabus. The `08_Natural_Language_Processing_download` folder is retained as trainer-source material for reference.

## Learning path

1. [Preprocessing](../08_Natural_Language_Processing/01_Preprocessing/README.md) — cleaning, normalization, tokenization, stopwords, stemming, lemmatization, regular expressions, and pipelines.
2. [Text Representation](../08_Natural_Language_Processing/02_Text_Representation/README.md) — Bag of Words, N-grams, TF-IDF, and word embeddings.
3. [Linguistic Analysis](../08_Natural_Language_Processing/03_Linguistic_Analysis/README.md) — POS tagging, named entity recognition, parsing, and chunking.
4. [Applications](../08_Natural_Language_Processing/04_Applications/README.md) — classification, sentiment, similarity and clustering, topic modeling, summarization and generation, evaluation, visualization, and speech.
5. [Neural Models](../08_Natural_Language_Processing/05_Neural_Models/README.md) — neural-network fundamentals, embeddings, RNNs, LSTMs, GRUs, and neural text classification.
6. [Attention and Transformers](../08_Natural_Language_Processing/06_Attention_and_Transformers/README.md) — Q/K/V, self- and cross-attention, multi-head attention, Transformer architecture, and GPT-2/Hugging Face demos.
7. [BERT](../08_Natural_Language_Processing/07_BERT/README.md) — architecture and tokenization, pretraining and fine-tuning, and applications.
8. [Projects](../08_Natural_Language_Processing/08_Projects/README.md) — spam, sentiment, news classification, summarization, entity extraction, and a rule-based chatbot.

## Shared data

- [Sample texts](../08_Natural_Language_Processing/data/sample_texts.txt)
- [Synthetic restaurant reviews](../08_Natural_Language_Processing/data/restaurant_reviews.tsv) — 1,000 labeled examples for sentiment-analysis practice.
- [Data notes](../08_Natural_Language_Processing/data/README.md)

## Course conventions

- Keep library implementations together inside each topic folder.
- Use lowercase snake_case filenames and add the library name as a suffix when applicable.
- Name library-comparison notebooks `comparison.ipynb`; use the shared sample text and compare speed, accuracy, and ease of use.
- Keep shared datasets under `data/`.
- Use the checklist in the active course README to track completed topics; empty and notes-only topics stay unchecked.

## Trainer archive

This folder preserves the original trainer material and its older 11-unit organization as supplemental reference material; the eight sections linked above are the current course structure.
