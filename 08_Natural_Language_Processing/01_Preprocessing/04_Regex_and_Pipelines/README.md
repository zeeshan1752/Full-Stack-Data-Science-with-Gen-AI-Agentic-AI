# Regular Expressions and Text Pipelines

Status: The code has not been run locally.

## Install

The regular-expression example uses only Python's standard library. The pipeline example also needs scikit-learn:

    python -m pip install scikit-learn

## Examples

- [Clean text with regular expressions](regex_cleaning_re.py)
- [Combine cleaning and TF-IDF in a pipeline](preprocessing_pipeline_sklearn.py)

## What you will learn

Regular expressions can remove punctuation and normalize whitespace. A scikit-learn pipeline connects steps so that the same transformations are applied together.

Both scripts read the shared examples from the NLP data folder. They do not create a copy of that file.

## Run

From the repository root, run:

    python 08_Natural_Language_Processing/01_Preprocessing/04_Regex_and_Pipelines/regex_cleaning_re.py
    python 08_Natural_Language_Processing/01_Preprocessing/04_Regex_and_Pipelines/preprocessing_pipeline_sklearn.py

## Common mistakes

- A regular expression can remove useful punctuation or word forms. Check the cleaned text before using it.
- Fit a vectorizer only on training text when building a predictive model. This small pipeline example only demonstrates transformation.
