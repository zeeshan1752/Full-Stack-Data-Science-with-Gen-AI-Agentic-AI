# Spam Message Classifier

Status: The code has not been run locally.

## Install

    python -m pip install scikit-learn

## Dataset

Download the SMS Spam Collection from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection). Extract the tab-separated file named SMSSpamCollection and place it at:

    08_Natural_Language_Processing/08_Projects/01_Spam_Message_Classifier/sms_spam.tsv

The dataset is licensed CC BY 4.0, as listed by UCI. If redistributed, include attribution to Almeida and Hidalgo's UCI SMS Spam Collection. The extracted file is included in this project folder.

## Run

    python 08_Natural_Language_Processing/08_Projects/01_Spam_Message_Classifier/spam_message_classifier_sklearn.py

## What you will learn

The project turns messages into TF-IDF features and trains a logistic-regression classifier. It reports results on a held-out split and can classify one example message.

## Common mistakes

- Keep `sms_spam.tsv` in this project folder next to the classifier script.
- A spam model may miss new scam patterns. Do not rely on it as a safety filter.
