"""Rule-based chatbot implemented with NLTK's chat utilities."""

from nltk.chat.util import Chat, reflections


# Patterns are checked in order; keep the fallback rule last.
pairs = [
    (r".*\bmy name is\s+(.+)", ["Hello %1! How are you today?"]),
    (r".*\bhelp\b.*", ["I can respond to greetings, names, and a few simple topics."]),
    (r".*\bwhat is your name\??", ["I'm a simple rule-based chatbot built with Python and NLTK."]),
    (r".*\bhow are you\b.*", ["I'm working as expected. Thanks for asking!", "I'm doing well. Thanks!"]),
    (r".*\bsorry\b.*", ["That's alright.", "No worries."]),
    (r".*\bi am (good|well|okay|ok)\b.*", ["Nice to hear that.", "Great!"]),
    (r".*\bi'm (good|well|okay|ok)\b.*", ["Nice to hear that.", "Great!"]),
    (r"\b(hi|hey|hello|hola|holla)\b.*", ["Hello!", "Hey there!"]),
    (r".*\bwho created you\??", ["I'm a demonstration chatbot built with Python and NLTK."]),
    (r".*\b(created|made) you\??", ["I'm a demonstration chatbot built with Python and NLTK."]),
    (r".*\b(location|city)\b.*", ["I don't have access to live location information."]),
    (r".*\braining in (.+)", ["I can't check live weather for %1. Please use a weather service for current conditions."]),
    (r".*\bhealth\b.*", ["I'm software, so I don't have physical health."]),
    (r".*\b(sports|game|sport|cricket)\b.*", ["I can chat about sports, but my responses are limited to predefined rules."]),
    (r".*\b(who is|name)\b.*\b(cricketer|batsman)\b.*", ["You could ask me about a particular cricket player."]),
    (r"\b(quit|exit|bye|goodbye)\b", ["Bye for now. See you soon!"]),
    (r".*", ["I didn't understand that. Try typing 'help'."]),
]


def main() -> None:
    """Run the chatbot in the terminal."""
    print(
        "Hi! I'm a simple rule-based chatbot.\n"
        "Type a message in English. Enter 'quit' to exit."
    )
    Chat(pairs, reflections).converse()


if __name__ == "__main__":
    main()
