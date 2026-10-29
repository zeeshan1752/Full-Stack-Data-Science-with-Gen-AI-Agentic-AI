
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(
    Path(__file__).resolve().parents[2] / "04_Neural_Models" / "restaurant_reviews.tsv",
    delimiter='\t',
    quoting=3
)

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')

corpus = []

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()

    review = [
        ps.stem(word)
        for word in review
        if word not in set(stopwords.words('english'))
    ]

    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()

y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    train_size= 0.7,
                                                    random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)


