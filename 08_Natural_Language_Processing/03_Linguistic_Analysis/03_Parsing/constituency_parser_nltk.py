"""Parse one sentence with a small hand-written NLTK constituency grammar."""

import nltk


GRAMMAR = nltk.CFG.fromstring(
    """
    S -> NP VP
    NP -> Det Adj N | Det N | Name
    VP -> V NP | V
    Det -> 'the' | 'a'
    Adj -> 'quick'
    N -> 'fox' | 'dog'
    Name -> 'ada'
    V -> 'sees' | 'writes'
    """
)


def parse_constituency(text: str):
    """Return all constituency trees accepted by the example grammar."""
    parser = nltk.ChartParser(GRAMMAR)
    tokens = text.lower().split()
    return list(parser.parse(tokens))


def main() -> None:
    sentence = "The quick fox sees a dog"
    parses = parse_constituency(sentence)
    if not parses:
        print("No parse found. Try a sentence covered by the small grammar.")
        return
    for tree in parses:
        print(tree)
        tree.pretty_print()


if __name__ == "__main__":
    main()
