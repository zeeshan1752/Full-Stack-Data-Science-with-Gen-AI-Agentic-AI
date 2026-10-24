# Lemmatization

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

## 1. Why Is Lemmatization Important?

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

## 2. How Does Lemmatization Work?

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

## 3. Lemmatization Using NLTK

NLTK provides the `WordNetLemmatizer`, which uses the WordNet lexical database.

### 3.1 Basic Example

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

### 3.2 Lemmatization With Part of Speech

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

## 4. Parts of Speech in NLTK

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

## 5. Lemmatization of a Sentence

Consider the sentence:

```text
The students are studying their lessons and playing games.
```

### Step 1: Tokenization

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

### Step 2: Lemmatization

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

### Step 3: Specify the Part of Speech

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

## 6. Lemmatization With Stop-Word Removal

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

## 7. Lemmatization vs. Stemming

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

## 8. Common Mistakes

- **Using the default part of speech for every word:** Verb forms such as `running` may remain unchanged.
- **Assuming every word will change:** A word that is already in its base form may remain the same.
- **Confusing stemming with lemmatization:** Stemming uses reduction rules, while lemmatization aims to identify a dictionary form.
- **Ignoring sentence context:** The same word can have different grammatical roles.
- **Removing stop words without considering meaning:** Negation words can change the interpretation of a sentence.
- **Forgetting WordNet data:** NLTK may require additional lexical resources.
- **Assuming lemmatization always improves accuracy:** Evaluate its effect on the intended NLP task.
- **Applying one part of speech to every token:** Use part-of-speech tagging when accurate sentence-level lemmatization is needed.

## 9. Practical Applications

### Search Engines

Lemmatization can help match different forms of words in search queries and documents.

### Sentiment Analysis

It can normalize related word forms in customer reviews while preserving more meaningful forms than aggressive stemming.

### Text Classification

Lemmatization can reduce vocabulary variation in document classification and topic detection.

### Chatbots

It can help normalize user messages before further language processing.

### Information Retrieval

Lemmatization can improve matching between queries and documents containing different grammatical forms of a word.

## 10. Exercises

### Exercise 1: Basic Lemmatization

Use `WordNetLemmatizer` on the following words:

```python
words = ["cars", "dogs", "studies", "playing"]
```

Observe the output using the default noun setting.

### Exercise 2: Verb Lemmatization

Use `pos="v"` on:

```python
words = ["playing", "played", "running", "studies"]
```

Compare the results with the default setting.

### Exercise 3: Adjective Lemmatization

Test the following words:

```python
words = ["better", "best", "faster"]
```

Try adjective and adverb parts of speech and compare the results.

### Exercise 4: Sentence Processing

Input:

```text
The children are playing, running, and studying.
```

Tasks:

1. Tokenize the sentence.
2. Remove stop words if appropriate.
3. Lemmatize the remaining tokens.
4. Compare the original words with their lemmas.

### Exercise 5: Stemming vs. Lemmatization

Compare both techniques on:

```python
words = ["studies", "running", "happiness", "cars"]
```

Identify which technique produces more recognizable dictionary forms.

### Exercise 6: Part-of-Speech Experiment

Use the word `meeting` as a noun and as a verb. Investigate how the part of speech affects lemmatization.

## 11. Installing and Configuring NLTK

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

## 12. Related Topics

- [Stemming](../06_Stemming/) — Reducing words through rule-based transformations.
- [Stop-Word Removal](../05_Stop_Word_Removal/) — Removing selected common words when appropriate.
- [Tokenization](../04_Tokenization/) — Splitting text into sentences or smaller units.
- [Bag of Words](../../02_Text_Representation/01_Bag_of_Words/) — Converting text into word-frequency features.

## 13. Points to Remember

- Lemmatization maps a word to its dictionary base form.
- The resulting form is called a lemma.
- NLTK provides the `WordNetLemmatizer`.
- Part-of-speech information can significantly affect results.
- Lemmatization differs from stemming because it uses vocabulary and linguistic information.
- WordNet resources may need to be downloaded separately.
- Stop-word removal and lemmatization are separate preprocessing operations.
- The choice of preprocessing should depend on the NLP task.

**Final takeaway:** Lemmatization normalizes words into meaningful dictionary forms. Using the correct part of speech helps produce better results when preparing text for NLP applications.
