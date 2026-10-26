# Natural Language Processing

This folder follows the 11-unit NLP sequence in the repository syllabus. Each module separates core concepts from library demonstrations, trainer material, and projects.

## Learning path

1. **Text Preprocessing** — clean text, tokenize it, normalize word forms, and prepare consistent input.
2. **Text Representation** — convert words and documents into numerical features using Bag of Words, N-grams, TF-IDF, and embeddings.
3. **Linguistic Analysis** — explore parts of speech, named entities, and phrase structure.
4. **NLP Applications** — connect the foundations to common text-processing tasks.
5. **NLP Libraries and Tools** — practise with NLTK, scikit-learn, and other Python tools.
6. **Neural Networks for NLP** — learn embeddings and neural text classification.
7. **Sequential Models** — understand RNNs, LSTMs, and GRUs.
8. **Attention Mechanism** — learn queries, keys, values, and attention weights.
9. **Transformers** — study encoder/decoder blocks, positional information, masking, and modern pretrained models.
10. **BERT** — understand bidirectional pretraining and downstream fine-tuning.
11. **NLP Projects** — combine concepts in small, clearly scoped applications.

## Current material and limitations

Practice files cover text cleaning, tokenization, stop words, stemming, lemmatization, Bag of Words, N-grams, TF-IDF, Word2Vec, POS tagging, NER, chunking, and WordCloud visualization. Small Word2Vec corpora demonstrate the API only; they are not general-purpose pretrained embeddings.

The NLTK practical notebook still has a known saved N-gram error where a required argument is missing. Optional language stop-word resources may also be unavailable in a given NLTK installation; the notebook change could not be committed in this batch. NLTK data packages are separate from the Python package; see the [NLTK data guide](https://www.nltk.org/data.html). Some tagging and NER examples also need model data, depending on the installed NLTK version.

The two GPT-2 notebooks under [GPT-2 Chunking and Hugging Face Demos](09_Transformers/07_GPT2_Chunking_and_HF_Demos/README.md) are preserved trainer material. They demonstrate text continuation and token chunking, not a complete summarization or retrieval system. Colab-specific cells may need adaptation for a local machine. Notebooks and scripts have not all been executed end-to-end, so saved outputs should not be treated as a passing test suite.

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

## Environment setup

Install the NLP-specific packages from the repository root with `python -m pip install -r 08_Natural_Language_Processing/requirements-nlp.txt`. The Hugging Face and PyTorch dependencies are optional and are listed as comments in that file. NLTK may also require separate corpus/model downloads; see the [NLTK setup notes](05_NLP_Libraries_and_Tools/01_NLTK/README.md).

## Organization notes

- The 11 modules above remain the core syllabus and keep their approved order.
- Supplementary material such as constituency parsing, clustering, text generation, WordClouds, and the rule-based chatbot remains available outside the core sequence.
- Trainer notebooks and existing learning material are retained rather than silently removed.
- PCA material from the trainer archive is not part of this NLP folder.
