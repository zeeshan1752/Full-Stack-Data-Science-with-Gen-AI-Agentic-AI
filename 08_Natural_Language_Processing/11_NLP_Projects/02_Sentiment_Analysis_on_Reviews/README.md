# Sentiment Analysis on Reviews

This project adapts the trainer's Restaurant Reviews example and keeps its text-cleaning, Porter-stemming, Bag-of-Words, and Naive Bayes sequence. The notebook fits the vocabulary on the training split and adds accuracy, a confusion matrix, and a classification report.

## Run the notebook

1. Place Restaurant_Reviews.tsv next to the notebook. The trainer archive did not include this dataset.
2. The file must contain Review and Liked columns; Liked uses 0 and 1 labels.
3. Install pandas, NLTK, and scikit-learn. If the English NLTK stop-word list is missing, run nltk.download('stopwords') once.
4. Open [Sentiment_Analysis_on_Reviews.ipynb](Sentiment_Analysis_on_Reviews.ipynb) and run its cells in order.

The notebook has not been executed here. Its saved outputs are empty until you run it with the dataset.
