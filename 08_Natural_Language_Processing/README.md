# Natural Language Processing

This folder organizes the NLP materials in seven numbered modules. The preserved notebooks and scripts provide evidence of practice, but they do not prove what an instructor explicitly taught or whether every topic was completed in class.

## Learning status

### Practice visible in the original files

- **Text preprocessing:** tokenization, stop-word removal, Porter/Lancaster/Snowball stemming, and WordNet lemmatization appear in the original scripts and NLTK notebook. Basic lowercasing and text cleaning also appear inside the original Bag of Words script.
- **Text representation:** the original materials use Bag of Words and TF-IDF vectorizers and include an N-gram section.
- **Linguistic analysis:** the original NLTK notebook contains POS-tagging and named-entity-recognition examples.
- **Additional practice:** the NLTK notebook includes multilingual stop-word lookups and a WordCloud example.
- **NLTK:** the original cross-topic notebook contains practical examples of several of the above techniques.

Saved notebook outputs show some incomplete attempts: an N-gram call omits its required size argument; Hindi and Kannada stop-word lookups report missing data files; and the Gensim Word2Vec attempt reports that Gensim was not installed. These saved outputs are preserved as part of the original work. They are not presented as successful runs.

### Attempted, with completion not established

- **Word2Vec with Gensim:** the original practice notebook contains an attempt, but its saved output records a missing-package error. See [Word2Vec](02_Text_Representation/06_Word2Vec/README.md).

### New study companions

Focused explanations, scripts, and notebooks have been added alongside the preserved work for the evidenced topics. Newly added notebooks have not been executed here and therefore have no claimed output. A manual Bag of Words exercise is new supplemental practice; no manual BoW exercise was found in the original files.

- [Text cleaning](01_Text_Preprocessing/02_Text_Cleaning/README.md)
- [Tokenization](01_Text_Preprocessing/04_Tokenization/README.md)
- [Stop-word removal](01_Text_Preprocessing/05_Stop_Word_Removal/README.md)
- [Stemming](01_Text_Preprocessing/06_Stemming/README.md)
- [Lemmatization](01_Text_Preprocessing/07_Lemmatization/README.md)
- [Bag of Words](02_Text_Representation/01_Bag_of_Words/README.md)
- [N-Grams](02_Text_Representation/02_N_Grams/README.md)
- [TF-IDF](02_Text_Representation/03_TF_IDF/README.md)
- [Word2Vec](02_Text_Representation/06_Word2Vec/README.md)
- [POS tagging](03_Linguistic_Analysis/01_POS_Tagging/README.md)
- [Named Entity Recognition](03_Linguistic_Analysis/02_Named_Entity_Recognition/README.md)
- [WordCloud visualization](04_NLP_Applications/08_Text_Visualization/README.md)

## The seven modules

### 01. Text Preprocessing

[Open the module](01_Text_Preprocessing/)

Prepare text for a specific task. Existing work includes tokenization, stop-word removal, stemming, lemmatization, and basic cleaning. Broader normalization, regular-expression practice, and reusable pipelines are planned.

- [Module guide](01_Text_Preprocessing/README.md)
- [Tokenization](01_Text_Preprocessing/04_Tokenization/)
- [Stemming](01_Text_Preprocessing/06_Stemming/)
- [Lemmatization](01_Text_Preprocessing/07_Lemmatization/)

### 02. Text Representation

[Open the module](02_Text_Representation/)

Convert documents into numerical features. Existing material demonstrates BoW and TF-IDF and contains N-gram practice. Word2Vec was attempted, with a saved missing-dependency error.

- [Bag of Words](02_Text_Representation/01_Bag_of_Words/README.md)
- [N-Grams](02_Text_Representation/02_N_Grams/README.md)
- [TF-IDF](02_Text_Representation/03_TF_IDF/README.md)
- [Word2Vec](02_Text_Representation/06_Word2Vec/README.md)

Planned: GloVe, sentence and document embeddings, and deeper vectorization comparisons.

### 03. Linguistic Analysis

[Open the module](03_Linguistic_Analysis/)

Analyze grammatical roles and entity spans. POS tagging and NER appear in the original NLTK notebook; dependency parsing, constituency parsing, chunking, and broader linguistic features are planned.

- [POS tagging](03_Linguistic_Analysis/01_POS_Tagging/README.md)
- [Named Entity Recognition](03_Linguistic_Analysis/02_Named_Entity_Recognition/README.md)

### 04. NLP Applications

[Open the module](04_NLP_Applications/)

Apply NLP methods to tasks such as classification, sentiment analysis, topic modeling, similarity, clustering, summarization, and generation. These application topics are planned; the WordCloud visualization is present in the original notebook.

- [Text visualization and WordCloud](04_NLP_Applications/08_Text_Visualization/README.md)

### 05. NLP Libraries

[Open the module](05_NLP_Libraries/)

Library-specific implementations are kept apart from concept-focused notes.

- [NLTK](05_NLP_Libraries/01_NLTK/README.md): original multi-topic practice notebook, moved here to keep library-focused work together.
- [spaCy](05_NLP_Libraries/02_spaCy/): planned.
- [scikit-learn](05_NLP_Libraries/03_Scikit_Learn/README.md): vectorization is present in the original BoW and practice files.
- [Gensim](05_NLP_Libraries/04_Gensim/README.md): Word2Vec was attempted; the saved run is blocked by the missing package.

### 06. Advanced NLP

[Open the module](06_Advanced_NLP/)

Neural networks, RNNs, LSTMs, attention, transformers, BERT, transfer learning, and large language model fundamentals are planned for future learning.

### 07. NLP Projects

[Open the module](07_NLP_Projects/)

Project folders are planned starting points for applied work. No completed project is claimed based on the audited files.

## Notes on files and checkpoints

Original scripts, notebooks, saved outputs, and checkpoint files were preserved. Checkpoints are notebook autosaves and may be older than the active notebook. The former root Tokens notebook is kept under NLTK because it combines several NLTK-focused examples; the original notebook content and its saved outputs were not edited.

For installation help, use the official guidance for [NLTK](https://www.nltk.org/install), [scikit-learn](https://scikit-learn.org/stable/install.html), [Gensim](https://radimrehurek.com/gensim/intro.html), and [WordCloud](https://pypi.org/project/wordcloud/).
