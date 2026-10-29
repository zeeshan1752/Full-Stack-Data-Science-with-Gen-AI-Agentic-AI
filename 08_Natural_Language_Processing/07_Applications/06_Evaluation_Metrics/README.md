# Evaluation Metrics

Status: The code has not been run locally.

## Install

    python -m pip install scikit-learn

## Example

- [Calculate classification metrics](classification_metrics_sklearn.py)

## What you will learn

Accuracy is the share of predictions that match the labels. Precision, recall, and F1 describe positive-class errors and trade-offs. A confusion matrix counts correct and incorrect predictions by class.

The script uses a small, explicitly illustrative list of labels and predictions. It does not claim to measure a trained model.

## Run

    python 08_Natural_Language_Processing/07_Applications/06_Evaluation_Metrics/classification_metrics_sklearn.py

## Common mistakes

- Accuracy can hide poor performance when one class is much more common than another.
- State which label is treated as positive when interpreting precision and recall.
