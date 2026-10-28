# Spam Message Classifier

Status: The code has not been run locally.

## Install

    python -m pip install scikit-learn

## Dataset

Download the SMS Spam Collection from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection). Extract the tab-separated file named SMSSpamCollection and place it at:

    08_Natural_Language_Processing/data/sms_spam.tsv

The dataset is licensed CC BY 4.0. Keep the source attribution in SOURCES.md if you redistribute it; this repository does not include the dataset file.

## Run

    python 08_Natural_Language_Processing/08_Projects/01_Spam_Message_Classifier/spam_message_classifier_sklearn.py

## What you will learn

The project turns messages into TF-IDF features and trains a logistic-regression classifier. It reports results on a held-out split and can classify one example message.

## Common mistakes

- Do not move the dataset into this project folder; shared data belongs in the NLP data folder.
- A spam model may miss new scam patterns. Do not rely on it as a safety filter.
