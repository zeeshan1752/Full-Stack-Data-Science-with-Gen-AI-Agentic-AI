# N-Grams with NLTK

## 1. What Are N-Grams?

An **N-gram** is a contiguous sequence of (n) tokens.

- **Unigram**: one token
- **Bigram**: two consecutive tokens
- **Trigram**: three consecutive tokens

For the tokens `["I", "love", "learning", "Python"]`, the bigrams are:

```text
("I", "love")
("love", "learning")
("learning", "Python")
```

## 2. Generate N-Grams with NLTK

Install NLTK if needed:

```bash
python -m pip install nltk
```

Example:

```python
from nltk.tokenize import wordpunct_tokenize
from nltk.util import ngrams

sentence = "I love learning Python"
tokens = wordpunct_tokenize(sentence)

print("Tokens:", tokens)

bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
```

Expected output:

```text
Tokens: ['I', 'love', 'learning', 'Python']
Bigrams: [('I', 'love'), ('love', 'learning'), ('learning', 'Python')]
Trigrams: [('I', 'love', 'learning'), ('love', 'learning', 'Python')]
```

**Important:** `ngrams(tokens, n)` requires the value of `n`. Calling `ngrams(tokens)` raises a `TypeError` because the required argument is missing.

## 3. Change the N-Gram Size

```python
n = 2
sequences = list(ngrams(tokens, n))
print(sequences)
```

The number of contiguous N-grams from (m) tokens is (m-n+1), provided (1 \le n \le m). If (n) is larger than the token sequence, the result is an empty list.

## 4. When Are N-Grams Useful?

- Capturing short phrases such as `"machine learning"`
- Building simple language models
- Creating features for text classification
- Detecting repeated phrases
- Comparing text patterns

N-grams do not understand meaning by themselves. Larger values of (n) create more specific sequences, but also produce more possible features and sparser data.

## 5. Common Mistakes

- Forgetting the required `n` argument.
- Passing a raw string when you intend to work with a list of tokens.
- Assuming that a bigram list contains every possible pair; NLTK's `ngrams` produces **adjacent** token sequences.
- Forgetting that punctuation may be included as tokens, depending on the tokenizer.

## References

- [NLTK API: ngrams](https://www.nltk.org/api/nltk.util.html#nltk.util.ngrams)
- [NLTK documentation](https://www.nltk.org/)
