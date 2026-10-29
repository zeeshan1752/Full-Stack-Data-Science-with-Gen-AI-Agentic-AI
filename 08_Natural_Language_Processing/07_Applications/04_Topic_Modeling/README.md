# Topic Modeling

Status: The code has not been run locally.

## Install

    python -m pip install scikit-learn

## Example

- [Discover word groups with scikit-learn LDA](topic_modeling_sklearn.py)

The example reads the shared sample texts. It prints the highest-weight words for each discovered topic.

## Run

    python 08_Natural_Language_Processing/07_Applications/04_Topic_Modeling/topic_modeling_sklearn.py

## What you will learn

Latent Dirichlet Allocation (LDA) finds word groups that tend to occur together across documents. The topic numbers have no built-in meaning; you interpret them by looking at their words.

## Common mistakes

- A handful of sample sentences is only enough to demonstrate the steps, not to discover stable real-world topics.
- Topic order and word weights can change with the data and model settings.
