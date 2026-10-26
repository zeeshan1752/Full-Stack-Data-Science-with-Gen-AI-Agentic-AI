# Natural Language Processing

This folder follows the 11-unit NLP sequence in the repository syllabus. The folders keep concept notes, library examples, trainer material, and projects in separate places.

## Learning status

Practice and saved outputs are present for text cleaning, tokenization, stop-word removal, stemming, lemmatization, Bag of Words, N-grams, TF-IDF, Word2Vec, POS tagging, NER, chunking, and WordCloud visualization. The Word2Vec examples use small teaching corpora; they demonstrate the API and do not produce general-purpose embeddings.

The preserved NLTK notebook has a saved N-gram error because one call omits n, and some non-English stop-word lookups fail when their NLTK data files are not installed. Notebook outputs are preserved as received. This reorganization did not execute scripts or notebooks.

The two GPT-2 chunking notebooks in 09_Transformers/07_GPT2_Chunking_and_HF_Demos/ are copies from the trainer archive. Their saved outputs are also preserved; they have not been rerun here. They demonstrate GPT-2 text continuation and token chunking, not a complete summarization or retrieval system.

## Course modules

1. [Text Preprocessing](01_Text_Preprocessing/README.md)
2. [Text Representation](02_Text_Representation/README.md)
3. [Linguistic Analysis](03_Linguistic_Analysis/README.md)
4. [NLP Applications](04_NLP_Applications/README.md)
5. [NLP Libraries and Tools](05_NLP_Libraries_and_Tools/README.md)
6. [Neural Networks for NLP](06_Neural_Networks_for_NLP/README.md)
7. [Sequential Models](07_Sequential_Models/README.md)
8. [Attention Mechanism](08_Attention_Mechanism/README.md)
9. [Transformers](09_Transformers/README.md)
10. [BERT](10_BERT/README.md)
11. [NLP Projects](11_NLP_Projects/README.md)

## Notes

- Existing source notebooks, scripts, and their outputs were preserved while folders were reorganized.
- Planned folders contain a short README so Git can track them and show their purpose.
- Extra material such as constituency parsing, clustering, text generation, WordClouds, and the rule-based chatbot remains available after the core syllabus topics.
- PCA material from the trainer archive is not part of this NLP folder.
