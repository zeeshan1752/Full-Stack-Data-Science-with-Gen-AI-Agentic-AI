# Similarity and Clustering

Status: The code has not been run locally.

## Install

    python -m pip install scikit-learn

## Examples

- [Find the most similar pair of sample texts](text_similarity_sklearn.py)
- [Group sample texts with K-means](text_clustering_sklearn.py)

Both scripts reuse 08_Natural_Language_Processing/01_Preprocessing/sample_texts.txt.

## Run

    python 08_Natural_Language_Processing/07_Applications/03_Similarity_And_Clustering/text_similarity_sklearn.py
    python 08_Natural_Language_Processing/07_Applications/03_Similarity_And_Clustering/text_clustering_sklearn.py

## What you will learn

TF-IDF represents each text as weighted word features. Cosine similarity compares two such vectors. K-means assigns vectors to a chosen number of groups.

## Common mistakes

- Similarity is based on word overlap here; it does not understand meaning like a language model.
- K-means needs a chosen cluster count, and changing that count changes the groups.
