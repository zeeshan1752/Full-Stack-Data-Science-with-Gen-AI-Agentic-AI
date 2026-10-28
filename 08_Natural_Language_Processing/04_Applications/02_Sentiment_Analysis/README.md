# Sentiment Analysis

Status: The code has not been run locally.

## Install

    python -m pip install scikit-learn

## Example

- [Train a sentiment classifier with scikit-learn](sentiment_analysis_sklearn.py)

The script uses the shared synthetic review dataset at 08_Natural_Language_Processing/data/restaurant_reviews.tsv. It splits those labeled examples into training and test portions, then prints the measured holdout accuracy.

## Run

    python 08_Natural_Language_Processing/04_Applications/02_Sentiment_Analysis/sentiment_analysis_sklearn.py

## Common mistakes

- A score on synthetic reviews does not show how a model will work on real customer reviews.
- Keep the test portion out of model fitting so it remains an independent check.
