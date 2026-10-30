# Introduction to NLP

text = "Natural Language Processing is interesting and useful."

print("Original Text:", text)

# Convert text to lowercase
lowercase_text = text.lower()
print("\nLowercase Text:", lowercase_text)

# Count characters
print("Number of Characters:", len(text))

# Split text into words
words = lowercase_text.split()
print("Words:", words)

# Count words
print("Number of Words:", len(words))

# Count occurrences of a word
search_word = "language"
print("Occurrences of 'language':", words.count(search_word))

# Check whether a word exists
search_word = "processing"

if search_word in words:
    print(search_word, "is present in the text.")
else:
    print(search_word, "is not present in the text.")

# Remove punctuation
text_with_punctuation = "Hello, NLP! Python is amazing."
cleaned_text = (
    text_with_punctuation
    .replace(",", "")
    .replace("!", "")
    .replace(".", "")
)

print("\nText Before Cleaning:", text_with_punctuation)
print("Text After Cleaning:", cleaned_text)

# Compare two sentences without considering case
sentence1 = "I love Natural Language Processing."
sentence2 = "I LOVE NATURAL LANGUAGE PROCESSING."

if sentence1.lower() == sentence2.lower():
    print("\nBoth sentences are equal when case is ignored.")
else:
    print("\nThe sentences are different.")

# Count the frequency of every word
sample_text = "python is useful and python is popular"
sample_words = sample_text.lower().split()

word_counts = {}

for word in sample_words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\nWord Frequencies:")

for word, count in word_counts.items():
    print(word, ":", count)

# Find unique words
sample_text = "cats chase dogs and dogs chase cats"
unique_words = set(sample_text.lower().split())

print("\nUnique Words:", sorted(unique_words))
print("Number of Unique Words:", len(unique_words))

# Compare words in two sentences
sentence1 = "Python is easy to learn"
sentence2 = "Python is useful for data science"

words1 = set(sentence1.lower().split())
words2 = set(sentence2.lower().split())

print("\nCommon Words:", sorted(words1.intersection(words2)))
print("Different Words:", sorted(words1.symmetric_difference(words2)))

# Basic text statistics
sample_text = "Natural language processing helps computers understand text."
sample_words = sample_text.lower().split()

print("\nText Statistics:")
print("Characters:", len(sample_text))
print("Words:", len(sample_words))
print("Unique Words:", len(set(sample_words)))