# Stop-Word Removal

Stop words are frequent words such as "the" or "and" that may contribute little to some text-analysis tasks. A stop-word list is a heuristic: removing words can also remove useful meaning, especially negation such as "not".

## Evidence and files

Existing scripts remove English stop words before stemming or lemmatization. Tokens.ipynb looks up stop-word lists in several languages; its saved Hindi and Kannada lookups have missing-resource errors.

- Stop_Word_Removal.py: safe removal example and language-availability check.
- Stop_Word_Removal.ipynb: explanation and exercises.
- Existing examples: [Stemming](../06_Stemming/) and [Lemmatization](../07_Lemmatization/).

Install NLTK with python -m pip install nltk. For the basic corpus, use python -m nltk.downloader popular. The script checks which language lists are installed instead of assuming every language is available.
