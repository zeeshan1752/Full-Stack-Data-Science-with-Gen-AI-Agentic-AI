# News Topic Classifier

Status: The code has not been run locally.

## Install

    python -m pip install scikit-learn

The first run needs an internet connection so scikit-learn can download and cache the 20 Newsgroups dataset. The dataset is not copied into this repository.

## Run

    python 08_Natural_Language_Processing/08_Projects/03_News_Topic_Classifier/news_topic_classifier_sklearn.py

## What you will learn

This example trains a text classifier on four 20 Newsgroups categories and prints its measured held-out accuracy. These are discussion-group posts organized by topic, used here as a news-topic-style classification exercise.

## Common mistakes

- The model may learn patterns specific to these discussion groups and categories.
- The scikit-learn documentation does not state a redistribution license for the downloaded data. Do not upload the dataset; review the original source terms before redistributing it.
