
# 02 Text Cleaning and Normalization

## 1. Introduction

Text cleaning and normalization are important steps in Natural Language Processing (NLP). Raw text collected from websites, social media, documents, and user input often contains unwanted characters, HTML tags, extra spaces, inconsistent capitalization, and other noise.

Before giving text to an NLP model, we often clean and normalize it so that the text is consistent and suitable for the task.

**Example:**

Raw text:

```text
"  HELLO!!!   I am learning NLP &amp; Python.  "
```

After cleaning and normalization:

```text
hello!!! i am learning nlp & python.
```

The exact output depends on the cleaning rules we choose for our application.

## 2. Text Cleaning vs Text Normalization

| Text Cleaning | Text Normalization |
|---|---|
| Removes unwanted content or noise. | Converts text into a consistent form. |
| Removes HTML tags, unnecessary spaces, or unwanted URLs. | Converts text to lowercase or standardizes Unicode characters. |
| Focuses on removing irrelevant information. | Focuses on consistency in how text is represented. |
| Example: Removing `<p>` from HTML text. | Example: Converting `PYTHON` to `python`. |

Both processes are often performed together as part of text preprocessing.

## 3. Learning Objectives

After studying this topic, you should understand how to:

- Remove HTML tags and decode HTML entities.
- Handle URLs, email addresses, and extra whitespace.
- Normalize uppercase and lowercase text.
- Use Unicode normalization.
- Decide how to handle punctuation, numbers, emojis, and contractions.
- Build a reusable text-cleaning function in Python.

## 4. Common Text Cleaning Operations

| Operation | Before | After |
|---|---|---|
| Lowercasing | `HELLO WORLD` | `hello world` |
| Removing extra spaces | `Hello    World` | `Hello World` |
| Removing HTML tags | `<p>Hello</p>` | `Hello` |
| Decoding HTML entities | `Tom &amp; Jerry` | `Tom & Jerry` |
| Removing URLs | `Visit https://example.com` | `Visit` |
| Removing email addresses | `Contact abc@example.com` | `Contact` |
| Removing unwanted punctuation | `Hello!!!` | `Hello` |
| Unicode normalization | Equivalent Unicode forms | Consistent Unicode representation |

These operations are optional. Apply only the operations that suit your NLP task.

## 5. Typical Text Cleaning Pipeline

A basic pipeline may follow this order:

1. Receive raw text.
2. Decode HTML entities.
3. Remove HTML tags.
4. Replace or remove URLs and email addresses.
5. Normalize Unicode characters.
6. Convert text to lowercase, if appropriate.
7. Remove unwanted characters, if required.
8. Normalize whitespace.
9. Return the cleaned text.

The order can change depending on the data and the problem being solved.

## 6. Practical Python Implementation

The following example demonstrates several text-cleaning operations using Python's built-in libraries.

```python
import re
import unicodedata
from html import unescape


def clean_text(text):
    # Decode HTML entities
    text = unescape(text)

    # Normalize Unicode characters
    text = unicodedata.normalize("NFKC", text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Replace URLs with a space
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Replace email addresses with a space
    text = re.sub(
        r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b",
        " ",
        text
    )

    # Convert text to lowercase
    text = text.lower()

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


raw_text = """
    <p>HELLO!!! Visit https://example.com
    or email abc@example.com &amp; learn NLP.</p>
"""

cleaned_text = clean_text(raw_text)

print("Original Text:")
print(raw_text)

print("\nCleaned Text:")
print(cleaned_text)
```

### Output

```text
Original Text:

    <p>HELLO!!! Visit https://example.com
    or email abc@example.com &amp; learn NLP.</p>


Cleaned Text:
hello!!! visit or email learn nlp.
```

**Note:** This is a basic educational example. Regular expressions are not a complete HTML parser, and URL or email patterns may not cover every possible format.

## 7. Lowercase Conversion

Lowercasing converts uppercase letters into lowercase letters.

```python
text = "Machine Learning Is Interesting"

normalized_text = text.lower()

print(normalized_text)
```

Output:

```text
machine learning is interesting
```

Lowercasing can help treat words such as `Python` and `python` as the same token.

However, it may remove useful distinctions in some applications. Case-sensitive information can matter when identifying names, acronyms, or programming-language identifiers.

## 8. Unicode Normalization

Unicode allows some characters to be represented using different underlying sequences. Unicode normalization helps standardize these representations.

Python provides Unicode normalization through the `unicodedata` module.

```python
import unicodedata

text = "café"

normalized_text = unicodedata.normalize("NFC", text)

print(normalized_text)
```

Output:

```text
café
```

Common Unicode normalization forms include:

- **NFC:** Combines characters into a canonical composed form where possible.
- **NFD:** Decomposes characters into their canonical components.
- **NFKC:** Applies compatibility normalization and can convert some equivalent forms.
- **NFKD:** Applies compatibility decomposition.

NFKC can be useful for standardization, but it may change distinctions that matter in certain languages or specialized text. Choose the normalization form based on your data.

## 9. Handling Punctuation, Numbers, Emojis, and Contractions

Not every NLP task requires the same cleaning rules.

| Text Element | Example | Recommended Consideration |
|---|---|---|
| Punctuation | `Hello!!!` | Preserve or simplify according to the task. |
| Numbers | `I scored 95 marks.` | Keep them when numerical information matters. |
| Emojis | `This is great 😊` | Preserve them for sentiment analysis when useful. |
| Contractions | `don't`, `I'm` | Expand only when it benefits the task. |
| Hashtags | `#MachineLearning` | Preserve or extract the hashtag text. |
| Special characters | `C++`, `#AI` | Avoid removing meaningful symbols blindly. |

For example, removing all punctuation from `C++` could change the meaning of the programming-language name.

Similarly, removing emojis from social-media comments may discard useful sentiment information.

## 10. Text Cleaning in an NLP Workflow

Text cleaning is usually one part of a larger NLP pipeline.

1. **Raw Text:** Original documents, reviews, or messages.
2. **Text Cleaning and Normalization:** Remove unwanted content and standardize text.
3. **Tokenization:** Split text into tokens.
4. **Text Representation:** Convert text into numerical representations using methods such as Bag of Words, TF-IDF, or Word2Vec.
5. **NLP Model:** Apply tasks such as classification or sentiment analysis.

This is a common workflow, not a mandatory sequence for every model. Modern transformer models may use their own tokenizer and expect specific preprocessing rules.

## 11. Key Takeaways

- Text cleaning removes unwanted or irrelevant content.
- Text normalization makes text more consistent.
- Python's `re` module is useful for pattern-based cleaning.
- `unicodedata` supports Unicode normalization.
- `html.unescape()` converts HTML entities into their corresponding characters.
- Lowercasing, punctuation removal, and URL removal should depend on the NLP task.
- Avoid deleting information that could be useful to the model.
- Keep preprocessing consistent between training and inference.

## 12. References

- [Python `re` documentation](https://docs.python.org/3/library/re.html)
- [Python `unicodedata` documentation](https://docs.python.org/3/library/unicodedata.html)
- [Python `html` documentation](https://docs.python.org/3/library/html.html)
- [NLTK documentation](https://www.nltk.org/)
