"""A small rule-based chatbot demo using NLTK's pattern matcher."""

from nltk.chat.util import Chat, reflections


pairs = [
    (r".*my name is (.*)", ["Hello %1! How are you today?"]),
    (r".*\\bhelp\\b.*", ["I can respond to greetings, names, and a few simple topics."]),
    (r".*your name\\??", ["I'm a simple rule-based chatbot built with Python and NLTK."]),
    (r"how are you.*", ["I'm working as expected. Thanks for asking!"]),
    (r"sorry.*", ["That's alright.", "No worries."]),
    (r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that.", "Great!"]),
    (r"(hi|hey|hello|hola).*", ["Hello!", "Hey there!"]),
    (r".*created.*", ["This is a small demonstration of NLTK's chat utilities."]),
    (r".*\\b(location|city)\\b.*", ["I don't have live location access."]),
    (r".*raining in (.*)", ["I can't check live weather for %1, but a weather service can."]),
    (r"how .* health .*", ["I'm software, so I don't have physical health."]),
    (r".*\\b(sports|game|sport)\\b.*", ["I can chat about sports, but my knowledge is limited."]),
    (r"who .* (cricketer|batsman).*", ["You could ask me about a particular player."]),
    (r"quit", ["Bye for now. See you soon!"]),
    (r".*", ["I didn't understand that. Try typing 'help'."]),
]


def main():
    print(
        "Hi! I'm a simple rule-based chatbot.\\n"
        "Type a message in English. Enter 'quit' to exit."
    )
    Chat(pairs, reflections).converse()


if __name__ == "__main__":
    main()
