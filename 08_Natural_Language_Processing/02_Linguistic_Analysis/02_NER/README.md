# Named Entity Recognition (NER)

## 1. Introduction

**Named Entity Recognition (NER)** is a Natural Language Processing (NLP) technique used to identify and classify spans of text that refer to named entities.

These entities can include people, organizations, locations, dates, times, monetary values, and other categories.

For example:

```text
Ada Lovelace worked in London for an organization.
```

A NER model may identify:

| Entity | Entity Label |
|---|---|
| Ada Lovelace | PERSON |
| London | GPE |

The exact entities and labels depend on the model, language, and context. NER systems may also miss entities or assign incorrect labels.

## 2. Why Do We Need NER?

NER helps extract useful information from unstructured text.

For example, a news article may mention people, companies, cities, and dates. NER can identify these spans so that another program can organize or analyze them.

### Common Applications

- Information extraction
- News article analysis
- Document processing
- Question-answering systems
- Customer support analysis
- Knowledge graph construction
- Search and information retrieval
- Identifying entities in reports and documents

NER is one component of an NLP pipeline. It does not independently understand every relationship or fact in a document.

## 3. Common Named Entity Categories

Entity labels vary between NLP libraries and models.

| Entity Category | Description | Example |
|---|---|---|
| `PERSON` | People, including fictional characters | Ada Lovelace |
| `ORG` | Organizations, companies, and institutions | Google |
| `GPE` | Countries, cities, states, and similar geopolitical entities | London |
| `LOC` | Non-GPE geographical locations | The Pacific Ocean |
| `FAC` | Facilities and infrastructure | The Eiffel Tower |
| `DATE` | Dates or periods | October 2026 |
| `TIME` | Times smaller than a day | 10:30 AM |
| `MONEY` | Monetary values | $500 |
| `PERCENT` | Percentage values | 25% |
| `PRODUCT` | Products | A named product |
| `EVENT` | Named events | A sporting event |
| `WORK_OF_ART` | Titles of creative works | A novel title |

These are common spaCy entity labels. NLTK uses a different set of labels, so the outputs from the two libraries may not match exactly.

## 4. How NER Works

A typical NER pipeline involves the following steps:

1. **Input text:** Provide a sentence, paragraph, or document.
2. **Tokenization:** Split the text into tokens.
3. **Context analysis:** Use surrounding words and learned patterns.
4. **Entity detection:** Identify spans that may refer to named entities.
5. **Entity classification:** Assign an entity label to each detected span.
6. **Output:** Return entity text and its predicted category.

For example:

```text
Input:
Ada Lovelace worked in London.
```

Possible output:

```text
Ada Lovelace : PERSON
London : GPE
```

The output is a prediction and is not guaranteed to be correct.

## 5. NER Using NLTK

NLTK provides named entity recognition through its `ne_chunk()` function.

In a typical NLTK workflow, the text is tokenized, POS-tagged, and then passed to the named entity chunker.

### Installation

Install NLTK:

```bash
python -m pip install nltk
```

### Example

```python
import nltk
from nltk import Tree

text = "Ada Lovelace worked on the Analytical Engine."

tokens = nltk.word_tokenize(text)
tagged_tokens = nltk.pos_tag(tokens)
entity_tree = nltk.ne_chunk(tagged_tokens, binary=False)

print("Named Entities:")

for node in entity_tree:
    if isinstance(node, Tree):
        entity_name = " ".join(
            word for word, tag in node.leaves()
        )
        entity_label = node.label()

        print(entity_name, ":", entity_label)
```

### Explanation

- `word_tokenize()` splits the text into tokens.
- `pos_tag()` assigns POS tags to the tokens.
- `ne_chunk()` identifies candidate named entities from the tagged tokens.
- `Tree` represents a chunk in the resulting entity tree.
- `node.leaves()` retrieves the words belonging to an entity.
- `node.label()` returns the predicted entity category.

NLTK's chunker commonly expects POS-tagged tokens as input.

## 6. NER Using spaCy

spaCy provides a trained NLP pipeline that can identify named entities directly from text.

### Installation

Install spaCy:

```bash
python -m pip install spacy
```

Download the English language model:

```bash
python -m spacy download en_core_web_sm
```

### Example

```python
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Ada Lovelace worked in London."

doc = nlp(text)

print("Named Entities:")

for entity in doc.ents:
    print(entity.text, ":", entity.label_)
```

### Explanation

- `spacy.load()` loads the trained English NLP pipeline.
- `nlp(text)` processes the text.
- `doc.ents` contains the entities detected by the pipeline.
- `entity.text` returns the entity's text.
- `entity.label_` returns its predicted entity label.

The `en_core_web_sm` model must be installed in the same Python environment used to run the script.

## 7. NLTK vs. spaCy NER

Both libraries support named entity recognition, but their APIs and entity-label conventions differ.

| Feature | NLTK | spaCy |
|---|---|---|
| Main library | NLTK | spaCy |
| Typical workflow | Tokenization, POS tagging, entity chunking | Process text through an NLP pipeline |
| Entity extraction | `nltk.ne_chunk()` | `doc.ents` |
| Entity text | Retrieved from tree leaves | `entity.text` |
| Entity label | `node.label()` | `entity.label_` |
| POS tagging | Usually a separate step before `ne_chunk()` | Available through the processed document |
| Model setup | Requires appropriate NLTK resources | Requires an installed spaCy language model |

The two libraries may detect different entities or assign different labels to the same text.

## 8. Comparing NLTK and spaCy

Your project includes separate scripts for both implementations. They expose the same function interface:

```python
extract_entities(text)
```

Both return lists of `(entity_text, label)` pairs.

This shared interface makes it possible to compare their results using the same input text.

For example, a comparison notebook can:

1. Load a sample sentence.
2. Run the NLTK entity extractor.
3. Run the spaCy entity extractor.
4. Display the entity-label pairs returned by each library.
5. Compare their predictions.

**Important:** A shared output format does not mean the libraries use identical entity categories or that their predictions will match.

## 9. Limitations of NER

1. **Prediction errors:** Models may miss entities or assign incorrect labels.
2. **Context dependence:** A name may be ambiguous without surrounding context.
3. **Different label sets:** Libraries can use different entity categories.
4. **Language dependence:** A model trained for one language may not work well for another.
5. **Domain differences:** Performance can vary between everyday text and specialized documents.
6. **Unfamiliar names:** Rare names and newly created organizations may be missed.
7. **Entity boundaries:** Models may select too much or too little text for an entity.
8. **Limited understanding:** Identifying an entity does not establish that every statement about it is true.

## 10. Common Mistakes

- Confusing POS tagging with NER.
- Assuming every proper noun will be recognized as an entity.
- Assuming NLTK and spaCy use identical labels.
- Forgetting to install the required NLTK resources.
- Forgetting to download the spaCy language model.
- Comparing results from different sentences instead of using the same input.
- Treating entity predictions as guaranteed facts.
- Assuming that every detected entity has been assigned the correct label.

## 11. Related Topics

- [Part-of-Speech Tagging](../01_POS_Tagging/README.md)
- [NLTK Notes](../../01_Preprocessing/02_Tokenization/README.md#nltk)

POS tagging and NER are related NLP tasks, but they solve different problems. POS tagging identifies grammatical categories, while NER identifies and classifies named entities.

## 12. Points to Remember

- NER stands for Named Entity Recognition.
- NER identifies and classifies spans referring to entities.
- Common categories include people, organizations, and locations.
- NLTK commonly uses POS-tagged tokens with `ne_chunk()`.
- spaCy exposes detected entities through `doc.ents`.
- Entity-label conventions differ between libraries.
- Both implementations can return `(entity_text, label)` pairs for comparison.
- NER output is an automated prediction and may contain errors.

## 14. References

- [NLTK Official Documentation](https://www.nltk.org/)
- [NLTK Data Guide](https://www.nltk.org/data.html)
- [NLTK Named Entity Chunking Documentation](https://www.nltk.org/api/nltk.chunk.html)
- [spaCy Official Documentation](https://spacy.io/usage)
- [spaCy Named Entity Recognition](https://spacy.io/usage/linguistic-features#named-entities)
- [spaCy Entity Labels](https://spacy.io/api/annotation#named-entities)
