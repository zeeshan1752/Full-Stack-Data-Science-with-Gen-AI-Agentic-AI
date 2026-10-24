# Stemming Comparison

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

# Words for stemming
words = ["connect", "connected", "connecting", "connection"]

# Create stemmer objects
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

# Porter Stemming
print("Porter Stemmer:")
for word in words:
    print(word, "->", porter.stem(word))

# Lancaster Stemming
print("\nLancaster Stemmer:")
for word in words:
    print(word, "->", lancaster.stem(word))

# Snowball Stemming
print("\nSnowball Stemmer:")
for word in words:
    print(word, "->", snowball.stem(word))
