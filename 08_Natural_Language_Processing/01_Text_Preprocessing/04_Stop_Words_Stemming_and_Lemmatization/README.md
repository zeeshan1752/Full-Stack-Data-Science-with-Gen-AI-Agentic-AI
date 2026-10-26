
# 04 Stop Words, Stemming, and Lemmatization

## 1. Introduction

Stop-word removal, stemming, and lemmatization are common text preprocessing techniques used in Natural Language Processing (NLP). They help prepare text for analysis by filtering selected words or reducing word variations.

Each technique serves a different purpose:

- **Stop-word removal:** Removes selected words from text.
- **Stemming:** Reduces words to simplified stems using rules.
- **Lemmatization:** Converts words into their dictionary base forms.

Detailed explanations and implementations are covered in their respective folders.

## 2. Comparison

| Technique | Purpose | Example | Main Consideration |
|---|---|---|---|
| Stop-word removal | Removes selected frequent words. | `the cat runs` → `cat runs` | Can remove meaningful words such as `not`. |
| Stemming | Reduces words using stemming rules. | `studies` → `studi` | May produce non-dictionary words. |
| Lemmatization | Converts words to dictionary base forms. | `running` → `run` | May require linguistic resources and context. |

## 3. Combined Example

Original text:

```text
The cats are running in the gardens.
```

A possible preprocessing result:

```text
cat run garden
```

This result may involve stop-word removal, stemming or lemmatization, and lowercasing. The exact output depends on the tools, language, and processing order.

## 4. When to Use Each Technique

- Use **stop-word removal** when selected frequent words do not contribute useful information to the task.
- Use **stemming** when a simpler reduction of related word forms is sufficient.
- Use **lemmatization** when meaningful dictionary forms are preferred.
- Evaluate the results before combining these techniques in a preprocessing pipeline.

These techniques are not mandatory for every NLP application. Transformer-based models generally use their own tokenizers and may perform best with their expected input format.

## 5. Related Topics

- [Stop-Word Removal](../03_Stop_Word_Removal/)
- [Stemming](../02_Stemming/)
- [Lemmatization](../03_Lemmatization/)

Refer to these folders for detailed explanations, Python implementations, and practical examples.

## 6. Key Takeaways

- Stop-word removal filters selected words.
- Stemming reduces words to simplified stems.
- Lemmatization aims to produce dictionary base forms.
- Each technique has different benefits and trade-offs.
- Choose preprocessing methods according to the NLP task and model requirements.
