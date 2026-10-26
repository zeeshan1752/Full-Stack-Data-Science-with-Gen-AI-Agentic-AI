# 06 Text Preprocessing Pipelines

## 1. Introduction

A text preprocessing pipeline is an ordered sequence of operations that converts raw text into a format suitable for a particular Natural Language Processing (NLP) task.

Instead of writing separate cleaning steps every time, we combine them into a reusable function or pipeline. This makes preprocessing easier to maintain and helps ensure that text is processed consistently.

For example, a customer review might contain HTML markup, a URL, irregular spacing, and mixed capitalization. A pipeline can clean the markup, normalize the text, tokenize it, and optionally remove selected stop words.

**Important:** There is no single pipeline that is best for every NLP task. The correct steps depend on the data, model, and information that must be preserved.

## 2. Learning Objectives

After studying this topic, you should understand how to:

- Explain what a preprocessing pipeline is.
- Choose an appropriate order for preprocessing operations.
- Combine cleaning, normalization, and tokenization in Python.
- Make stop-word removal optional.
- Keep preprocessing reusable and consistent.
- Understand why stemming, lemmatization, and punctuation removal should be task-dependent.
- Recognize how traditional NLP pipelines differ from transformer preprocessing.

## 3. What Is a Pipeline?

A pipeline connects several processing steps so that the output of one step becomes the input to the next step.

A simple traditional NLP pipeline may look like this:

```text
Raw Text
   |
   v
HTML Entity Decoding
   |
   v
Remove HTML Markup and Selected URLs
   |
   v
Unicode and Whitespace Normalization
   |
   v
Lowercasing (when appropriate)
   |
   v
Tokenization
   |
   v
Optional Stop-Word Removal
   |
   v
Processed Tokens
   |
   v
Text Representation or NLP Model
```

Not every project needs every step. Removing URLs can be harmful if the URL itself is relevant, and lowercasing can remove useful distinctions in names or identifiers.

## 4. Main Pipeline Steps

| Step | Purpose | Example |
|---|---|---|
| HTML entity decoding | Converts encoded entities into characters. | `Tom &amp; Jerry` → `Tom & Jerry` |
| HTML markup removal | Removes simple markup from text. | `<p>Hello</p>` → `Hello` |
| URL handling | Removes or replaces URLs when they are not needed. | `Visit https://example.com` → `Visit` |
| Unicode normalization | Standardizes equivalent character representations. | Applies a chosen Unicode normalization form. |
| Lowercasing | Standardizes letter case. | `Python` → `python` |
| Whitespace normalization | Collapses repeated spaces and line breaks. | `hello   world` → `hello world` |
| Tokenization | Splits text into tokens. | `learn NLP` → `['learn', 'nlp']` |
| Stop-word removal | Removes selected tokens from a chosen list. | `the cat` → `cat` |
| Stemming or lemmatization | Optionally reduces word forms. | Depends on the selected algorithm and language. |

The examples are illustrative. Actual results depend on the rules and tools used.

## 5. A Basic Pipeline Using Python

This implementation uses only Python's standard library, so no third-party installation is required.

The example:
1. Decodes HTML entities.
2. Applies Unicode normalization.
3. Removes simple HTML-like tags.
4. Removes URLs and email addresses.
5. Converts text to lowercase.
6. Normalizes whitespace.
7. Tokenizes words and numbers.
8. Optionally removes a small demonstration list of stop words.

```python
import re
import unicodedata
from html import unescape


DEMO_STOP_WORDS = {
    "a", "an", "and", "are", "is", "of", "the", "to"
}


def clean_text(text):
    """Clean selected noise from a raw text string."""
    text = unescape(text)
    text = unicodedata.normalize("NFC", text)

    # Remove simple HTML-like tags (not a full HTML parser)
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove URLs and email addresses
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(
        r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b",
        " ",
        text
    )

    # Standardize case for this example
    text = text.lower()

    # Collapse repeated whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_text(text):
    """Return word-like tokens and numbers from cleaned text."""
    return re.findall(r"[a-z]+(?:'[a-z]+)?|\d+", text)


def preprocess_text(text, remove_stop_words=False):
    """Run the selected preprocessing steps and return tokens."""
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)

    if remove_stop_words:
        tokens = [
            token for token in tokens
            if token not in DEMO_STOP_WORDS
        ]

    return tokens


if __name__ == "__main__":
    raw_text = (
        "<p>THE Cat is learning NLP &amp; Python!</p> "
        "Visit https://example.com or email team@example.com."
    )

    print("Raw text:")
    print(raw_text)

    print("\nTokens without stop-word removal:")
    print(preprocess_text(raw_text))

    print("\nTokens with demo stop-word removal:")
    print(preprocess_text(raw_text, remove_stop_words=True))
```

### Expected Output

```text
Raw text:
<p>THE Cat is learning NLP &amp; Python!</p> Visit https://example.com or email team@example.com.

Tokens without stop-word removal:
['the', 'cat', 'is', 'learning', 'nlp', 'python', 'visit', 'or', 'email']

Tokens with demo stop-word removal:
['cat', 'learning', 'nlp', 'python', 'visit', 'or', 'email']
```

The stop-word list is intentionally small for demonstration. Notice that `or` remains because it is not in `DEMO_STOP_WORDS`. For a real project, choose and validate a language-appropriate list instead of relying on this demo list.

## 6. Why Is the Order Important?

The order of operations can affect the final output.

For example, decoding HTML entities before further text processing converts `&amp;` into `&`. Normalizing whitespace near the end ensures that extra spaces introduced when removing tags or URLs are collapsed.

Tokenization is usually performed after cleaning steps that affect word boundaries. However, some tokenizers are designed to handle raw text and punctuation themselves, so cleaning should not destroy information the tokenizer needs.

## 7. Optional Stop-Word Removal

Stop-word removal should be optional because frequently occurring words can still carry meaning.

Consider:

```text
This movie is not good.
```

Removing `not` could change the meaning of the sentence. This is especially important for sentiment analysis.

In the example pipeline, stop-word removal is controlled by the `remove_stop_words` argument. The demo list is not intended as a comprehensive English stop-word resource.

## 8. Stemming and Lemmatization

Stemming and lemmatization can be added when a task benefits from reducing word variations.

| Technique | What it does | Consideration |
|---|---|---|
| Stemming | Applies rules to reduce words to stems. | The result may not be a dictionary word. |
| Lemmatization | Attempts to return a dictionary base form. | May require language resources and part-of-speech information. |

Do not automatically apply both techniques. Choose based on the task and evaluate whether they improve results.

See the detailed notes:
- [Stemming](../04_Stop_Words_Stemming_and_Lemmatization/02_Stemming/README.md)
- [Lemmatization](../04_Stop_Words_Stemming_and_Lemmatization/03_Lemmatization/README.md)
- [Stop-Word Removal](../03_Stop_Word_Removal/README.md)

## 9. Traditional NLP vs Transformer Preprocessing

Traditional NLP workflows often clean text, tokenize it into words, and then use methods such as Bag of Words or TF-IDF.

Transformer models usually expect text to be passed through the tokenizer associated with the specific pretrained model. That tokenizer may handle subwords, special tokens, casing, and other model-specific details.

| Traditional NLP workflow | Transformer workflow |
|---|---|
| May use custom word tokenization. | Usually uses the model's own tokenizer. |
| May remove stop words or apply stemming. | Usually preserves the original wording unless model documentation specifies otherwise. |
| Often creates Bag of Words or TF-IDF features. | Converts text into token IDs and related model inputs. |
| Preprocessing choices are task-dependent. | Preprocessing must match the selected model's expectations. |

Do not apply aggressive text cleaning before a transformer by default. It can remove punctuation, casing, or other information that the model uses.

## 10. Reproducibility and Data Leakage

A pipeline should behave consistently during training, validation, testing, and prediction.

- Use the same deterministic text-cleaning rules for all data splits.
- Fit vocabulary-based transformations, such as a TF-IDF vectorizer, on the training data only.
- Do not use information from validation or test data to fit preprocessing parameters.
- Save or document the configuration used for preprocessing.
- Test how the pipeline handles empty strings, missing values, unusual Unicode, and unexpected input types.

Scikit-learn's `Pipeline` can connect feature extraction and model steps so learned transformations are fitted appropriately during model training and cross-validation.

## 11. Practical Design Principles

- Keep each operation in a small, understandable function.
- Make optional steps configurable.
- Preserve the original text when it may be needed for debugging or comparison.
- Avoid removing meaningful punctuation, numbers, emojis, or negation.
- Use language-specific tokenizers and resources when required.
- Do not treat regular expressions as a complete parser for HTML or natural language.
- Evaluate preprocessing decisions using the target task rather than assuming more cleaning is always better.

## 12. Related Files and Topics

- `Preprocessing_Pipeline.py` — runnable end-to-end pipeline example.
- [NLP Fundamentals](../01_NLP_Fundamentals/README.md)
- [Text Cleaning and Normalization](../02_Text_Cleaning_and_Normalization/README.md)
- [Tokenization](../03_Tokenization/README.md)
- [Regular Expressions](../05_Regular_Expressions/README.md)
- [Text Representation](../../02_Text_Representation/README.md)

## 13. Key Takeaways

- A preprocessing pipeline combines text-processing steps into a reusable workflow.
- The correct steps and order depend on the data and NLP task.
- Cleaning, normalization, and tokenization are common stages, while stop-word removal, stemming, and lemmatization are optional.
- Consistent preprocessing helps make training and inference results comparable.
- Transformer models generally require their own tokenizer and expected input format.
- Keep learned transformations, such as TF-IDF vocabulary fitting, inside the training workflow to avoid data leakage.

## 14. References

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python Unicode Data](https://docs.python.org/3/library/unicodedata.html)
- [NLTK Documentation](https://www.nltk.org/)
- [Scikit-learn Pipeline and Composite Estimators](https://scikit-learn.org/stable/modules/compose.html)
- [Scikit-learn Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html)
