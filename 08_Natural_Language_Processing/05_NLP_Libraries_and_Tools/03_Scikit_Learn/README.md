# scikit-learn for Text

This guide links the core text-representation notes to scikit-learn's APIs. Detailed theory and introductory examples stay in their canonical topic folders.

## Start with the concepts

- [Bag of Words](../../02_Text_Representation/01_Bag_of_Words/README.md)
- [TF-IDF](../../02_Text_Representation/03_TF_IDF/README.md)
- [Text classification](../../04_NLP_Applications/01_Text_Classification/README.md)
- [Evaluation metrics](../../04_NLP_Applications/09_Evaluation_Metrics/README.md)

## Existing practice

- [Bag of Words implementation](../../02_Text_Representation/01_Bag_of_Words/Bag_of_words.py)
- [Manual Bag of Words exercise](../../02_Text_Representation/01_Bag_of_Words/Manual_Bag_of_Words.ipynb)
- [TF-IDF implementation](../../02_Text_Representation/03_TF_IDF/TF_IDF.py)

Install the library with:

```bash
python -m pip install -U scikit-learn
```

The former CountVectorizer, TfidfVectorizer, classification, and evaluation subfolders contained only placeholder READMEs. They have been removed; add a separate subfolder only when it contains a distinct practical lesson or runnable implementation.
