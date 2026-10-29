# 01 Basics and Cleaning

## 1. Introduction to Natural Language Processing (NLP)

### 1.1 What Is Natural Language Processing?

**Natural Language Processing (NLP)** is a field of Artificial Intelligence (AI) that enables computers to process, analyze, understand, and generate human language.

Humans communicate using languages such as English, Hindi, and Urdu. Computers work with numerical representations of data. NLP bridges this gap by converting language into representations that computers can process.

For example, when you type:

> I love learning Python.

An NLP system can split the sentence into words, identify important terms, analyze its sentiment, or use it as input for a chatbot.

NLP combines ideas from several fields:

- Artificial Intelligence (AI)
- Machine Learning (ML)
- Deep Learning
- Linguistics
- Statistics
- Computer Science

The goal of NLP is to make interactions between humans and computers more natural and useful.

### 1.2 Why Do We Need NLP?

People generate large amounts of text through messages, emails, reviews, documents, social media posts, and online searches.

Manually analyzing all this information can be time-consuming. NLP helps computers process language data efficiently.

Applications include:

- Email services identifying spam.
- Chatbots processing questions and generating responses.
- Search engines retrieving relevant information.
- Businesses analyzing customer reviews.
- Translation systems converting text between languages.
- Voice assistants processing spoken commands.

### 1.3 How Does NLP Work?

An NLP system generally follows several stages. The exact workflow depends on the task and the model being used.

```text
Human Language
      |
      v
Text or Speech Input
      |
      v
Preprocessing
      |
      v
Text Representation
      |
      v
NLP Model or Algorithm
      |
      v
Prediction or Language Output
```

**Step 1: Input**

The system receives language data, such as a sentence, document, message, or speech transcript.

Example:

`The movie was very good!`

**Step 2: Preprocessing**

The text may be cleaned, normalized, and divided into smaller units.

Original text:

`The Movie was very good!!!`

Normalized text:

`the movie was very good`

**Step 3: Text Representation**

The text is converted into a numerical representation that a machine learning algorithm or language model can process.

Common techniques include:

- Bag of Words (BoW)
- Term Frequency–Inverse Document Frequency (TF-IDF)
- Word embeddings such as Word2Vec
- Contextual embeddings used by transformer models

**Step 4: Analysis or Prediction**

The system performs a task such as sentiment analysis, text classification, translation, or question answering.

**Step 5: Output**

The system produces a result, such as a sentiment label, translated sentence, ranked search result, or generated response.

Modern transformer-based models may combine several of these stages internally rather than following a fixed, separate pipeline.

### 1.4 Types of Language Data

#### Text Data

Text data includes written language, such as:

- Emails
- News articles
- Product reviews
- Social media comments
- Books and documents
- Chat messages

#### Speech and Spoken Language

Spoken-language systems often combine NLP with speech technologies.

Examples include:

- Voice assistants
- Speech-to-text applications
- Voice-based chatbots
- Spoken-language translation

Speech recognition converts audio into text. NLP can then analyze the recognized words or generate a response.

### 1.5 Major Applications of NLP

#### 1. Chatbots and Virtual Assistants

Chatbots process user messages and generate relevant responses.

Example:

`How can I reset my password?`

A chatbot can recognize the user's intent and provide appropriate instructions.

#### 2. Sentiment Analysis

Sentiment analysis identifies the opinion or emotional polarity expressed in text.

Example:

`The product quality is excellent.`

Possible result: **Positive sentiment**

Common sentiment categories include positive, negative, and neutral.

#### 3. Machine Translation

Machine translation converts text from one language into another.

Example:

- English: `How are you?`
- Hindi: `आप कैसे हैं?`

Translation systems must account for vocabulary, grammar, context, and differences between languages.

#### 4. Spam Detection

Spam detection classifies messages as spam or legitimate.

Example:

`Congratulations! You have won a free prize. Click here now!`

An email classifier may identify this message as suspicious based on learned patterns and other signals.

#### 5. Search Engines

Search engines process user queries and retrieve relevant information from large collections of documents.

Example query:

`best beginner Python tutorials`

A search system analyzes the query and ranks relevant pages.

#### 6. Text Summarization

Text summarization produces a shorter version of a document while preserving its main information.

For example, a long news article can be summarized into a few key points.

#### 7. Named Entity Recognition (NER)

Named Entity Recognition identifies entities such as people, organizations, locations, and dates.

Example:

`Microsoft opened a new office in London in 2025.`

Identified entities:

- Microsoft — Organization
- London — Location
- 2025 — Date or year

#### 8. Question Answering

Question-answering systems use a question and available information to produce an answer.

Example:

- Question: `What is the capital of France?`
- Answer: `Paris.`

The quality of the answer depends on the system, its available information, and the task.

### 1.6 Important NLP Tasks

| NLP Task | Purpose | Example |
|---|---|---|
| Tokenization | Splits text into smaller units | Sentence into words |
| Text Cleaning | Removes unwanted text elements | Removing HTML tags |
| Stop-Word Removal | Removes selected common words | Removing `the` or `is` |
| Stemming | Reduces words using simple rules | `playing` to `play` |
| Lemmatization | Converts words to dictionary forms | `cars` to `car` |
| Text Classification | Assigns categories to text | Spam or not spam |
| Sentiment Analysis | Identifies sentiment | Positive or negative review |
| Named Entity Recognition | Identifies named entities | Person, place, organization |
| Machine Translation | Translates between languages | English to Hindi |
| Text Summarization | Shortens text while preserving key ideas | Article summary |
| Language Modeling | Predicts or generates language sequences | Predicting the next token |

These tasks solve different language-processing problems.

### 1.7 NLP vs. AI vs. Machine Learning vs. Deep Learning

| Concept | Meaning | Example |
|---|---|---|
| Artificial Intelligence | Broad field focused on intelligent systems | A system that solves problems |
| Machine Learning | Methods that learn patterns from data | Spam classifier trained on emails |
| Deep Learning | Machine learning using multilayer neural networks | Transformer language model |
| NLP | Field focused on processing human language | Sentiment analysis or translation |

Their relationship can be summarized as follows:

- AI is the broader field.
- Machine learning is one approach within AI.
- Deep learning is a subset of machine learning.
- NLP is a language-focused field that can use rule-based methods, machine learning, deep learning, or a combination of these approaches.

NLP and machine learning overlap, but NLP is not limited to machine learning.

### 1.8 Rule-Based NLP vs. Machine Learning-Based NLP

#### Rule-Based Approach

A rule-based system follows explicitly written rules.

For example, a simple system might flag a message if it contains a specific phrase.

**Advantages:**

- Easy to understand for simple tasks.
- Predictable behavior.
- Does not require training data for manually written rules.

**Limitations:**

- Rules must be created and maintained.
- Difficult to cover every language variation.
- May fail when wording or context changes.

#### Machine Learning-Based Approach

A machine learning system learns patterns from examples.

For example, a spam classifier can learn from messages labeled as spam or legitimate.

**Advantages:**

- Can learn complex patterns from data.
- Can generalize to examples not seen during training.
- Can be improved using suitable training data and evaluation.

**Limitations:**

- Requires suitable data and evaluation.
- Can learn biases present in the data.
- Predictions may be difficult to explain.

Modern NLP frequently uses deep learning, including transformer architectures, for complex language tasks.

### 1.9 Challenges in NLP

Human language is complex. The same word or sentence can have different meanings depending on context.

#### Ambiguity

A word or sentence may have multiple meanings.

Example:

`I saw a bat.`

The word `bat` may refer to an animal or a piece of sports equipment.

#### Context

The meaning of a word can depend on surrounding words.

- `The bank approved my loan.`
- `We sat beside the river bank.`

The word `bank` has different meanings in these sentences.

#### Sarcasm

A sentence may express the opposite of its literal meaning.

Example:

`Great! My laptop crashed again.`

A simple keyword-based system may interpret `Great` as positive even though the overall sentiment is negative.

#### Spelling and Grammar Errors

Users often type informal or incorrect text.

Examples:

- `I luv python`
- `How r u?`
- `This product are good`

NLP systems may need normalization or models that can handle these variations.

#### Multilingual Text

Different languages have different writing systems, grammatical rules, word boundaries, and vocabulary. Some languages combine several meaningful parts into a single written word, making tokenization more difficult.

#### Idioms and Expressions

The meaning of an expression may not be clear from its individual words.

Example:

`It's raining cats and dogs.`

This usually means that it is raining heavily.

#### Bias and Data Quality

NLP models learn from data. Biased, incomplete, or noisy data can lead to unreliable or unfair results. Careful data collection, evaluation, and monitoring are important.

### 1.10 First NLP Example Using Python

We can begin with basic Python string operations before using specialized NLP libraries.

```python
## Introduction to NLP

text = "Natural Language Processing is interesting."

print("Original Text:", text)

## Convert text to lowercase
lowercase_text = text.lower()
print("Lowercase Text:", lowercase_text)

## Count characters
print("Number of Characters:", len(text))

## Split text into words
words = lowercase_text.split()
print("Words:", words)

## Count words
print("Number of Words:", len(words))

## Count occurrences of a word
word = "language"
print("Occurrences of 'language':", words.count(word))

## Check whether a word exists
search_word = "processing"

if search_word in words:
    print(search_word, "is present in the text.")
else:
    print(search_word, "is not present in the text.")
```

**Explanation:**

- `lower()` converts uppercase letters to lowercase.
- `len()` counts characters in a string or items in a list.
- `split()` separates text using whitespace by default.
- `count()` counts matching items.
- The `in` operator checks membership.

These are basic string-processing operations, not a complete NLP pipeline. Dedicated tokenizers and NLP libraries provide additional capabilities for advanced text processing.

### 1.11 Sentiment Analysis Example

An online store may receive thousands of product reviews.

| Review | Possible Sentiment |
|---|---|
| The product is excellent and easy to use. | Positive |
| The product is broken and disappointing. | Negative |
| The product arrived yesterday. | Neutral |

A real model would require suitable training examples and evaluation. The labels can depend on annotation rules and context.

Businesses can use sentiment analysis to identify customer satisfaction patterns and investigate common complaints.

### 1.12 NLP Libraries and Tools

| Library or Tool | Main Purpose |
|---|---|
| NLTK | Tokenization, stop words, stemming, and educational NLP tasks |
| spaCy | Efficient linguistic processing and named entity recognition |
| scikit-learn | Text vectorization and traditional machine learning |
| Gensim | Topic modeling and word-vector workflows |
| Transformers | Pretrained transformer models for many NLP tasks |
| pandas | Data loading, cleaning, and analysis |
| NumPy | Numerical operations and arrays |

Choose a library according to the task. Not every library is required for every NLP project.

---

## 2. Text Cleaning

Text Cleaning is an important preprocessing step in Natural Language Processing (NLP). It involves removing unwanted elements, correcting inconsistencies, and standardizing raw text before further analysis.

Text collected from websites, social media, documents, and user inputs may contain HTML tags, unnecessary punctuation, extra spaces, inconsistent capitalization, and other elements that can affect text processing.

The main goal is to prepare text in a consistent and useful format while preserving the information required for the task.

### 2.1 Why Is Text Cleaning Important?

Consider the following example.

**Original text:**

```text
<HTML><body>  HELLO!!!   I am Learning NLP. </body></HTML>
```

**After cleaning:**

```text
hello i am learning nlp
```

Text cleaning helps to:

- Remove unnecessary HTML tags and markup.
- Standardize uppercase and lowercase characters.
- Handle punctuation according to the task.
- Remove unnecessary spaces and line breaks.
- Prepare text for tokenization and feature extraction.
- Reduce unwanted variations in text data.

Cleaning should not remove meaningful information. The correct process depends on the dataset and the problem being solved.

### 2.2 Common Text Cleaning Operations

#### 2.2.1 Lowercasing

Lowercasing converts all uppercase letters into lowercase letters.

**Example:**

```text
Original:  Machine Learning Is Interesting
Cleaned:   machine learning is interesting
```

**Python:**

```python
text = "Machine Learning Is Interesting"

cleaned_text = text.lower()

print(cleaned_text)
```

**Output:**

```text
machine learning is interesting
```

Lowercasing helps reduce differences caused by capitalization. Without it, some text-processing methods may treat `Python`, `PYTHON`, and `python` as different tokens.

However, capitalization may carry useful information in tasks involving named entities, acronyms, or case-sensitive data.

#### 2.2.2 Removing HTML Tags

Text collected from websites may contain HTML elements such as `<p>`, `<div>`, and `<b>`.

**Example:**

```text
Original:  <p>Welcome to <b>NLP</b></p>
Cleaned:   Welcome to NLP
```

**Python:**

```python
import re

text = "<p>Welcome to <b>NLP</b></p>"

cleaned_text = re.sub(r"<[^>]+>", "", text)

print(cleaned_text)
```

**Output:**

```text
Welcome to NLP
```

The regular expression `r"<[^>]+>"` matches simple strings that resemble HTML tags.

Regular expressions are suitable for simple demonstrations but are not complete HTML parsers. For complex or malformed HTML, a dedicated HTML parser such as Beautiful Soup is more appropriate.

#### 2.2.3 Removing or Replacing Punctuation

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

**Python:**

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

**Output:**

```text
Hello    How are you 
```

The output still contains extra spaces, which can be handled through whitespace normalization.

Replacing punctuation with spaces can prevent unrelated words from being joined accidentally.

```text
Original:  data-driven
Deleting:  datadriven
Replacing: data driven
```

However, punctuation may be meaningful in URLs, programming languages, financial data, and sentiment analysis. The method should depend on the application.

#### 2.2.4 Normalizing Whitespace

Raw text may contain multiple spaces, tabs, and newline characters.

**Example:**

```text
Original:  "Python    is\n\n easy"
Cleaned:   "Python is easy"
```

**Python:**

```python
import re

text = "Python    is\n\n easy"

cleaned_text = re.sub(r"\s+", " ", text).strip()

print(cleaned_text)
```

**Output:**

```text
Python is easy
```

**Explanation:**

- `\s+` matches one or more whitespace characters.
- `re.sub()` replaces matching sequences with a single space.
- `.strip()` removes whitespace from the beginning and end.

Whitespace normalization makes text more consistent and readable.

#### 2.2.5 Handling Numbers

Numbers may or may not be important in an NLP task.

**Example:**

```text
Original: I bought 3 books for ₹500.
```

Possible outputs:

```text
Keep numbers:   I bought 3 books for ₹500.
Remove numbers: I bought books for ₹.
```

Removing digits blindly can destroy useful information, such as prices, ages, dates, ratings, and quantities.

If numbers need to be removed, define a rule that considers the data and the intended analysis.

#### 2.2.6 Handling Apostrophes and Contractions

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

### 2.3 Complete Text Cleaning Example

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

### 2.4 Understanding Regular Expressions

Regular expressions, commonly called **regex**, are patterns used to search for and manipulate text.

| Pattern | Meaning |
|---|---|
| `r"<[^>]+>"` | Matches simple HTML-like tags |
| `r"\s+"` | Matches one or more whitespace characters |
| `r"\d+"` | Matches one or more digits |
| `r"[A-Za-z]+"` | Matches sequences of English letters |
| `r"[^\w\s]"` | Matches characters that are neither word characters nor whitespace |

**Example:**

```python
import re

text = "Python   123   NLP"

print(re.sub(r"\s+", " ", text))
print(re.sub(r"\d+", "", text))
```

**Output:**

```text
Python 123 NLP
Python    NLP
```

Removing digits can leave extra spaces. A complete cleaning pipeline should normalize whitespace after operations that may introduce it.

### 2.5 Text Cleaning Before and After

| Operation | Before | After |
|---|---|---|
| Lowercasing | `HELLO World` | `hello world` |
| HTML removal | `<b>Python</b>` | `Python` |
| Punctuation replacement | `Hello!!!` | `Hello` |
| Whitespace normalization | `NLP   is easy` | `NLP is easy` |
| Digit removal, when required | `Python 3` | `Python` |

The order of operations matters because one operation may change the input for the next operation.

### 2.6 Text Cleaning in an NLP Pipeline

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

### 2.7 Practical Applications of Text Cleaning

#### Sentiment Analysis

Reviews often contain inconsistent capitalization, punctuation, and spacing.

```text
Original: "THIS PRODUCT IS AMAZING!!!"
Cleaned:  "this product is amazing"
```

Cleaning can make text more consistent before feature extraction.

#### Spam Detection

Messages may contain unwanted markup or repeated whitespace.

```text
Original: "<b>WIN NOW!!!</b>   CLAIM YOUR PRIZE"
Cleaned:  "win now claim your prize"
```

Repeated punctuation and capitalization can themselves be useful spam indicators. Removing them may reduce predictive information.

#### Search Engines

Standardizing text can help match queries and documents that differ only in capitalization or spacing.

#### Chatbots

Cleaning can help prepare user messages for tokenization and other language-processing operations.

### 2.8 Key Points About Text Cleaning

- Text cleaning is a preprocessing step in NLP.
- The goal is to standardize text without losing useful information.
- Lowercasing, markup removal, punctuation handling, and whitespace normalization are common operations.
- Numbers and apostrophes should be handled according to the task.
- Regex is useful for simple text transformations but has limitations.
- Cleaning should be followed by appropriate preprocessing and feature extraction.
- Always inspect the cleaned output before using it for machine learning.

**Main idea:** Good text cleaning is not about removing everything unusual. It is about preparing text in a consistent format while preserving the information that matters for the problem.

---

## 3. Text Normalization in NLP

### 3.1 Introduction

**Text Normalization** is the process of converting text into a consistent and standardized form so that different variations of the same word or expression can be handled more consistently by an NLP system.

For example:

- `HELLO WORLD`
- `Hello World`
- `hello world`

Normalization can convert these variations into:

`hello world`

Text normalization helps reduce unnecessary variations in text and can make downstream text processing more effective.

It is commonly used in text classification, sentiment analysis, search engines, chatbots, and other NLP applications.

### 3.2 Why Is Text Normalization Important?

Consider these examples:

| Original Text | Normalized Text |
|---|---|
| `HELLO PYTHON` | `hello python` |
| `  natural   language  ` | `natural language` |
| `I don't know` | `i do not know` |
| `Python!!!` | `python!!!` |
| `u r gr8` | `you are great` |

These transformations use different techniques. Not every normalization pipeline performs all of them, and punctuation is intentionally retained in the fourth example.

Without suitable normalization, the same expression may appear in multiple forms, increasing vocabulary variation and making comparisons more difficult.

For example, a simple word-counting system may treat `Python` and `python` as different tokens unless it normalizes case or uses a case-insensitive approach.

### 3.3 Common Text Normalization Techniques

#### 3.3.1 Lowercasing

Lowercasing converts uppercase letters to lowercase.

**Example:**

```text
Original:   Natural Language Processing Is Interesting
Normalized: natural language processing is interesting
```

**Python:**

```python
text = "Natural Language Processing Is Interesting"

normalized_text = text.lower()

print(normalized_text)
```

**Output:**

```text
natural language processing is interesting
```

Lowercasing:

- Reduces differences caused by capitalization.
- Helps combine words such as `Python` and `python`.
- Can reduce the number of distinct tokens in a vocabulary.

However, capitalization can carry meaning. For example, `apple` may refer to a fruit, while `Apple` may refer to a company. Lowercasing should depend on the task.

#### 3.3.2 Uppercasing

Uppercasing converts letters to uppercase.

**Example:**

```text
natural language processing
→
NATURAL LANGUAGE PROCESSING
```

**Python:**

```python
text = "natural language processing"

normalized_text = text.upper()

print(normalized_text)
```

**Output:**

```text
NATURAL LANGUAGE PROCESSING
```

Uppercasing is useful for some text-matching tasks, but lowercasing is more common in traditional text-processing pipelines.

#### 3.3.3 Whitespace Normalization

Text may contain extra spaces, tabs, or newline characters.

**Original:**

```text
"   Natural    Language \n Processing   "
```

**Normalized:**

```text
"Natural Language Processing"
```

**Python:**

```python
import re

text = "   Natural    Language \n Processing   "

normalized_text = re.sub(r"\s+", " ", text).strip()

print(normalized_text)
```

**Output:**

```text
Natural Language Processing
```

**Explanation:**

- `\s+` matches one or more whitespace characters.
- `re.sub()` replaces matching sequences with a single space.
- `strip()` removes whitespace at the beginning and end.

Whitespace normalization is useful when text comes from copied documents, web pages, or inconsistent user input.

#### 3.3.4 Contraction Expansion

A contraction is a shortened form of two or more words.

Examples:

- `don't` → `do not`
- `can't` → `cannot`
- `I'm` → `I am`
- `they're` → `they are`
- `it's` → `it is` or `it has`, depending on context

**Python:**

```python
text = "I don't know why they're waiting."

text = text.replace("don't", "do not")
text = text.replace("they're", "they are")

print(text)
```

**Output:**

```text
I do not know why they are waiting.
```

Simple replacements are suitable for selected examples, but they do not handle every contraction or contextual ambiguity. Larger datasets may require a dedicated normalization tool or carefully designed rules.

#### 3.3.5 Standardizing Informal Language

Informal text often contains abbreviations, slang, and shortened expressions.

| Informal Form | Standardized Form |
|---|---|
| `u` | `you` |
| `r` | `are` |
| `gr8` | `great` |
| `pls` | `please` |
| `thx` | `thanks` |

**Python:**

```python
text = "u r gr8"

normalization_map = {
    "u": "you",
    "r": "are",
    "gr8": "great"
}

words = text.split()

normalized_words = [
    normalization_map.get(word, word)
    for word in words
]

normalized_text = " ".join(normalized_words)

print(normalized_text)
```

**Output:**

```text
you are great
```

This approach uses a dictionary to map known informal expressions to standard forms.

Informal expressions can have multiple meanings, so replacements should be applied carefully.

#### 3.3.6 Unicode Normalization

Unicode allows some characters to be represented in more than one underlying way. For example, an accented character can be represented as a single character or as a base character followed by a combining accent.

Unicode normalization standardizes these representations.

**Python:**

```python
import unicodedata

text = "café"

normalized_text = unicodedata.normalize("NFC", text)

print(normalized_text)
```

**Output:**

```text
café
```

Common Unicode normalization forms include:

- **NFC:** Combines characters into canonical composed forms where possible.
- **NFD:** Decomposes characters into canonical forms.
- **NFKC:** Applies compatibility normalization and may combine characters considered compatibility-equivalent.
- **NFKD:** Applies compatibility decomposition.

Compatibility normalization can change the representation of some characters, so choose the form based on your data and application.

#### 3.3.7 Spelling Normalization

Spelling normalization standardizes selected spelling variations or corrects misspellings.

Examples:

- `teh` → `the`
- `recieve` → `receive`

These transformations usually require a dictionary, spelling-correction library, or context-aware method.

Automatic correction should be used carefully because names, technical terms, abbreviations, and regional spellings may otherwise be changed incorrectly.

#### 3.3.8 Repeated Character Normalization

Informal messages sometimes contain repeated characters for emphasis.

Examples:

- `soooo good` → `soo good`
- `heyyyy` → `heyy`

A regular expression can reduce repeated characters.

```python
import re

text = "This is sooo good!!!"

normalized_text = re.sub(r"(.)\1{2,}", r"\1\1", text)

print(normalized_text)
```

**Output:**

```text
This is soo good!!
```

This expression limits sequences of three or more identical characters to two. Such rules can be useful for informal text but may damage meaningful spellings, names, or intentional expressions if applied indiscriminately.

### 3.4 Text Normalization vs. Text Cleaning

Text normalization and text cleaning are related, but their primary purposes differ.

| Feature | Text Cleaning | Text Normalization |
|---|---|---|
| Main purpose | Remove unwanted or noisy content | Standardize text representations |
| Typical operations | Remove HTML tags, unwanted symbols, or irrelevant markup | Lowercasing, whitespace standardization, contraction expansion |
| Example | `<p>Hello</p>` → `Hello` | `HELLO` → `hello` |
| Main goal | Improve the quality of input text | Improve consistency of text |
| Overlap | May include standardization | May include cleaning-like transformations |

The distinction is not absolute. Different courses, libraries, and projects may classify some operations differently.

For example, removing punctuation may be considered text cleaning, but it is not always part of normalization.

### 3.5 Text Normalization vs. Tokenization

**Normalization** standardizes text, while **tokenization** splits text into smaller units such as words or sentences.

**Original text:**

```text
"HELLO    WORLD!"
```

**After normalization:**

```text
"hello world!"
```

**After word tokenization:**

```python
["hello", "world", "!"]
```

The exact tokens depend on the tokenizer used.

Normalization and tokenization are separate operations, although they are often used together in a text preprocessing pipeline.

### 3.6 Text Normalization vs. Stemming and Lemmatization

Stemming and lemmatization are commonly taught alongside text normalization because they reduce variations in word forms.

#### Stemming

Stemming uses rules to reduce words to stems, which may not be valid dictionary words.

Examples:

- `playing` → `play`
- `connected` → `connect`
- `studies` → `studi` with some stemming algorithms

The result depends on the algorithm.

#### Lemmatization

Lemmatization uses vocabulary and linguistic information to return a word's dictionary form, called a lemma.

Examples:

- `running` → `run`
- `cars` → `car`
- `better` → `good` when the word is analyzed as an adjective in the appropriate context

Lemmatization may require part-of-speech information for the correct result.

**Comparison:**

| Technique | Purpose | Example |
|---|---|---|
| Lowercasing | Standardizes capitalization | `HELLO` → `hello` |
| Whitespace normalization | Standardizes spacing | Multiple spaces → one space |
| Stemming | Reduces words using rules | `studies` → `studi` |
| Lemmatization | Finds a dictionary form | `cars` → `car` |
| Tokenization | Splits text into units | Sentence → word tokens |

### 3.7 Complete Text Normalization Pipeline in Python

The following example combines lowercasing, contraction expansion, whitespace normalization, Unicode normalization, and selected informal-word replacements.

```python
## Text Normalization

import re
import unicodedata

text = "   HELLO!!!   I don't know   why u r waiting.   "

print("Original Text:", repr(text))

## Apply Unicode normalization
text = unicodedata.normalize("NFC", text)

## Convert text to lowercase
text = text.lower()

## Expand selected contractions
text = text.replace("don't", "do not")

## Standardize selected informal words
normalization_map = {
    "u": "you",
    "r": "are"
}

words = text.split()

normalized_words = [
    normalization_map.get(word, word)
    for word in words
]

text = " ".join(normalized_words)

## Normalize whitespace
text = re.sub(r"\s+", " ", text).strip()

print("Normalized Text:", text)
```

**Output:**

```text
Original Text: "   HELLO!!!   I don't know   why u r waiting.   "
Normalized Text: hello!!! i do not know why you are waiting.
```

**Explanation:**

1. Unicode normalization standardizes compatible character representations.
2. Lowercasing makes capitalization consistent.
3. Contraction expansion replaces a selected shortened expression.
4. Dictionary-based replacements standardize selected informal words.
5. Whitespace normalization removes unnecessary spacing.

This pipeline deliberately keeps punctuation. Additional cleaning steps should be added only when the task requires them.

### 3.8 Applications of Text Normalization

#### Search Engines

Normalization helps a search system match queries and documents with consistent representations.

#### Sentiment Analysis

Lowercasing and selected text standardization can reduce variation in review text. However, punctuation and capitalization may express emotion and should sometimes be preserved.

#### Chatbots

Normalization can help standardize informal user messages before intent classification or other processing.

#### Text Classification

Consistent text representations can reduce unnecessary vocabulary variation and make model features more consistent.

#### Social Media Analysis

Normalization can help process abbreviations, repeated characters, inconsistent spacing, and informal expressions.

#### Information Retrieval

Normalization can improve matching between a query and documents when they contain equivalent textual forms.

### 3.9 Key Points About Text Normalization

- Text normalization converts text into a consistent representation.
- Lowercasing and whitespace normalization are common techniques.
- Contraction expansion and informal-word standardization require suitable rules or tools.
- Unicode normalization handles different representations of Unicode text.
- Spelling correction and repeated-character normalization should be applied carefully.
- Normalization is related to text cleaning, but the two terms are not identical.
- Tokenization splits text into units; normalization standardizes text.
- Stemming and lemmatization reduce word-form variations.
- Not every normalization technique is appropriate for every NLP task.
- Preprocessing rules should be consistent between training and inference.