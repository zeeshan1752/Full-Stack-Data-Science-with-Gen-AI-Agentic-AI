# Text Cleaning

Text Cleaning is an important preprocessing step in Natural Language Processing (NLP). It involves removing unwanted elements, correcting inconsistencies, and standardizing raw text before performing further analysis.

Text collected from websites, social media, documents, and user inputs may contain HTML tags, unnecessary punctuation, extra spaces, inconsistent capitalization, and other elements that can affect text processing.

The main goal of text cleaning is to prepare text in a consistent and useful format while preserving the information required for the task.

## 1. Why Is Text Cleaning Important?

Raw text is not always ready for analysis. Consider the following example:

**Original text:**

```text
<HTML><body>  HELLO!!!   I am Learning NLP. </body></HTML>
```

**After cleaning:**

```text
hello i am learning nlp
```

The cleaned text is easier to process using techniques such as Tokenization, Bag of Words (BoW), TF-IDF, and other NLP methods.

Text cleaning helps to:

- Remove unnecessary HTML tags and markup.
- Standardize uppercase and lowercase characters.
- Handle punctuation according to the task.
- Remove unnecessary spaces and line breaks.
- Prepare text for tokenization and feature extraction.
- Reduce unwanted variations in text data.

**Important:** Cleaning should not remove meaningful information. The correct cleaning process depends on the dataset and the problem being solved.

## 2. Common Text Cleaning Operations

### 2.1 Lowercasing

Lowercasing converts all uppercase letters into lowercase letters.

**Example:**

```text
Original:  Machine Learning Is Interesting
Cleaned:   machine learning is interesting
```

Python:

```python
text = "Machine Learning Is Interesting"

cleaned_text = text.lower()

print(cleaned_text)
```

Output:

```text
machine learning is interesting
```

**Why is it useful?**

Without lowercasing, some text-processing methods may treat `Python`, `PYTHON`, and `python` as different tokens.

**When should you avoid it?**

In tasks involving named entities, acronyms, or case-sensitive information, capitalization may carry useful meaning.

### 2.2 Removing HTML Tags

Text collected from websites may contain HTML elements such as `<p>`, `<div>`, and `<b>`.

**Example:**

```text
Original:  <p>Welcome to <b>NLP</b></p>
Cleaned:   Welcome to NLP
```

Python:

```python
import re

text = "<p>Welcome to <b>NLP</b></p>"

cleaned_text = re.sub(r"<[^>]+>", "", text)

print(cleaned_text)
```

Output:

```text
Welcome to NLP
```

The regular expression `r"<[^>]+>"` matches simple strings that resemble HTML tags.

**Limitation:** Regular expressions are suitable for simple demonstrations, but they are not a complete HTML parser. For complex or malformed HTML, use a dedicated HTML parser such as Beautiful Soup.

### 2.3 Removing or Replacing Punctuation

Punctuation includes characters such as:

```text
! ? , . ; : ' " ( ) [ ] { }
```

Depending on the task, punctuation can be removed or replaced with spaces.

**Example:**

```text
Original:  Hello!!! How are you?
Cleaned:   Hello How are you
```

Python:

```python
import string

text = "Hello!!! How are you?"

translator = str.maketrans(
    string.punctuation,
    " " * len(string.punctuation)
)

cleaned_text = text.translate(translator)

print(cleaned_text)
```

Output:

```text
Hello    How are you 
```

The result still contains extra spaces, which can be handled through whitespace normalization.

**Why replace punctuation with spaces instead of deleting it directly?**

Consider:

```text
Original:  data-driven
Deleting:  datadriven
Replacing: data driven
```

Replacing punctuation with spaces helps prevent unrelated words from being joined accidentally.

However, punctuation may be meaningful in URLs, programming languages, financial data, and sentiment analysis. Choose the method according to the application.

### 2.4 Normalizing Whitespace

Raw text may contain multiple spaces, tabs, and newline characters.

**Example:**

```text
Original:  "Python    is\n\n easy"
Cleaned:   "Python is easy"
```

Python:

```python
import re

text = "Python    is\n\n easy"

cleaned_text = re.sub(r"\s+", " ", text).strip()

print(cleaned_text)
```

Output:

```text
Python is easy
```

Explanation:

- `\s+` matches one or more whitespace characters.
- `" "` replaces the matched characters with a single space.
- `.strip()` removes whitespace from the beginning and end.

This operation makes text more consistent and readable.

### 2.5 Handling Numbers

Numbers may or may not be important in an NLP task.

For example:

```text
Original:  I bought 3 books for ₹500.
```

Possible cleaned outputs:

```text
Keep numbers:    I bought 3 books for ₹500.
Remove numbers:  I bought books for ₹.
```

Removing digits blindly can destroy useful information, such as prices, ages, dates, ratings, and quantities.

If numbers need to be removed, define a rule that considers the type of data and the intended analysis.

### 2.6 Handling Apostrophes and Contractions

Apostrophes appear in words such as:

```text
don't
I'm
you're
isn't
```

Removing apostrophes can produce:

```text
don't → don t
```

Alternatively, contraction expansion can produce:

```text
don't → do not
I'm → I am
```

Contraction expansion may be useful for certain NLP applications, but it should be performed carefully because not every apostrophe has the same meaning.

For a basic cleaning pipeline, preserve apostrophes unless the task specifically requires removing or expanding them.

## 3. Complete Text Cleaning Example

The following example combines several common operations into one reusable function.

```python
import re
import string

def clean_text(text):
    # Remove simple HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Convert text to lowercase
    text = text.lower()

    # Replace punctuation with spaces
    translator = str.maketrans(
        string.punctuation,
        " " * len(string.punctuation)
    )
    text = text.translate(translator)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


text = "<p>HELLO!!!   Welcome to NLP.</p>"

cleaned_text = clean_text(text)

print("Original Text:", text)
print("Cleaned Text:", cleaned_text)
```

**Output:**

```text
Original Text: <p>HELLO!!!   Welcome to NLP.</p>
Cleaned Text: hello welcome to nlp
```

This function performs four operations:

1. Removes simple HTML tags.
2. Converts the text to lowercase.
3. Replaces ASCII punctuation with spaces.
4. Normalizes whitespace.

It does not remove numbers or perform stop-word removal, stemming, or lemmatization. Those are separate preprocessing decisions.

## 4. Understanding the Regular Expressions

Regular expressions, commonly called regex, are patterns used to search for and manipulate text.

| Pattern | Meaning |
|---|---|
| `r"<[^>]+>"` | Matches simple HTML-like tags |
| `r"\s+"` | Matches one or more whitespace characters |
| `r"\d+"` | Matches one or more digits |
| `r"[A-Za-z]+"` | Matches sequences of English letters |
| `r"[^\w\s]"` | Matches characters that are neither word characters nor whitespace |

Examples:

```python
import re

text = "Python   123   NLP"

print(re.sub(r"\s+", " ", text))
print(re.sub(r"\d+", "", text))
```

Output:

```text
Python 123 NLP
Python    NLP
```

Notice that removing digits can leave extra spaces. A complete cleaning pipeline should normalize whitespace after operations that may introduce it.

## 5. Text Cleaning Before and After

| Operation | Before | After |
|---|---|---|
| Lowercasing | `HELLO World` | `hello world` |
| HTML removal | `<b>Python</b>` | `Python` |
| Punctuation replacement | `Hello!!!` | `Hello` |
| Whitespace normalization | `NLP   is easy` | `NLP is easy` |
| Digit removal, when required | `Python 3` | `Python` |

The examples above illustrate individual operations. Their order matters because one operation may change the input for the next operation.

## 6. Text Cleaning in an NLP Pipeline

Text cleaning is usually one stage in a larger workflow.

```text
Raw Text
   ↓
Text Cleaning
   ↓
Tokenization
   ↓
Optional Stop-Word Removal
   ↓
Text Representation
   ↓
Machine Learning Model
```

For example, a Bag of Words pipeline may clean a sentence before converting it into a numerical representation.

**Raw text:**

```text
"Python is AMAZING!!!"
```

**After cleaning:**

```text
python is amazing
```

**After tokenization:**

```python
["python", "is", "amazing"]
```

**After Bag of Words representation:**

The sentence can be represented using numerical features that count the occurrences of vocabulary words.

Text cleaning prepares the input, tokenization splits it into units, and Bag of Words converts those units into numerical features.

## 7. Practical Applications

### Sentiment Analysis

Reviews often contain inconsistent capitalization, punctuation, and spacing.

```text
Original: "THIS PRODUCT IS AMAZING!!!"
Cleaned:  "this product is amazing"
```

Cleaning can make text more consistent before feature extraction.

### Spam Detection

Messages may contain unwanted markup or repeated whitespace.

```text
Original: "<b>WIN NOW!!!</b>   CLAIM YOUR PRIZE"
Cleaned:  "win now claim your prize"
```

Keep in mind that repeated punctuation and capitalization can themselves be useful spam indicators. Removing them may reduce predictive information.

### Search Engines

Standardizing text can help match queries and documents that differ only in capitalization or spacing.

### Chatbots

Cleaning can help prepare user messages for tokenization and other language-processing operations.

## 8. Common Mistakes

- **Removing all punctuation without checking its meaning:** This can damage URLs, contractions, decimals, and identifiers.
- **Removing all numbers:** This can discard important dates, prices, and quantities.
- **Using regex as a complete HTML parser:** Nested markup and malformed HTML require more robust handling.
- **Applying lowercasing to every task:** Some applications depend on capitalization.
- **Confusing cleaning with tokenization:** Cleaning modifies text; tokenization divides it into tokens.
- **Removing stop words automatically:** Words such as `not` can be important for sentiment and meaning.
- **Ignoring the order of operations:** Cleaning steps can affect one another.
- **Assuming more cleaning is always better:** Excessive cleaning can remove information needed by the model.

## 9. Exercises

Try to solve these exercises yourself before checking the output.

### Exercise 1: Basic Cleaning

Input:

```text
"HELLO!!!   Welcome   to Python."
```

Tasks:

1. Convert the text to lowercase.
2. Replace punctuation with spaces.
3. Normalize whitespace.

Expected output:

```text
hello welcome to python
```

### Exercise 2: HTML Tags

Input:

```text
"<h1>Machine Learning</h1> is interesting!"
```

Remove the simple HTML tags and normalize the text.

Expected output:

```text
Machine Learning is interesting!
```

### Exercise 3: Numbers

Input:

```text
"I bought 2 books for 500 rupees."
```

Create two versions:

- Version A: Preserve all numbers.
- Version B: Remove digit sequences.

Compare the outputs and explain which version is more suitable for a price-analysis task.

### Exercise 4: Apostrophes

Input:

```text
"I don't think it's difficult."
```

Create one version that preserves apostrophes and another that replaces punctuation with spaces.

Explain how the meaning or tokenization may differ.

### Exercise 5: Build a Reusable Function

Write a `clean_text()` function that:

- Accepts a string as input.
- Removes simple HTML tags.
- Converts text to lowercase.
- Replaces punctuation with spaces.
- Normalizes whitespace.
- Returns the cleaned text.

Test your function on at least five different sentences.

### Exercise 6: Experiment With Cleaning

Run the same text through the pipeline with and without lowercasing.

Compare the outputs and explain when capitalization could be useful.

## 10. Files and Exercises

This folder contains the following learning resources:

- **`Text_Cleaning.py`** — A reusable cleaning function with a short practical example.
- **`Text_Cleaning.ipynb`** — Step-by-step explanations, executable code cells, output examples, and exercises.

Run the Python script to test the cleaning function. Use the notebook to experiment with individual cleaning operations and compare their results.

## 11. Related Topics

Continue learning with the following topics:

- [Tokenization](../../03_Tokenization/) — Splitting text into words or other tokens.
- [Stop-Word Removal](../../04_Stop_Words_Stemming_and_Lemmatization/01_Stop_Word_Removal/) — Removing selected common words when appropriate.
- [Bag of Words](../../../02_Text_Representation/01_Bag_of_Words/) — Representing text using word-frequency features.
- [Regex Example in the Existing Pipeline](../../../02_Text_Representation/01_Bag_of_Words/Bag_of_words.py) — Exploring regular expressions in an existing Bag of Words implementation.

The existing repository demonstrates basic text cleaning inside a Bag of Words pipeline. This folder provides a focused study version so that each cleaning operation can be understood and tested independently.

## 12. Points to Remember

- Text cleaning is a preprocessing step in NLP.
- The goal is to standardize text without losing useful information.
- Lowercasing, markup removal, punctuation handling, and whitespace normalization are common operations.
- Numbers and apostrophes should be handled according to the task.
- Regex is useful for simple text transformations but has limitations.
- Cleaning should be followed by appropriate preprocessing and feature extraction.
- Always inspect the cleaned output before using it for machine learning.

**Final takeaway:** Good text cleaning is not about removing everything unusual. It is about preparing text in a consistent format while preserving the information that matters for the problem.
