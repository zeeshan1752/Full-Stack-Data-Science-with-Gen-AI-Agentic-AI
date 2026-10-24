"""Build a basic word cloud from a short text sample."""
import matplotlib.pyplot as plt
from wordcloud import WordCloud


text = (
    "Natural language processing helps computers work with text. "
    "Text cleaning, tokenization, and language models are common NLP tasks."
)

cloud = WordCloud(
    width=900,
    height=450,
    background_color="white",
    collocations=False,
).generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.title("Example NLP Word Cloud")
plt.tight_layout()
plt.show()

# Install if needed: python -m pip install wordcloud
