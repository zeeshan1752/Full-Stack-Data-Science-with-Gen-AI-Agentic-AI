# 01 Basics and Cleaning

---

## Introduction to Natural Language Processing (NLP)

### 1. What Is Natural Language Processing?

**Natural Language Processing (NLP)** is a field of Artificial Intelligence (AI) that enables computers to process, analyze, understand, and generate human language.

Humans communicate using languages such as English, Hindi, Urdu, and many others. Computers, however, work with numerical representations of data. NLP helps bridge this gap by converting language into representations that computers can process.

For example, when you type:

> I love learning Python.

An NLP system can split the sentence into words, identify important terms, analyze its sentiment, or use the sentence as input for a chatbot.

NLP combines ideas from several fields:

- Artificial Intelligence (AI)
- Machine Learning (ML)
- Deep Learning
- Linguistics
- Statistics
- Computer Science

The goal of NLP is to make interactions between humans and computers more natural and useful.

### 2. Why Do We Need NLP?

Every day, people generate large amounts of text through messages, emails, reviews, documents, social media posts, and online searches.

Manually analyzing all this information can be time-consuming. NLP helps computers process language data efficiently.

For example:

- Email services use NLP techniques to identify spam.
- Chatbots process questions and generate responses.
- Search engines analyze queries to retrieve relevant information.
- Businesses analyze customer reviews to understand opinions.
- Translation systems convert text from one language into another.
- Voice assistants process language to respond to spoken commands.

Without NLP, computers would have difficulty processing human language in a useful, automated way.

### 3. How Does NLP Work?

An NLP system generally follows several stages. The exact workflow depends on the task and the model being used.

<pre>
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
</pre>

#### Step 1: Input

The system receives language data, such as a sentence, document, message, or speech transcript.

Example:

`The movie was very good!`

#### Step 2: Preprocessing

The text may be cleaned, normalized, and divided into smaller units.

Example:

Original text:

`The Movie was very good!!!`

Normalized text:

`the movie was very good`

#### Step 3: Text Representation

The text is converted into a numerical representation that a machine learning algorithm or language model can process.

Common techniques include:

- Bag of Words
- TF-IDF
- Word embeddings such as Word2Vec
- Contextual embeddings used by transformer models

#### Step 4: Analysis or Prediction

The system performs a task such as sentiment analysis, text classification, translation, or question answering.

#### Step 5: Output

The system produces a result, such as a sentiment label, translated sentence, ranked search result, or generated response.

**Important:** Modern transformer-based models may combine several of these stages internally rather than following a fixed, separate pipeline.

### 4. Types of Language Data

NLP can work with different forms of language data.

#### 4.1 Text Data

Text data includes written language.

Examples:

- Emails
- News articles
- Product reviews
- Social media comments
- Books and documents
- Chat messages

#### 4.2 Speech and Spoken Language

Spoken-language systems often combine NLP with speech technologies.

Examples:

- Voice assistants
- Speech-to-text applications
- Voice-based chatbots
- Spoken-language translation

Speech recognition converts audio into text. NLP can then analyze the recognized words or generate a response.

### 5. Major Applications of NLP

#### 5.1 Chatbots and Virtual Assistants

Chatbots process user messages and generate relevant responses.

Examples include customer support bots and conversational assistants.

User:

`How can I reset my password?`

A chatbot can recognize the user's intent and provide the appropriate instructions.

#### 5.2 Sentiment Analysis

Sentiment analysis identifies the opinion or emotional polarity expressed in text.

Example:

`The product quality is excellent.`

Possible result: **Positive sentiment**

Common sentiment categories include positive, negative, and neutral.

#### 5.3 Machine Translation

Machine translation converts text from one language into another.

Example:

English: `How are you?`

Hindi: `आप कैसे हैं?`

Translation systems must account for vocabulary, grammar, context, and differences between languages.

#### 5.4 Spam Detection

Spam detection classifies messages as spam or legitimate.

Example:

`Congratulations! You have won a free prize. Click here now!`

An email classifier may identify this message as suspicious based on learned patterns and other signals.

#### 5.5 Search Engines

Search engines process user queries and retrieve relevant information from large collections of documents.

Query:

`best beginner Python tutorials`

A search system analyzes the query and ranks relevant pages.

#### 5.6 Text Summarization

Text summarization produces a shorter version of a document while preserving its main information.

For example, a long news article can be summarized into a few key points.

#### 5.7 Named Entity Recognition (NER)

Named Entity Recognition identifies entities such as people, organizations, locations, and dates.

Example:

`Microsoft opened a new office in London in 2025.`

Possible entities:

- Microsoft — Organization
- London — Location
- 2025 — Date or year

#### 5.8 Question Answering

Question-answering systems use a question and available information to produce an answer.

Example:

Question: `What is the capital of France?`

Answer: `Paris.`

The quality of the answer depends on the system, its available information, and the task.

### 6. Important NLP Tasks

| NLP Task | Purpose | Example |
|---|---|---|
| Tokenization | Splits text into smaller units | Sentence into words |
| Text Cleaning | Removes unwanted text elements | Removing HTML tags |
| Stop-Word Removal | Removes selected common words | Removing `the` or `is` |
| Stemming | Reduces words using simple rules | `playing` to `play` |
| Lemmatization | Converts words to dictionary forms | `better` to `good` in the appropriate context |
| Text Classification | Assigns categories to text | Spam or not spam |
| Sentiment Analysis | Identifies sentiment | Positive or negative review |
| Named Entity Recognition | Identifies named entities | Person, place, organization |
| Machine Translation | Translates between languages | English to Hindi |
| Text Summarization | Shortens text while preserving key ideas | Article summary |
| Language Modeling | Predicts or generates language sequences | Predicting the next token |

These tasks are related but are not interchangeable. Each solves a different language-processing problem.

### 7. NLP vs. AI vs. Machine Learning vs. Deep Learning

These terms are related, but they do not mean the same thing.

| Concept | Meaning | Example |
|---|---|---|
| Artificial Intelligence | Broad field focused on intelligent systems | A system that solves problems |
| Machine Learning | Methods that learn patterns from data | Spam classifier trained on emails |
| Deep Learning | Machine learning using multilayer neural networks | Transformer language model |
| NLP | Field focused on processing human language | Sentiment analysis or translation |

NLP can use rule-based methods, machine learning, deep learning, or a combination of these approaches.

#### Relationship Between Them

A simplified view is:

- AI is the broader field.
- Machine learning is one approach within AI.
- Deep learning is a subset of machine learning.
- NLP is a language-focused field that can use any of these approaches.

NLP and machine learning overlap, but NLP is not limited to machine learning.

### 8. Rule-Based NLP vs. Machine Learning-Based NLP

#### Rule-Based Approach

A rule-based system follows explicitly written rules.

For example, a simple system might flag a message if it contains a specific phrase.

Advantages:

- Easy to understand for simple tasks
- Predictable behavior
- Does not require training data for manually written rules

Limitations:

- Rules must be created and maintained
- Difficult to cover every language variation
- May fail when wording or context changes

#### Machine Learning-Based Approach

A machine learning system learns patterns from examples.

For example, a spam classifier can learn from messages labeled as spam or legitimate.

Advantages:

- Can learn complex patterns from data
- Can generalize to examples not seen during training
- Can be improved using suitable training data and evaluation

Limitations:

- Requires suitable data and evaluation
- Can learn biases present in the data
- Predictions may be difficult to explain

Modern NLP frequently uses deep learning, including transformer architectures, for complex language tasks.

### 9. Challenges in NLP

Human language is complex. The same word or sentence can have different meanings depending on context.

#### 9.1 Ambiguity

A word or sentence may have multiple meanings.

Example:

`I saw a bat.`

The word `bat` may refer to an animal or a piece of sports equipment.

#### 9.2 Context

The meaning of a word can depend on the surrounding words.

Example:

- `The bank approved my loan.`
- `We sat beside the river bank.`

The word `bank` has different meanings in these sentences.

#### 9.3 Sarcasm

A sentence may express the opposite of its literal meaning.

Example:

`Great! My laptop crashed again.`

A simple keyword-based system may interpret `Great` as positive even though the overall sentiment is negative.

#### 9.4 Spelling and Grammar Errors

Users often type informal or incorrect text.

Examples:

- `I luv python`
- `How r u?`
- `This product are good`

NLP systems may need normalization or models that can handle these variations.

#### 9.5 Multilingual Text

Different languages have different writing systems, grammatical rules, word boundaries, and vocabulary.

Some languages also combine several meaningful parts into a single written word, making tokenization more difficult.

#### 9.6 Idioms and Expressions

The meaning of an expression may not be clear from its individual words.

Example:

`It's raining cats and dogs.`

This usually means that it is raining heavily, not that animals are falling from the sky.

#### 9.7 Bias and Data Quality

NLP models learn from data. Biased, incomplete, or noisy data can lead to unreliable or unfair results.

Careful data collection, evaluation, and monitoring are important.

### 10. First NLP Example Using Python

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

#### What Does This Example Teach?

- Variables store text.
- `lower()` converts uppercase letters to lowercase.
- `len()` counts characters in a string or items in a list.
- `split()` separates text using whitespace by default.
- `count()` counts matching items.
- The `in` operator checks membership.

These are basic string-processing operations, not a complete NLP pipeline. For more advanced text processing, dedicated tokenizers and NLP libraries provide additional capabilities.

### 11. A Simple Real-World Example: Sentiment Analysis

Imagine that an online store receives thousands of product reviews.

Examples:

1. `The product is excellent and easy to use.`
2. `The product is broken and disappointing.`
3. `The product arrived yesterday.`

A sentiment analysis system might classify them as:

| Review | Possible sentiment |
|---|---|
| The product is excellent and easy to use. | Positive |
| The product is broken and disappointing. | Negative |
| The product arrived yesterday. | Neutral |

A real model would need suitable examples and evaluation. These labels are illustrative and can depend on the annotation rules and context.

Businesses can use sentiment analysis to identify customer satisfaction patterns and investigate common complaints.

### 12. NLP Libraries and Tools

Several Python libraries are useful for learning and implementing NLP.

| Library or Tool | Main Purpose |
|---|---|
| NLTK | Tokenization, stop words, stemming, and educational NLP tasks |
| spaCy | Efficient linguistic processing and named entity recognition |
| scikit-learn | Text vectorization and traditional machine learning |
| Gensim | Topic modeling and word-vector workflows |
| Transformers | Pretrained transformer models for many NLP tasks |
| pandas | Data loading, cleaning, and analysis |
| NumPy | Numerical operations and arrays |

Choose the library according to the task. You do not need to install every library before starting the introductory exercises.

### 13. Learning Roadmap

A practical sequence for learning NLP is:

1. Introduction to NLP
2. Text cleaning
3. Text normalization
4. Tokenization
5. Stop-word removal
6. Stemming
7. Lemmatization
8. Regular expressions
9. Text preprocessing pipelines
10. Bag of Words
11. N-Grams
12. TF-IDF
13. Word embeddings, including Word2Vec
14. Text classification and sentiment analysis
15. Named Entity Recognition
16. Advanced NLP with transformers

Learn the basic concepts first, then practise them with Python and real text examples.

### 14. Practice Exercises

#### Beginner Level

**Exercise 1:** Create a variable containing a sentence and print it.

**Exercise 2:** Convert a sentence to lowercase.

**Exercise 3:** Count the characters in a sentence.

**Exercise 4:** Split a sentence into words and display the word list.

**Exercise 5:** Count how many times a particular word appears in a sentence.

#### Intermediate Level

**Exercise 6:** Write a program that checks whether a given word exists in a sentence.

**Exercise 7:** Compare two sentences after converting them to lowercase.

**Exercise 8:** Count the number of words in three different sentences.

**Exercise 9:** Identify the differences between a rule-based spam filter and a machine learning spam classifier.

**Exercise 10:** Find five real-world applications of NLP and explain what each one does.

#### Conceptual Questions

1. What is NLP, and why is it useful?
2. How is NLP related to artificial intelligence?
3. What is the difference between stemming and lemmatization?
4. Why is context important in language processing?
5. How does sentiment analysis work at a high level?
6. Why do NLP systems require text preprocessing in some tasks?
7. What is the difference between Bag of Words and TF-IDF?
8. Why can sarcasm be difficult for an NLP system to identify?

### 15. Common Mistakes

- Assuming NLP always requires machine learning.
- Treating text cleaning and tokenization as the same operation.
- Assuming that every common word should always be removed.
- Assuming that stemming always produces a valid dictionary word.
- Expecting a simple keyword search to understand context or sarcasm.
- Assuming that TF-IDF or Bag of Words understands the meaning of a sentence.
- Evaluating a language system only on examples it has already seen.
- Ignoring language variation, bias, and data quality.

### 16. Points to Remember

- NLP stands for Natural Language Processing.
- NLP enables computers to process and work with human language.
- It combines ideas from linguistics, computer science, statistics, and AI.
- Common applications include chatbots, translation, search, sentiment analysis, and spam detection.
- Text preprocessing can improve the suitability of text for particular tasks.
- Text representation converts language into a form that computational methods can use.
- NLP can use rule-based methods, machine learning, deep learning, or combinations of them.
- Context, ambiguity, sarcasm, and multilingual text remain important challenges.
- Understanding the basics makes it easier to learn more advanced NLP techniques.

### 17. References and Learning Resources

- [NLTK Documentation](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/usage)
- [scikit-learn: Working with Text Data](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)
- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/)
- [Stanford CS224N: Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/)

---

**Next topic:** [Text Cleaning](README.md#text-cleaning)

---

## Text Cleaning

Text Cleaning is an important preprocessing step in Natural Language Processing (NLP). It involves removing unwanted elements, correcting inconsistencies, and standardizing raw text before performing further analysis.

Text collected from websites, social media, documents, and user inputs may contain HTML tags, unnecessary punctuation, extra spaces, inconsistent capitalization, and other elements that can affect text processing.

The main goal of text cleaning is to prepare text in a consistent and useful format while preserving the information required for the task.

### 1. Why Is Text Cleaning Important?

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

### 2. Common Text Cleaning Operations

#### 2.1 Lowercasing

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

#### 2.2 Removing HTML Tags

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

#### 2.3 Removing or Replacing Punctuation

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

#### 2.4 Normalizing Whitespace

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

#### 2.5 Handling Numbers

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

#### 2.6 Handling Apostrophes and Contractions

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

### 3. Complete Text Cleaning Example

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

### 4. Understanding the Regular Expressions

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

### 5. Text Cleaning Before and After

| Operation | Before | After |
|---|---|---|
| Lowercasing | `HELLO World` | `hello world` |
| HTML removal | `<b>Python</b>` | `Python` |
| Punctuation replacement | `Hello!!!` | `Hello` |
| Whitespace normalization | `NLP   is easy` | `NLP is easy` |
| Digit removal, when required | `Python 3` | `Python` |

The examples above illustrate individual operations. Their order matters because one operation may change the input for the next operation.

### 6. Text Cleaning in an NLP Pipeline

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

### 7. Practical Applications

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

Keep in mind that repeated punctuation and capitalization can themselves be useful spam indicators. Removing them may reduce predictive information.

#### Search Engines

Standardizing text can help match queries and documents that differ only in capitalization or spacing.

#### Chatbots

Cleaning can help prepare user messages for tokenization and other language-processing operations.

### 8. Common Mistakes

- **Removing all punctuation without checking its meaning:** This can damage URLs, contractions, decimals, and identifiers.
- **Removing all numbers:** This can discard important dates, prices, and quantities.
- **Using regex as a complete HTML parser:** Nested markup and malformed HTML require more robust handling.
- **Applying lowercasing to every task:** Some applications depend on capitalization.
- **Confusing cleaning with tokenization:** Cleaning modifies text; tokenization divides it into tokens.
- **Removing stop words automatically:** Words such as `not` can be important for sentiment and meaning.
- **Ignoring the order of operations:** Cleaning steps can affect one another.
- **Assuming more cleaning is always better:** Excessive cleaning can remove information needed by the model.

### 9. Exercises

Try to solve these exercises yourself before checking the output.

#### Exercise 1: Basic Cleaning

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

#### Exercise 2: HTML Tags

Input:

```text
"<h1>Machine Learning</h1> is interesting!"
```

Remove the simple HTML tags and normalize the text.

Expected output:

```text
Machine Learning is interesting!
```

#### Exercise 3: Numbers

Input:

```text
"I bought 2 books for 500 rupees."
```

Create two versions:

- Version A: Preserve all numbers.
- Version B: Remove digit sequences.

Compare the outputs and explain which version is more suitable for a price-analysis task.

#### Exercise 4: Apostrophes

Input:

```text
"I don't think it's difficult."
```

Create one version that preserves apostrophes and another that replaces punctuation with spaces.

Explain how the meaning or tokenization may differ.

#### Exercise 5: Build a Reusable Function

Write a `clean_text()` function that:

- Accepts a string as input.
- Removes simple HTML tags.
- Converts text to lowercase.
- Replaces punctuation with spaces.
- Normalizes whitespace.
- Returns the cleaned text.

Test your function on at least five different sentences.

#### Exercise 6: Experiment With Cleaning

Run the same text through the pipeline with and without lowercasing.

Compare the outputs and explain when capitalization could be useful.

### 10. Files and Exercises

This folder contains the following learning resources:

- **`text_cleaning.py`** — A reusable cleaning function with a short practical example.
- **`Text_Cleaning.ipynb`** — Step-by-step explanations, executable code cells, output examples, and exercises.

Run the Python script to test the cleaning function. Use the notebook to experiment with individual cleaning operations and compare their results.

### 11. Related Topics

Continue learning with the following topics:

- [Tokenization](../02_Tokenization/) — Splitting text into words or other tokens.
- [Stop-Word Removal](../03_Stopwords_Stemming_Lemmatization/) — Removing selected common words when appropriate.
- [Bag of Words](../../02_Text_Representation/01_Bag_of_Words_and_NGrams/) — Representing text using word-frequency features.
- [Regex Example in the Existing Pipeline](../../02_Text_Representation/01_Bag_of_Words_and_NGrams/bag_of_words_sklearn.py) — Exploring regular expressions in an existing Bag of Words implementation.

The existing repository demonstrates basic text cleaning inside a Bag of Words pipeline. This folder provides a focused study version so that each cleaning operation can be understood and tested independently.

### 12. Points to Remember

- Text cleaning is a preprocessing step in NLP.
- The goal is to standardize text without losing useful information.
- Lowercasing, markup removal, punctuation handling, and whitespace normalization are common operations.
- Numbers and apostrophes should be handled according to the task.
- Regex is useful for simple text transformations but has limitations.
- Cleaning should be followed by appropriate preprocessing and feature extraction.
- Always inspect the cleaned output before using it for machine learning.

**Final takeaway:** Good text cleaning is not about removing everything unusual. It is about preparing text in a consistent format while preserving the information that matters for the problem.

---

## Text Normalization in NLP

### 1. Introduction

**Text Normalization** is the process of converting text into a consistent and standardized form so that different variations of the same word or expression can be handled more consistently by an NLP system.

People write the same words in different ways. For example:

- `HELLO WORLD`
- `Hello World`
- `hello world`

In many NLP tasks, these sentences have the same meaning. Normalization can convert them into a consistent representation:

`hello world`

Text normalization helps reduce unnecessary variations in text and can make downstream text processing more effective.

It is commonly used in Natural Language Processing (NLP), text classification, sentiment analysis, search engines, chatbots, and other language-processing applications.

### 2. Why Is Text Normalization Important?

Consider these examples:

| Original Text | Normalized Text |
|---|---|
| `HELLO PYTHON` | `hello python` |
| `  natural   language  ` | `natural language` |
| `I don't know` | `i do not know` |
| `Python!!!` | `python!!!` |
| `u r gr8` | `you are great` |

The transformations above use different techniques. Not every normalization pipeline performs all of them, and punctuation is intentionally retained in the fourth example.

Without suitable normalization, the same expression may appear in multiple forms, increasing vocabulary variation and making comparisons more difficult.

For example, a simple word-counting system may treat `Python` and `python` as different tokens unless it normalizes case or uses a case-insensitive approach.

### 3. Common Text Normalization Techniques

#### 3.1 Lowercasing

Lowercasing converts uppercase letters to lowercase.

Example:

Original:

`Natural Language Processing Is Interesting`

Normalized:

`natural language processing is interesting`

Python example:

```python
text = "Natural Language Processing Is Interesting"

normalized_text = text.lower()

print(normalized_text)
```

Output:

```text
natural language processing is interesting
```

**Why use it?**

- Reduces differences caused by capitalization.
- Helps combine words such as `Python` and `python`.
- Can reduce the number of distinct tokens in a vocabulary.

**Limitation:** Capitalization can carry meaning. For example, `apple` may refer to a fruit, while `Apple` may refer to a company. Lowercasing should depend on the task.

#### 3.2 Uppercasing

Uppercasing converts letters to uppercase.

Example:

`natural language processing` → `NATURAL LANGUAGE PROCESSING`

Python example:

```python
text = "natural language processing"

normalized_text = text.upper()

print(normalized_text)
```

Output:

```text
NATURAL LANGUAGE PROCESSING
```

Uppercasing is useful for some text-matching tasks, but lowercasing is more common in traditional text-processing pipelines.

#### 3.3 Whitespace Normalization

Text may contain extra spaces, tabs, or newline characters.

Original:

`"Natural    Language     Processing"`

Normalized:

`"Natural Language Processing"`

Python example:

```python
import re

text = "   Natural    Language \n Processing   "

normalized_text = re.sub(r"\s+", " ", text).strip()

print(normalized_text)
```

Output:

```text
Natural Language Processing
```

Explanation:

- `\s+` matches one or more whitespace characters.
- `re.sub()` replaces matching sequences with a single space.
- `strip()` removes whitespace at the beginning and end.

Whitespace normalization is useful when text comes from copied documents, web pages, or inconsistent user input.

#### 3.4 Contraction Expansion

A contraction is a shortened form of two or more words.

Examples:

- `don't` → `do not`
- `can't` → `cannot`
- `I'm` → `I am`
- `they're` → `they are`
- `it's` → `it is` or `it has`, depending on context

Python example:

```python
text = "I don't know why they're waiting."

text = text.replace("don't", "do not")
text = text.replace("they're", "they are")

print(text)
```

Output:

```text
I do not know why they are waiting.
```

**Important:** Simple replacements are suitable for selected examples, but they do not handle every contraction or contextual ambiguity. A dedicated normalization tool or carefully designed rules may be needed for larger datasets.

#### 3.5 Standardizing Informal Language

Informal text often contains abbreviations, slang, and shortened expressions.

Examples:

| Informal Form | Standardized Form |
|---|---|
| `u` | `you` |
| `r` | `are` |
| `gr8` | `great` |
| `pls` | `please` |
| `thx` | `thanks` |

Python example:

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

Output:

```text
you are great
```

This approach uses a dictionary to map known informal expressions to standard forms.

**Limitation:** Informal expressions can have multiple meanings. Avoid replacing words blindly, especially when meaning or context matters.

#### 3.6 Unicode Normalization

Unicode allows some characters to be represented in more than one underlying way. For example, an accented character can be represented as a single character or as a base character followed by a combining accent.

Unicode normalization standardizes these representations.

Python example:

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

- **NFC:** Combines characters into canonical composed forms where possible.
- **NFD:** Decomposes characters into canonical forms.
- **NFKC:** Applies compatibility normalization and may combine characters that are considered compatibility-equivalent.
- **NFKD:** Applies compatibility decomposition.

Compatibility normalization can change the representation of some characters, so choose the form based on your data and application.

#### 3.7 Spelling Normalization

Spelling normalization standardizes selected spelling variations or corrects misspellings.

Examples:

- `teh` → `the`
- `recieve` → `receive`

These transformations usually require a dictionary, spelling-correction library, or context-aware method.

Automatic correction should be used carefully because names, technical terms, abbreviations, and regional spellings may otherwise be changed incorrectly.

#### 3.8 Repeated Character Normalization

Informal messages sometimes contain repeated characters for emphasis.

Examples:

- `soooo good` → `soo good`
- `heyyyy` → `heyy`

A simple regular expression can reduce repeated characters:

```python
import re

text = "This is sooo good!!!"

normalized_text = re.sub(r"(.)\1{2,}", r"\1\1", text)

print(normalized_text)
```

Output:

```text
This is soo good!!
```

This example limits sequences of three or more identical characters to two. Such rules may be useful for informal text but can damage meaningful spellings, names, or intentional expressions if applied indiscriminately.

### 4. Text Normalization vs. Text Cleaning

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

### 5. Text Normalization vs. Tokenization

**Normalization** standardizes text, while **tokenization** splits text into smaller units such as words or sentences.

Example:

Original text:

`"HELLO    WORLD!"`

After normalization:

`"hello world!"`

After word tokenization:

`["hello", "world", "!"]`

The exact tokens depend on the tokenizer used.

Normalization and tokenization are separate operations, although they are often used together in a text preprocessing pipeline.

### 6. Text Normalization vs. Stemming and Lemmatization

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

#### Comparison

| Technique | Purpose | Example |
|---|---|---|
| Lowercasing | Standardizes capitalization | `HELLO` → `hello` |
| Whitespace normalization | Standardizes spacing | Multiple spaces → one space |
| Stemming | Reduces words using rules | `studies` → `studi` |
| Lemmatization | Finds a dictionary form | `cars` → `car` |
| Tokenization | Splits text into units | Sentence → word tokens |

### 7. Complete Text Normalization Pipeline in Python

The following example combines lowercasing, contraction expansion, whitespace normalization, and selected informal-word replacements.

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

Output:

```text
Original Text: "   HELLO!!!   I don't know   why u r waiting.   "
Normalized Text: hello!!! i do not know why you are waiting.
```

#### Explanation

1. Unicode normalization standardizes compatible character representations.
2. Lowercasing makes capitalization consistent.
3. Contraction expansion replaces a selected shortened expression.
4. Dictionary-based replacements standardize selected informal words.
5. Whitespace normalization removes unnecessary spacing.

This pipeline deliberately keeps punctuation. Additional cleaning steps should be added only when the task requires them.

### 8. When Should You Use Text Normalization?

Normalization is useful in many applications.

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

### 9. Common Mistakes

1. **Removing all punctuation automatically.** Punctuation may carry meaning, especially in sentiment analysis or conversational text.
2. **Assuming every task needs lowercasing.** Capitalization can distinguish names, abbreviations, and other important information.
3. **Expanding contractions without considering context.** Expressions such as `it's` can have different expansions.
4. **Replacing informal words blindly.** Short forms may have multiple meanings.
5. **Confusing normalization with tokenization.** One standardizes text; the other splits it into units.
6. **Confusing stemming with lemmatization.** Stemming applies rules, while lemmatization aims to produce dictionary forms.
7. **Over-normalizing text.** Excessive transformations may remove important information or alter meaning.
8. **Applying inconsistent transformations.** Training and inference data should follow compatible preprocessing rules.
9. **Ignoring language-specific requirements.** Rules that work for English may not work for other languages.

### 10. Practice Exercises

#### Beginner Level

**Exercise 1:** Convert `"HELLO WORLD"` into lowercase.

**Exercise 2:** Convert `"natural language processing"` into uppercase.

**Exercise 3:** Normalize the spaces in `"  Python    is   useful  "`.

**Exercise 4:** Expand the contraction `"don't"` into `"do not"`.

#### Intermediate Level

**Exercise 5:** Create a dictionary to normalize `u`, `r`, and `gr8`.

**Exercise 6:** Use `unicodedata.normalize()` with NFC on a string containing an accented character.

**Exercise 7:** Write a program that combines lowercasing and whitespace normalization.

**Exercise 8:** Normalize a short social media message while preserving punctuation.

#### Conceptual Questions

1. What is text normalization?
2. Why is normalization useful in NLP?
3. What is the difference between text normalization and text cleaning?
4. What is the difference between normalization and tokenization?
5. Why might lowercasing be harmful in some applications?
6. What is Unicode normalization?
7. How are stemming and lemmatization related to normalization?
8. Why should normalization rules depend on the NLP task?

### 11. Points to Remember

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

### 12. References

- [Python: `str` Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python: `re` — Regular Expression Operations](https://docs.python.org/3/library/re.html)
- [Python: `unicodedata`](https://docs.python.org/3/library/unicodedata.html)
- [NLTK Documentation](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/usage)

---

**Next topic:** [Tokenization](../02_Tokenization/README.md)
