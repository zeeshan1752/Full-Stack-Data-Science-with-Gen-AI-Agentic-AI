# 02. Text Cleaning and Normalization

Text cleaning and normalization prepare raw text for NLP by removing unwanted noise and applying consistent representations. The correct steps depend on the task: text for sentiment analysis, search, named-entity recognition, and a language model may need different preprocessing.

## Learning objectives

- Understand the difference between text cleaning and text normalization.
- Clean whitespace, HTML, URLs, email addresses, and unwanted characters when appropriate.
- Standardize case and Unicode text.
- Decide how to handle punctuation, numbers, emojis, contractions, and repeated characters.
- Build a reusable preprocessing function and inspect how each step changes the text.

## 1. Text cleaning vs. text normalization

**Text cleaning** removes or fixes content that is not useful for the intended task, such as HTML markup, accidental extra spaces, or corrupted characters.

**Text normalization** converts different surface forms into a consistent representation. Examples include lowercasing text, standardizing Unicode characters, or expanding selected contractions.

| Operation | Example | Purpose |
|---|---|---|
| Remove HTML tags | \`<p>Hello</p>\` → \`Hello\` | Remove markup while preserving visible text |
| Normalize whitespace | \`"hello   world"\` → \`"hello world"\` | Make spacing consistent |
| Lowercase | \`"Machine Learning"\` → \`"machine learning"\` | Treat case variants as the same form |
| Normalize Unicode | Convert equivalent Unicode forms to a consistent form | Reduce representation differences |
| Replace URLs | \`"Read https://example.com"\` → \`"Read URL"\` | Retain a signal that a link was present |
| Handle punctuation | Task-specific | Preserve or remove punctuation based on its meaning |
| Handle numbers | Keep, remove, or replace numbers | Match the needs of the task |

These operations are not universally required. For example, punctuation and capitalization may carry useful information for sentiment, intent, named-entity recognition, and language modeling.

## 2. A typical preprocessing pipeline

A basic pipeline may follow this order:

1. Receive the raw text.
2. Normalize Unicode representation.
3. Remove HTML markup if the source contains HTML.
4. Replace or remove URLs and email addresses if appropriate.
5. Normalize whitespace.
6. Apply task-specific case and punctuation handling.
7. Inspect the result before tokenization or vectorization.

This is a starting point, not a fixed rule. For example, if a task detects web addresses, do not remove URLs. If a model's tokenizer expects natural casing, do not lowercase text automatically.

## 3. Practical example with Python

The following example uses only Python's standard library. It removes simple HTML tags, replaces URLs and email addresses with descriptive placeholders, normalizes Unicode, and collapses repeated whitespace.

\`\`\`python
import re
import unicodedata
from html import unescape


def clean_text(text):
    # Decode HTML entities such as &amp; and &quot;.
    text = unescape(text)

    # Normalize equivalent Unicode representations.
    text = unicodedata.normalize("NFKC", text)

    # Remove simple HTML tags.
    text = re.sub(r"<[^>]+>", " ", text)

    # Replace URLs and email addresses with placeholders.
    text = re.sub(r"https?://\\S+|www\\.\\S+", " URL ", text)
    text = re.sub(
        r"\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b",
        " EMAIL ",
        text,
    )

    # Collapse repeated spaces, tabs, and line breaks.
    text = re.sub(r"\\s+", " ", text).strip()

    return text


raw_text = """
    <p>Machine   Learning is useful!</p>
    Visit https://example.com or email hello@example.com.
"""

cleaned_text = clean_text(raw_text)

print("Original text:")
print(raw_text)
print("\\nCleaned text:")
print(cleaned_text)
\`\`\`

Expected cleaned output:

\`\`\`text
Machine Learning is useful! Visit URL or email EMAIL.
\`\`\`

This is an introductory demonstration, not a complete HTML parser. For complex or malformed HTML, use a dedicated parser such as Beautiful Soup. Regex-based URL and email detection is also approximate; production applications may need more robust validation.

## 4. Lowercasing and case preservation

Lowercasing is common for traditional Bag of Words and TF-IDF workflows because it reduces vocabulary duplication:

- \`"Python"\`
- \`"PYTHON"\`
- \`"python"\`

After lowercasing, these forms become \`"python"\`.

However, case can contain meaning. For example, \`"US"\` can refer to the United States, while \`"us"\` is a pronoun. Named-entity recognition and some classification tasks may benefit from preserving case.

To lowercase text only when appropriate:

\`\`\`python
text = "Natural Language Processing"
lowercase_text = text.lower()

print(lowercase_text)
\`\`\`

Output:

\`\`\`text
natural language processing
\`\`\`

## 5. Unicode normalization

Text can contain visually identical characters represented by different Unicode sequences. Unicode normalization can make equivalent forms more consistent.

Python provides \`unicodedata.normalize()\`:

\`\`\`python
import unicodedata

text = "café"
normalized = unicodedata.normalize("NFC", text)

print(normalized)
\`\`\`

- **NFC** combines characters into a canonical composed form when possible.
- **NFD** decomposes characters into canonical components.
- **NFKC** applies compatibility normalization as well as canonical normalization.

NFKC can be useful for standardizing some full-width and compatibility characters, but it may change distinctions that matter in specialized text. Choose a normalization form based on the data and task.

## 6. Punctuation, numbers, emojis, and contractions

These elements should be handled intentionally rather than deleted automatically.

- **Punctuation:** punctuation can affect meaning and sentiment. \`"Great!"\` and \`"Great?"\` express different tones.
- **Numbers:** keep them for tasks such as financial text, dates, addresses, and product identification. Replace them with placeholders only when that supports the task.
- **Emojis:** emojis often convey sentiment or intent. Preserve them or map them deliberately if the task depends on their meaning.
- **Contractions:** expanding \`"can't"\` to \`"cannot"\` can standardize some corpora, but contractions may be meaningful features. Use a language-aware method when expansion is required.
- **Repeated characters:** reducing \`"soooo good"\` to \`"soo good"\` may help in some informal text, but aggressive normalization can remove emphasis.

## 7. How cleaning connects to later NLP steps

| Next step | How cleaning helps |
|---|---|
| Tokenization | Removes irrelevant markup and makes whitespace more consistent |
| Stop-word filtering | Produces text in a more predictable form before selecting tokens |
| Stemming and lemmatization | Gives the normalizer cleaner token input |
| Bag of Words and TF-IDF | Can reduce accidental vocabulary variants |
| Word embeddings | Provides more consistent training text when normalization is appropriate |
| Transformers | Must follow the selected model's tokenizer and preprocessing expectations |

Modern pretrained Transformer models usually provide their own tokenizer. Do not aggressively remove punctuation, lowercase text, or strip special characters before using one unless the model or task specifically requires it.

## 8. Related topics in this repository

- [Text Cleaning](01_Text_Cleaning/README.md)
- [Text Normalization](02_Text_Normalization/README.md)
- [Tokenization](../03_Tokenization/README.md)
- [Stop Words, Stemming, and Lemmatization](../04_Stop_Words_Stemming_and_Lemmatization/README.md)
- [Text Preprocessing overview](../README.md)

## Key takeaways

- Cleaning removes unwanted noise; normalization standardizes selected text forms.
- Preprocessing should be guided by the NLP task, not applied as a universal checklist.
- Keep the original text when possible so that preprocessing decisions can be reviewed.
- Use Python's \`re\`, \`html\`, and \`unicodedata\` modules for simple examples; use dedicated parsers for complex formats.
- Check the cleaned output on representative samples before applying it to a full dataset.
