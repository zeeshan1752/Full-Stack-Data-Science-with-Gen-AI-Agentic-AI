# Natural Language Processing Syllabus and Checklist

This is the main NLP syllabus and progress checklist. Topic notes are consolidated into each folder’s `README.md` for direct browsing on GitHub. The checklist shows which topics already contain runnable code and which ones still need examples.

[x] means runnable example or project code is present; notes-only topics remain unchecked.

## Learning path

1. [Preprocessing](01_Preprocessing/README.md) — cleaning, normalization, tokenization, stopwords, stemming, lemmatization, regular expressions, and pipelines.
2. [Text Representation](03_Text_Representation/README.md) — Bag of Words, N-grams, TF-IDF, and word embeddings.
3. [Linguistic Analysis](02_Linguistic_Analysis/README.md) — POS tagging, named entity recognition, parsing, and chunking.
4. [Applications](07_Applications/README.md) — classification, sentiment, similarity and clustering, topic modeling, summarization and generation, evaluation, visualization, and speech.
5. [Neural Models](04_Neural_Models/README.md) — neural-network fundamentals, embeddings, RNNs, LSTMs, GRUs, and neural text classification.
6. [Attention and Transformers](05_Attention_And_Transformers/README.md) — Q/K/V, self- and cross-attention, multi-head attention, Transformer architecture, and GPT-2/Hugging Face demos.
7. [BERT](06_BERT/README.md) — architecture and tokenization, pretraining and fine-tuning, and applications.
8. [Projects](08_Projects/README.md) — spam, sentiment, news classification, summarization, entity extraction, and a rule-based chatbot.

## Topic checklist

## 01_Preprocessing
- [x] [01_Basics_And_Cleaning](01_Preprocessing/01_Basics_And_Cleaning/)
- [x] [02_Tokenization](01_Preprocessing/02_Tokenization/)
- [x] [03_Stopwords_Stemming_Lemmatization](01_Preprocessing/03_Stopwords_Stemming_Lemmatization/)
- [x] [04_Regex_And_Pipelines](01_Preprocessing/04_Regex_And_Pipelines/)

## 03_Text_Representation
- [x] [01_Bag_Of_Words_And_NGrams](03_Text_Representation/01_Bag_Of_Words_And_NGrams/)
- [x] [02_TF_IDF](03_Text_Representation/02_TF_IDF/)
- [x] [03_Word_Embeddings](03_Text_Representation/03_Word_Embeddings/)

## 02_Linguistic_Analysis
- [x] [01_POS_Tagging](02_Linguistic_Analysis/01_POS_Tagging/)
- [x] [02_NER](02_Linguistic_Analysis/02_NER/)
- [x] [03_Parsing](02_Linguistic_Analysis/03_Parsing/)
- [x] [04_Chunking](02_Linguistic_Analysis/04_Chunking/)

## 07_Applications
- [ ] [01_Text_Classification](07_Applications/01_Text_Classification/)
- [x] [02_Sentiment_Analysis](07_Applications/02_Sentiment_Analysis/)
- [x] [03_Similarity_And_Clustering](07_Applications/03_Similarity_And_Clustering/)
- [x] [04_Topic_Modeling](07_Applications/04_Topic_Modeling/)
- [x] [05_Summarization_And_Generation](07_Applications/05_Summarization_And_Generation/)
- [x] [06_Evaluation_Metrics](07_Applications/06_Evaluation_Metrics/)
- [x] [07_Visualization_And_Speech](07_Applications/07_Visualization_And_Speech/)

## 04_Neural_Models
- [x] [01_NN_Fundamentals_And_Embeddings](04_Neural_Models/01_NN_Fundamentals_And_Embeddings/)
- [x] [02_RNN_LSTM_GRU](04_Neural_Models/02_RNN_LSTM_GRU/)
- [x] [03_Neural_Text_Classification](04_Neural_Models/03_Neural_Text_Classification/)

## 05_Attention_and_Transformers
- [ ] [01_Attention](05_Attention_And_Transformers/01_Attention/)
- [ ] [02_Transformer_Architecture](05_Attention_And_Transformers/02_Transformer_Architecture/)
- [x] [03_GPT2_And_HF_Demos](05_Attention_And_Transformers/03_GPT2_And_HF_Demos/)

## 06_BERT
- [x] [01_BERT_Architecture_And_Tokenization](06_BERT/01_BERT_Architecture_And_Tokenization/)
- [x] [02_Pretraining_And_Fine_Tuning](06_BERT/02_Pretraining_And_Fine_Tuning/)
- [x] [03_BERT_Applications](06_BERT/03_BERT_Applications/)

## 08_Projects
- [x] [01_Spam_Message_Classifier](08_Projects/01_Spam_Message_Classifier/)
- [x] [02_Sentiment_Analysis_on_Reviews](08_Projects/02_Sentiment_Analysis_on_Reviews/)
- [x] [03_News_Topic_Classifier](08_Projects/03_News_Topic_Classifier/)
- [x] [04_Text_Summarization_Application](08_Projects/04_Text_Summarization_Application/)
- [x] [05_Named_Entity_Extraction](08_Projects/05_Named_Entity_Extraction/)
- [x] [06_Rule_Based_Chatbot](08_Projects/06_Rule_Based_Chatbot/)

## Course conventions

- Keep library implementations together inside each topic folder.
- Use lowercase snake_case filenames and add a library suffix when applicable.
- Name comparison notebooks `comparison.ipynb` and use the shared sample text.
- Keep each dataset next to the topic files that use it and avoid nesting beyond section / topic / files.

## Shared data

- [SMS Spam data instructions](08_Projects/01_Spam_Message_Classifier/README.md)
- [Sample texts](01_Preprocessing/sample_texts.txt)
- [Synthetic restaurant reviews dataset](04_Neural_Models/restaurant_reviews.tsv) — 1,000 labeled examples for sentiment analysis.
- [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) — included for the spam project at 08_Projects/01_Spam_Message_Classifier/sms_spam.tsv; licensed CC BY 4.0.
