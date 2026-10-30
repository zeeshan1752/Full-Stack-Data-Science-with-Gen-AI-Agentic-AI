# Regular Expressions and Text Pipelines

## 1. Introduction

Regular Expressions (Regex) and Text Pipelines are useful techniques in Natural Language Processing (NLP). They help clean raw text, identify patterns, transform documents, and prepare text for machine learning algorithms.

Raw text often contains unnecessary punctuation, extra spaces, numbers, special characters, and inconsistent formatting. Before applying NLP techniques, the text may need to be cleaned and normalized.

- **Regular Expressions:** Used to search, match, extract, split, and replace text patterns.
- **Text Pipelines:** Used to connect multiple preprocessing and machine learning steps into a single workflow.

These techniques are commonly used in text classification, sentiment analysis, spam detection, document processing, and information retrieval.

## 2. Regular Expressions

A regular expression is a sequence of characters that defines a search pattern. Python provides the built-in `re` module for working with regular expressions.

Regex can identify patterns without requiring every possible matching word or character sequence to be specified individually.

For example, a regular expression can identify all digits in a sentence, remove punctuation, find email addresses, or replace multiple spaces with a single space.

### 2.1 Importing the Regex Module

```python
import re
```

The `re` module is part of Python's standard library. It does not require a separate installation.

## 3. Common Regex Functions

| Function | Description |
|---|---|
| `re.search()` | Finds the first match anywhere in the string |
| `re.match()` | Checks for a match at the beginning of the string |
| `re.fullmatch()` | Checks whether the entire string matches the pattern |
| `re.findall()` | Returns all non-overlapping matches as a list |
| `re.finditer()` | Returns an iterator of match objects |
| `re.sub()` | Replaces matching text with another string |
| `re.subn()` | Replaces matches and returns the result with the replacement count |
| `re.split()` | Splits a string wherever the pattern matches |
| `re.compile()` | Compiles a pattern for repeated use |

### 3.1 Example: Finding Matches

```python
import re

text = "NLP is useful. NLP is interesting."

result = re.search(r"NLP", text)
print(result.group() if result else "No match found")

all_matches = re.findall(r"NLP", text)
print(all_matches)
```

Output:

```text
NLP
['NLP', 'NLP']
```

`re.search()` returns the first matching object, while `re.findall()` returns all matching occurrences.

### 3.2 Example: Replacing Text

```python
import re

text = "I like Java. Java is popular."

result = re.sub(r"Java", "Python", text)

print(result)
```

Output:

```text
I like Python. Python is popular.
```

### 3.3 Example: Splitting Text

```python
import re

text = "Python,Java;SQL NLP"

result = re.split(r"[,;\s]+", text)

print(result)
```

Output:

```text
['Python', 'Java', 'SQL', 'NLP']
```

The pattern matches one or more commas, semicolons, or whitespace characters.

## 4. Common Regex Patterns

### 4.1 Character Patterns

| Pattern | Description | Example |
|---|---|---|
| `.` | Matches any character except a newline by default | `a.c` matches `abc` |
| `\d` | Matches a digit | `\d` matches `7` |
| `\D` | Matches a non-digit | `\D` matches `A` |
| `\w` | Matches a word character: letters, digits, and underscore | `\w+` matches `hello_1` |
| `\W` | Matches a character that is not a word character | `\W` matches `@` |
| `\s` | Matches whitespace, including spaces and tabs | `\s+` matches multiple spaces |
| `\S` | Matches a non-whitespace character | `\S+` matches a word-like sequence |
| `\b` | Matches a word boundary | `\bcat\b` matches `cat` as a separate word |
| `\B` | Matches a position that is not a word boundary | `\Bcat` can match `cat` inside `educate` |
| `\A` | Matches the beginning of the string | `\AHello` |
| `\Z` | Matches the end of the string | `world\Z` |

Using raw strings such as `r"\d+"` is recommended because backslashes are interpreted as part of the regular expression rather than ordinary Python string escapes.

### 4.2 Quantifiers

Quantifiers specify how many times a pattern may occur.

| Pattern | Description | Example |
|---|---|---|
| `*` | Zero or more occurrences | `ab*c` matches `ac`, `abc`, `abbc` |
| `+` | One or more occurrences | `ab+c` matches `abc`, `abbc` |
| `?` | Zero or one occurrence | `colou?r` matches `color` and `colour` |
| `{n}` | Exactly `n` occurrences | `\d{4}` matches four digits |
| `{n,}` | At least `n` occurrences | `\d{2,}` matches two or more digits |
| `{n,m}` | Between `n` and `m` occurrences | `\d{2,4}` matches two to four digits |

Example:

```python
import re

text = "A 7 B 42 C 2026"

result = re.findall(r"\d+", text)

print(result)
```

Output:

```text
['7', '42', '2026']
```

The `+` quantifier groups consecutive digits into a single match.

### 4.3 Character Classes

Character classes match one character from a specified set.

| Pattern | Description |
|---|---|
| `[abc]` | Matches `a`, `b`, or `c` |
| `[a-z]` | Matches lowercase English letters |
| `[A-Z]` | Matches uppercase English letters |
| `[0-9]` | Matches digits |
| `[a-zA-Z]` | Matches English letters in either case |
| `[a-zA-Z0-9]` | Matches English letters and digits |
| `[^abc]` | Matches a character other than `a`, `b`, or `c` |
| `[^0-9]` | Matches a character that is not a digit |
| `[aeiou]` | Matches a lowercase vowel |
| `[.,!?]` | Matches any one listed punctuation mark |

Example:

```python
import re

text = "NLP2026 is useful!"

letters = re.findall(r"[A-Za-z]+", text)
digits = re.findall(r"[0-9]+", text)
punctuation = re.findall(r"[.,!?]", text)

print("Letters:", letters)
print("Digits:", digits)
print("Punctuation:", punctuation)
```

Output:

```text
Letters: ['NLP', 'is', 'useful']
Digits: ['2026']
Punctuation: ['!']
```

### 4.4 Anchors

Anchors match positions in a string rather than actual characters.

| Pattern | Description |
|---|---|
| `^Python` | Matches `Python` at the beginning of the string |
| `Python$` | Matches `Python` at the end of the string |
| `\AHello` | Matches `Hello` at the absolute beginning |
| `world\Z` | Matches `world` at the absolute end |

Example:

```python
import re

text = "Python is easy to learn"

print(bool(re.search(r"^Python", text)))
print(bool(re.search(r"learn$", text)))
```

Output:

```text
True
True
```

The meanings of `^` and `$` can change when multiline mode is enabled. In multiline mode, they can match the beginning and end of individual lines.

### 4.5 Alternation and Grouping

| Pattern | Description |
|---|---|
| `cat|dog` | Matches either `cat` or `dog` |
| `(abc)` | Groups a pattern and captures the match |
| `(?:abc)` | Groups a pattern without capturing it |
| `(a)(b)` | Captures two separate groups |
| `(?P<name>...)` | Creates a named capturing group |

Example:

```python
import re

text = "I use Python and Java."

result = re.findall(r"Python|Java", text)

print(result)
```

Output:

```text
['Python', 'Java']
```

Alternation is useful when multiple patterns should be accepted.

### 4.6 Greedy and Non-Greedy Matching

By default, quantifiers such as `*` and `+` are greedy. They attempt to match as much text as possible.

Adding `?` after a quantifier makes it non-greedy, meaning it attempts to match as little text as possible while still satisfying the pattern.

```python
import re

text = "<title>First</title><title>Second</title>"

greedy = re.findall(r"<title>.*</title>", text)
non_greedy = re.findall(r"<title>.*?</title>", text)

print("Greedy:", greedy)
print("Non-greedy:", non_greedy)
```

The greedy pattern matches from the first opening tag to the last closing tag. The non-greedy pattern finds each title separately.

### 4.7 Lookahead and Lookbehind

Lookarounds check surrounding text without including that surrounding text in the match.

| Pattern | Description |
|---|---|
| `(?=...)` | Positive lookahead: the following text must match |
| `(?!...)` | Negative lookahead: the following text must not match |
| `(?<=...)` | Positive lookbehind: the preceding text must match |
| `(?<!...)` | Negative lookbehind: the preceding text must not match |

Example:

```python
import re

text = "Item 100 costs 50. Item 200 costs 75."

result = re.findall(r"\d+(?=\.)", text)

print(result)
```

Output:

```text
['50', '75']
```

The lookahead matches numbers immediately followed by a period without including the period itself.

Lookbehind patterns in Python's standard `re` module have restrictions, including fixed-width requirements for lookbehind expressions.

### 4.8 Regex Flags

Flags modify how a regular expression behaves.

| Flag | Description |
|---|---|
| `re.IGNORECASE` or `re.I` | Performs case-insensitive matching |
| `re.MULTILINE` or `re.M` | Makes `^` and `$` operate on individual lines |
| `re.DOTALL` or `re.S` | Allows `.` to match newline characters |
| `re.VERBOSE` or `re.X` | Allows readable patterns with whitespace and comments |

Example:

```python
import re

text = "Python is powerful. PYTHON is popular."

result = re.findall(r"python", text, flags=re.IGNORECASE)

print(result)
```

Output:

```text
['Python', 'PYTHON']
```

## 5. Regex for Text Cleaning

Text cleaning is an important preprocessing step in NLP. It removes or modifies text elements according to the requirements of a task.

### 5.1 Remove Punctuation

```python
import re

text = "Hello!!! Welcome to NLP, Python & AI."

cleaned_text = re.sub(r"[^\w\s]", "", text)

print(cleaned_text)
```

Output:

```text
Hello Welcome to NLP Python  AI
```

The character class `[^\w\s]` matches characters that are neither word characters nor whitespace.

**Note:** This pattern retains underscores because `_` is included in `\w`. Removing punctuation can also remove meaningful symbols, so the pattern should be selected according to the dataset and task.

### 5.2 Remove Digits

```python
import re

text = "NLP started in 2026 with 100 examples."

cleaned_text = re.sub(r"\d+", "", text)

print(cleaned_text)
```

Output:

```text
NLP started in  with  examples.
```

Use digit removal only when numerical information is unnecessary for the task.

### 5.3 Remove Extra Whitespace

```python
import re

text = "Natural    Language   Processing"

cleaned_text = re.sub(r"\s+", " ", text).strip()

print(cleaned_text)
```

Output:

```text
Natural Language Processing
```

The pattern `\s+` matches one or more consecutive whitespace characters. The `strip()` method removes whitespace from the beginning and end.

### 5.4 Extract Email Addresses

```python
import re

text = "Contact us at student@example.com or admin@example.org."

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print(emails)
```

Output:

```text
['student@example.com', 'admin@example.org']
```

This is a practical pattern for simple examples, not a complete validator for every valid email address.

### 5.5 Extract Numbers

```python
import re

text = "Python 3.12, score 95, and price 250.50"

numbers = re.findall(r"\d+(?:\.\d+)?", text)

print(numbers)
```

Output:

```text
['3.12', '95', '250.50']
```

The optional non-capturing group `(?:\.\d+)?` allows a decimal portion.

### 5.6 Extract Hashtags

```python
import re

text = "Learning #Python and #NLP with #MachineLearning"

hashtags = re.findall(r"#[A-Za-z0-9_]+", text)

print(hashtags)
```

Output:

```text
['#Python', '#NLP', '#MachineLearning']
```

Hashtag patterns may need to be adapted to support Unicode letters and platform-specific rules.

### 5.7 Replace Multiple Punctuation Marks

```python
import re

text = "This is amazing!!! Really??? Yes..."

cleaned_text = re.sub(r"[!?.,]+", ".", text)

print(cleaned_text)
```

Output:

```text
This is amazing. Really. Yes.
```

This example replaces consecutive periods, exclamation marks, or question marks with a single period.

## 6. Building a Text Cleaning Workflow

Multiple Regex operations can be applied in sequence to clean a document.

```python
import re

text = "  Hello!!!   NLP is useful in 2026. Visit @example  "

# Convert text to lowercase
text = text.lower()

# Remove mentions beginning with @
text = re.sub(r"@\w+", "", text)

# Remove punctuation and special characters
text = re.sub(r"[^\w\s]", "", text)

# Replace multiple whitespace characters
text = re.sub(r"\s+", " ", text)

# Remove leading and trailing whitespace
text = text.strip()

print(text)
```

Output:

```text
hello nlp is useful in 2026 visit
```

Each operation handles a different part of the cleaning process. The order matters because one transformation can affect the input to subsequent transformations.

For example, converting text to lowercase changes letter case, while removing punctuation can remove symbols that may be meaningful in URLs, code, or sentiment analysis.

## 7. Introduction to Text Pipelines

A text pipeline combines multiple processing steps into a single workflow. It is useful when raw text must be transformed into numerical features before being used by a machine learning model.

A typical text classification workflow is:

1. Collect raw text documents.
2. Clean and normalize the text.
3. Convert the text into numerical features.
4. Train a machine learning model.
5. Use the fitted pipeline to predict the class of new documents.

A pipeline makes it easier to keep the steps organized and apply them consistently.

## 8. Scikit-learn Pipeline

Scikit-learn provides the `Pipeline` class to combine transformers and an optional final estimator.

A transformer processes input data and returns transformed data. An estimator learns from data and can make predictions.

In a text pipeline:

- `TfidfVectorizer` converts text into numerical features.
- A classifier learns patterns from those features.
- `Pipeline` connects the vectorizer and classifier in the correct order.

### 8.1 Installing Scikit-learn

```bash
python -m pip install scikit-learn
```

### 8.2 Example: TF-IDF and Logistic Regression

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "I love this product",
    "This product is excellent",
    "I hate this product",
    "This product is terrible"
]

labels = [1, 1, 0, 0]

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

# Train the pipeline
pipeline.fit(texts, labels)

# Predict classes for new text
new_texts = [
    "I love this",
    "This is terrible"
]

predictions = pipeline.predict(new_texts)

print(predictions)
```

The labels represent two example classes: `1` and `0`. The example demonstrates the pipeline workflow rather than a production-ready sentiment model.

### 8.3 How the Pipeline Works

When `pipeline.fit(texts, labels)` is called:

1. `TfidfVectorizer` learns its vocabulary and IDF values from the training documents.
2. The training documents are transformed into TF-IDF feature vectors.
3. `LogisticRegression` is trained using those feature vectors and the labels.

When `pipeline.predict(new_texts)` is called:

1. The new documents are transformed using the already-fitted TF-IDF vectorizer.
2. The classifier predicts a class for each document.

The vectorizer is not fitted again on the new documents. This keeps the feature representation consistent between training and prediction.

## 9. Understanding TF-IDF

TF-IDF stands for **Term Frequency–Inverse Document Frequency**. It is a text representation technique that assigns numerical weights to terms in a collection of documents.

### 9.1 Term Frequency (TF)

Term frequency measures how often a term occurs in a document.

A simple definition is:

`TF(t, d) = count of term t in document d / total terms in document d`

### 9.2 Inverse Document Frequency (IDF)

Inverse document frequency reduces the weight of terms that appear in many documents.

One common smoothed formulation used by scikit-learn is:

`IDF(t) = log((1 + N) / (1 + df(t))) + 1`

Where:

- `N` is the total number of documents.
- `df(t)` is the number of documents containing term `t`.

The TF-IDF weight is based on the combination of term frequency and inverse document frequency.

### 9.3 Applications of TF-IDF

- Text classification.
- Spam detection.
- Document similarity.
- Information retrieval.
- Search and ranking systems.
- Basic sentiment analysis.

TF-IDF does not understand the meaning of words in the way a contextual language model does. It represents terms using statistical information from the document collection.

## 10. Combining Custom Regex Cleaning with a Pipeline

Regex cleaning can be incorporated into a scikit-learn pipeline by implementing it as a custom transformer.

The following example creates a reusable cleaning transformer and connects it to TF-IDF vectorization and logistic regression.

```python
import re

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class RegexCleaner(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        cleaned_texts = []

        for text in X:
            text = text.lower()
            text = re.sub(r"[^\w\s]", " ", text)
            text = re.sub(r"\s+", " ", text)
            text = text.strip()

            cleaned_texts.append(text)

        return cleaned_texts


texts = [
    "I love this product!!!",
    "This product is excellent.",
    "I hate this product!!!",
    "This product is terrible."
]

labels = [1, 1, 0, 0]

pipeline = Pipeline([
    ("cleaner", RegexCleaner()),
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

pipeline.fit(texts, labels)

new_texts = [
    "I love it!",
    "This is terrible!"
]

predictions = pipeline.predict(new_texts)

print(predictions)
```

In this example:

- `RegexCleaner` applies the same cleaning rules to training and new text.
- `TfidfVectorizer` converts the cleaned text into numerical features.
- `LogisticRegression` learns from those features and predicts classes.

The custom transformer implements `fit()` and `transform()` so that it can be used as a preprocessing step in scikit-learn's pipeline.

## 11. Data Leakage and Correct Pipeline Usage

Data leakage occurs when information from outside the training data improperly influences model training. It can lead to overly optimistic evaluation results.

For text machine learning:

- Split the data into training and test sets before fitting the vectorizer.
- Fit preprocessing steps that learn from the dataset only on the training data.
- Use the fitted pipeline to transform the test data and make predictions.
- Do not fit TF-IDF separately on the complete dataset before splitting it.

A scikit-learn pipeline helps prevent common leakage problems by fitting its transformers on the data supplied to `fit()` and reusing them during prediction.

For model evaluation, the training and test sets should remain separate until evaluation.

## 12. Regex and Text Pipelines: Comparison

| Feature | Regular Expressions | Text Pipelines |
|---|---|---|
| Main purpose | Match and manipulate text patterns | Connect processing and modeling steps |
| Main tool | Python `re` module | Scikit-learn `Pipeline` |
| Input | Usually strings | Data accepted by each pipeline step |
| Output | Matched, extracted, or modified text | Transformed features or model predictions |
| Typical use | Cleaning, extraction, pattern matching | Repeatable preprocessing and machine learning |
| Learns from data | Usually no | Some steps, such as TF-IDF and classifiers, learn from training data |
| Example | Removing repeated spaces | TF-IDF followed by logistic regression |

Regex and pipelines are complementary rather than competing techniques. Regex can perform text cleaning, while a pipeline can combine that cleaning with vectorization and modeling.

## 13. Installation and Execution

The regular-expression example uses only Python's standard library. The scikit-learn pipeline example requires scikit-learn.

Install the dependency:

```bash
python -m pip install scikit-learn
```

Run the scripts from the repository root:

```bash
python 08_Natural_Language_Processing/01_Preprocessing/04_Regex_And_Pipelines/regex_cleaning_re.py
```

```bash
python 08_Natural_Language_Processing/01_Preprocessing/04_Regex_And_Pipelines/preprocessing_pipeline_sklearn.py
```

**Status:** The code has not been run locally, so the outputs have not been verified.

## 14. Key Points

- Regex patterns identify characters, words, and other text structures.
- Python's `re` module supports searching, extraction, replacement, splitting, and matching.
- Character classes describe which characters can match.
- Quantifiers specify how many occurrences are allowed.
- Anchors identify positions in a string.
- Lookarounds check surrounding text without including it in the match.
- Regex can help remove unwanted characters and normalize whitespace.
- Cleaning rules must preserve information relevant to the NLP task.
- TF-IDF converts text into numerical features.
- Scikit-learn's `Pipeline` connects compatible preprocessing and modeling steps.
- Custom transformers allow reusable cleaning logic to become part of a pipeline.
- Fitting preprocessing steps only on training data helps avoid data leakage.