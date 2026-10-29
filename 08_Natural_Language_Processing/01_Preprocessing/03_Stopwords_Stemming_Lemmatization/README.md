# 03 Stopwords Stemming Lemmatization

---

## Lemmatization

Lemmatization is a text preprocessing technique in Natural Language Processing (NLP) that converts a word into its dictionary base form, known as a **lemma**.

Unlike stemming, which removes or modifies word endings using rules, lemmatization uses vocabulary and linguistic information to identify a meaningful base form.

For example:

| Original Word | Lemma |
|---|---|
| playing | play |
| played | play |
| studies | study |
| cars | car |
| better | good (in the appropriate context) |
| running | run |

The resulting lemma is generally a valid dictionary word. However, the correct result depends on the word's grammatical role and the capabilities of the lemmatizer.

### 1. Why Is Lemmatization Important?

Words can have different grammatical forms while sharing the same basic meaning.

For example:

```text
play
playing
played
plays
```

Lemmatization can reduce these forms to `play`, helping NLP systems process related word forms consistently.

Lemmatization is useful for:

- Reducing different word forms to their dictionary base forms.
- Preparing text for information retrieval and search.
- Preprocessing documents for text classification.
- Analyzing customer reviews and feedback.
- Supporting text analysis in chatbots.
- Normalizing vocabulary before text representation.
- Processing grammatical variations in natural language.

**Important:** Lemmatization does not always improve model performance. Its usefulness depends on the language, dataset, and NLP task.

### 2. How Does Lemmatization Work?

A lemmatizer uses linguistic information and a vocabulary to determine the base form of a word.

Consider these examples:

```text
cars       → car
studies    → study
am         → be
better     → good
```

The result can depend on the part of speech supplied to the lemmatizer.

For example, the word `meeting` may refer to an event or to the action of meeting. Its correct base form depends on how it is used.

This is why lemmatization can require more linguistic information than simple suffix removal.

### 3. Lemmatization Using NLTK

NLTK provides the `WordNetLemmatizer`, which uses the WordNet lexical database.

#### 3.1 Basic Example

```python
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")
nltk.download("omw-1.4")

lemmatizer = WordNetLemmatizer()

words = ["cars", "playing", "studies", "running"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
```

Expected output:

```text
cars -> car
playing -> playing
studies -> study
running -> running
```

Notice that `playing` and `running` remain unchanged. By default, `WordNetLemmatizer` treats the input as a noun unless another part of speech is specified.

#### 3.2 Lemmatization With Part of Speech

To obtain the lemma of a verb, specify the verb part of speech using `pos="v"`.

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["playing", "played", "running", "studies"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word, pos="v"))
```

Expected output:

```text
playing -> play
played -> play
running -> run
studies -> study
```

This example demonstrates why choosing the correct part of speech is important.

### 4. Parts of Speech in NLTK

The `WordNetLemmatizer` supports several WordNet part-of-speech categories.

| Part of speech | NLTK value | Example |
|---|---|---|
| Noun | `n` | `cars` → `car` |
| Verb | `v` | `running` → `run` |
| Adjective | `a` | `better` → `good` |
| Adverb | `r` | `faster` → `fast` |

For example:

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cars", pos="n"))
print(lemmatizer.lemmatize("running", pos="v"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("faster", pos="r"))
```

Output:

```text
car
run
good
fast
```

These examples show how the part of speech affects the output. A lemmatizer does not automatically understand every word's role in a sentence merely because the correct `pos` parameter exists.

### 5. Lemmatization of a Sentence

Consider the sentence:

```text
The students are studying their lessons and playing games.
```

#### Step 1: Tokenization

Split the sentence into tokens.

```python
from nltk.tokenize import word_tokenize

text = "The students are studying their lessons and playing games."

words = word_tokenize(text)

print(words)
```

Output:

```python
[
    "The", "students", "are", "studying", "their",
    "lessons", "and", "playing", "games", "."
]
```

#### Step 2: Lemmatization

Apply the appropriate part of speech to each token.

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = [
    "students", "are", "studying",
    "lessons", "playing", "games"
]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
```

With the default noun setting, verbs such as `studying` and `playing` may remain unchanged.

#### Step 3: Specify the Part of Speech

```python
print(lemmatizer.lemmatize("studying", pos="v"))
print(lemmatizer.lemmatize("playing", pos="v"))
print(lemmatizer.lemmatize("are", pos="v"))
```

Output:

```text
study
play
be
```

For accurate sentence-level lemmatization, a practical pipeline can use part-of-speech tagging before lemmatization.

### 6. Lemmatization With Stop-Word Removal

Lemmatization can be combined with tokenization and stop-word removal.

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

text = "The students are studying and playing games."

words = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]

lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word, pos="v")
    for word in filtered_words
]

print("Original Text:", text)
print("Tokens:", words)
print("After Stop-Word Removal:", filtered_words)
print("After Lemmatization:", lemmatized_words)
```

The output is a list of normalized tokens. Because the example applies verb lemmatization to every remaining token, some nouns may not be lemmatized optimally. In a more advanced pipeline, part-of-speech tagging should be used to select the appropriate category for each word.

**Important:** Stop-word removal should be task-dependent. Words such as `not` can be essential for understanding sentiment and meaning.

### 7. Lemmatization vs. Stemming

Stemming and lemmatization both reduce variations in words, but they use different approaches.

| Feature | Stemming | Lemmatization |
|---|---|---|
| Method | Applies rules to remove or modify word endings | Uses vocabulary and linguistic information |
| Output | May not be a valid word | Generally produces a dictionary form |
| Part of speech | Usually not required | Can improve results when supplied |
| Processing | Usually faster | May require additional linguistic resources |
| Example | `studies` → `studi` | `studies` → `study` |
| Example | `running` may become `run` | `running` → `run` when treated as a verb |
| Complexity | Relatively simple | Generally more linguistically informed |

Choose stemming when simple word reduction is sufficient. Consider lemmatization when meaningful dictionary forms are important.

### 8. Common Mistakes

- **Using the default part of speech for every word:** Verb forms such as `running` may remain unchanged.
- **Assuming every word will change:** A word that is already in its base form may remain the same.
- **Confusing stemming with lemmatization:** Stemming uses reduction rules, while lemmatization aims to identify a dictionary form.
- **Ignoring sentence context:** The same word can have different grammatical roles.
- **Removing stop words without considering meaning:** Negation words can change the interpretation of a sentence.
- **Forgetting WordNet data:** NLTK may require additional lexical resources.
- **Assuming lemmatization always improves accuracy:** Evaluate its effect on the intended NLP task.
- **Applying one part of speech to every token:** Use part-of-speech tagging when accurate sentence-level lemmatization is needed.

### 9. Practical Applications

#### Search Engines

Lemmatization can help match different forms of words in search queries and documents.

#### Sentiment Analysis

It can normalize related word forms in customer reviews while preserving more meaningful forms than aggressive stemming.

#### Text Classification

Lemmatization can reduce vocabulary variation in document classification and topic detection.

#### Chatbots

It can help normalize user messages before further language processing.

#### Information Retrieval

Lemmatization can improve matching between queries and documents containing different grammatical forms of a word.

### 10. Installing and Configuring NLTK

Install NLTK using the following command:

```bash
python -m pip install nltk
```

Download the lexical resources required for WordNet lemmatization:

```python
import nltk

nltk.download("wordnet")
nltk.download("omw-1.4")
```

For examples involving tokenization and stop-word removal, you may also need:

```python
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
```

Download only the resources needed by your program. If NLTK reports a missing resource, follow the resource name given in the error message.

### 11. Related Topics

- [Stemming](stemming_comparison_nltk.py) — Reducing words through rule-based transformations.
- [Stop-Word Removal](stopword_removal_nltk.py) — Removing selected common words when appropriate.
- [Tokenization](../02_Tokenization/) — Splitting text into sentences or smaller units.
- [Bag of Words](../../03_Text_Representation/01_Bag_of_Words_and_NGrams/) — Converting text into word-frequency features.

### 12. Points to Remember

- Lemmatization maps a word to its dictionary base form.
- The resulting form is called a lemma.
- NLTK provides the `WordNetLemmatizer`.
- Part-of-speech information can significantly affect results.
- Lemmatization differs from stemming because it uses vocabulary and linguistic information.
- WordNet resources may need to be downloaded separately.
- Stop-word removal and lemmatization are separate preprocessing operations.
- The choice of preprocessing should depend on the NLP task.

**Final takeaway:** Lemmatization normalizes words into meaningful dictionary forms. Using the correct part of speech helps produce better results when preparing text for NLP applications.

---

## Stemming

Stemming is a text preprocessing technique in Natural Language Processing (NLP) that reduces words to a common stem by removing or modifying word endings.

It helps group related word forms so that they can be treated similarly during text analysis.

For example:

| Original Word | Possible Stem |
|---|---|
| connected | connect |
| connecting | connect |
| connects | connect |
| studies | studi |
| playing | play |

A stem is not guaranteed to be a valid English dictionary word. Stemming uses algorithmic rules rather than understanding the complete meaning of a word.

### 1. Why Is Stemming Important?

The same basic word can appear in multiple forms in natural language.

For example:

```text
connect
connected
connecting
connects
```

Without preprocessing, a text-processing system may treat these as separate tokens. Stemming can reduce some of these forms to a common stem.

Stemming is useful for:

- Reducing variations in word forms.
- Preparing text for information retrieval and search.
- Preprocessing documents for text classification.
- Reducing vocabulary size in some NLP pipelines.
- Processing reviews, articles, and other text data.
- Preparing text for Bag of Words and TF-IDF representations.

**Important:** Stemming is not always necessary. Whether it improves results depends on the dataset and the NLP task.

### 2. How Does Stemming Work?

Stemming applies language-specific rules to modify words, often by removing suffixes.

Consider the following examples:

```text
playing   → play
played    → play
connected → connect
```

A stemming algorithm does not necessarily determine the grammatical role or meaning of a word. It applies rules based on its implementation.

For example, a stemmer may reduce a word to a form that is not a valid dictionary word:

```text
studies → studi
```

This can still be useful when the goal is to group related word forms.

### 3. Types of Stemming Algorithms

Several stemming algorithms are available. Porter, Lancaster, and Snowball are three commonly used stemmers in NLTK.

#### 3.1 Porter Stemmer

The Porter Stemmer uses a sequence of suffix-removal rules to reduce words to their stems.

It is a widely known stemming algorithm used in English text processing.

Example:

```python
from nltk.stem import PorterStemmer

porter = PorterStemmer()

words = ["connect", "connected", "connecting", "connection"]

for word in words:
    print(word, "->", porter.stem(word))
```

Typical output:

```text
connect -> connect
connected -> connect
connecting -> connect
connection -> connect
```

**Characteristics:**

- Uses a sequence of stemming rules.
- Is widely used in traditional English NLP workflows.
- May produce stems that are not dictionary words.
- Can be useful for text retrieval and classification.

#### 3.2 Lancaster Stemmer

The Lancaster Stemmer uses a more aggressive set of stemming rules. It can shorten words more extensively than some other stemmers.

Example:

```python
from nltk.stem import LancasterStemmer

lancaster = LancasterStemmer()

words = ["playing", "played", "plays", "happiness"]

for word in words:
    print(word, "->", lancaster.stem(word))
```

Typical output:

```text
playing -> play
played -> play
plays -> play
happiness -> happy
```

The exact stem depends on the algorithm's rules.

**Characteristics:**

- Often produces shorter stems.
- Applies relatively aggressive stemming rules.
- Can reduce different words to the same stem.
- May remove more information from words than desired.

#### 3.3 Snowball Stemmer

The Snowball Stemmer is a family of stemming algorithms for multiple languages. NLTK provides a Snowball implementation for English and several other languages.

Example:

```python
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer("english")

words = ["running", "runs", "runner", "easily"]

for word in words:
    print(word, "->", snowball.stem(word))
```

Typical output:

```text
running -> run
runs -> run
runner -> runner
easily -> easili
```

**Characteristics:**

- Supports multiple languages.
- Provides language-specific stemming rules.
- Is useful when working with supported non-English text.
- May produce stems that are not dictionary words.

### 4. Comparison of Stemming Algorithms

| Feature | Porter | Lancaster | Snowball |
|---|---|---|---|
| Approach | Rule-based suffix reduction | Aggressive rule-based reduction | Language-specific stemming rules |
| Languages | Primarily English | Primarily English | Multiple supported languages |
| Stemming strength | Moderate | Often aggressive | Depends on the language and algorithm |
| Output | May not be a dictionary word | May not be a dictionary word | May not be a dictionary word |
| Common use | Traditional English NLP | Experiments requiring stronger reduction | Multilingual preprocessing |

Different stemmers can produce different results for the same input. None is automatically the best choice for every application.

### 5. Practical Comparison Using NLTK

The following example applies all three stemmers to the same set of words.

```python
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

words = ["connect", "connected", "connecting", "connection"]

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

print("Porter Stemmer:")
for word in words:
    print(word, "->", porter.stem(word))

print("\nLancaster Stemmer:")
for word in words:
    print(word, "->", lancaster.stem(word))

print("\nSnowball Stemmer:")
for word in words:
    print(word, "->", snowball.stem(word))
```

For this particular group of words, all three stemmers may produce the same result. To understand their differences, test them with a broader vocabulary.

### 6. Stemming in an NLP Pipeline

Stemming is commonly used after tokenization and may follow stop-word removal.

```text
Raw Text
   ↓
Text Cleaning
   ↓
Tokenization
   ↓
Optional Stop-Word Removal
   ↓
Stemming
   ↓
Text Representation
   ↓
Machine Learning Model
```

Consider this example:

**Original text:**

```text
The players are playing and played well.
```

**After tokenization:**

```python
["The", "players", "are", "playing", "and", "played", "well", "."]
```

**After optional stop-word removal:**

```python
["players", "playing", "played", "well", "."]
```

**After stemming:**

```python
["player", "play", "play", "well", "."]
```

The exact output depends on the stemmer and the input tokens.

Stemming can help reduce variations before text is converted into numerical features. However, punctuation handling and stop-word removal should be selected according to the task.

### 7. Stemming vs. Lemmatization

Stemming and lemmatization both reduce word variations, but they use different approaches.

| Feature | Stemming | Lemmatization |
|---|---|---|
| Method | Applies stemming rules | Uses vocabulary and linguistic analysis |
| Output | A stem that may not be a word | Usually a valid dictionary form |
| Context | Generally does not understand sentence context | Quality depends on the lemmatizer and available linguistic information |
| Speed | Usually faster | Often more computationally intensive |
| Example | `studies` → `studi` | `studies` → `study` |
| Example | `better` may remain `better` | May become `good` when the correct part of speech is supplied |

Choose stemming when simple reduction is sufficient. Consider lemmatization when meaningful dictionary forms are important.

### 8. Common Mistakes

- **Assuming every stem is a valid word:** Stemming can produce forms such as `studi`.
- **Assuming all stemmers produce the same result:** Their rules differ.
- **Confusing stemming with lemmatization:** Lemmatization aims to return a dictionary form.
- **Applying stemming without evaluating the task:** It can remove useful distinctions between words.
- **Assuming stemming understands context:** Traditional stemmers mainly apply algorithmic rules.
- **Ignoring language support:** A stemmer must be appropriate for the language being processed.
- **Assuming stemming always improves accuracy:** Evaluate the resulting NLP model rather than assuming preprocessing is beneficial.

### 10. Practical Applications

#### Search Engines

Stemming can help match related word forms in search queries and documents.

#### Text Classification

Stemming can reduce vocabulary variations in spam detection, topic classification, and document categorization.

#### Sentiment Analysis

It may help group related word forms in reviews, although excessive stemming can remove distinctions important to sentiment.

#### Information Retrieval

Stemming can improve matching between a user's query and documents containing related forms of the same word.

### 11. Related Topics

- [Stop-Word Removal](stopword_removal_nltk.py) — Removing selected common words before further processing.
- [Lemmatization](lemmatization_nltk.ipynb) — Reducing words to their dictionary forms using linguistic information.
- [Tokenization](../02_Tokenization/) — Splitting text into smaller units.
- [Bag of Words](../../03_Text_Representation/01_Bag_of_Words_and_NGrams/) — Converting text into word-frequency features.

### 12. Points to Remember

- Stemming reduces words using algorithmic rules.
- A stem is not necessarily a valid dictionary word.
- Porter, Lancaster, and Snowball use different stemming approaches.
- Lancaster is often more aggressive than Porter.
- Snowball supports multiple languages.
- Stemming can reduce vocabulary variations in NLP pipelines.
- Stemming is different from lemmatization.
- The best preprocessing method depends on the application and should be evaluated.

**Final takeaway:** Stemming simplifies text by reducing related word forms to common stems. Understanding its algorithms and limitations helps you decide when stemming is useful in an NLP pipeline.

---

## Stop-Word Removal

Stop words are frequent words such as "the" or "and" that may contribute little to some text-analysis tasks. A stop-word list is a heuristic: removing words can also remove useful meaning, especially negation such as "not".

### Evidence and files

Existing scripts remove English stop words before stemming or lemmatization. Tokens.ipynb looks up stop-word lists in several languages; its saved Hindi and Kannada lookups have missing-resource errors.

- Stop_Word_Removal.py: safe removal example and language-availability check.
- Stop_Word_Removal.ipynb: explanation and exercises.
- Existing examples: [Stemming](stemming_comparison_nltk.py) and [Lemmatization](lemmatization_nltk.ipynb).

Install NLTK with python -m pip install nltk. For the basic corpus, use python -m nltk.downloader popular. The script checks which language lists are installed instead of assuming every language is available.
