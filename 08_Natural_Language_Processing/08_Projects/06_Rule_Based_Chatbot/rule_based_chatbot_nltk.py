"""NLTK rule-based chatbot patterns and responses."""

from nltk.chat.util import reflections

# Define chatbot patterns and responses
pairs = [
    [
        'sample chatbot phrase 1',
        ["Hello %2, how are you today?"]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you. What would you like to know?"]
    ],
    [
        r"(.*)your name(.*)",
        [
            'sample chatbot phrase 4'
        ]
    ],
    [
        r"how are you(.*)",
        ['sample chatbot phrase 5', 'sample chatbot phrase 6']
    ],
    [
        r"sorry(.*)",
        ["It's alright.", "It's OK, never mind."]
    ],
    [
        'sample chatbot phrase 2',
        ["Nice to hear that!", "Alright, great!"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello!", "Hey there!"]
    ],
    [
        r"what (.*) want(.*)",
        ["Make me an offer I can't refuse."]
    ],
    [
        r"(.*)created(.*)",
        [
            'sample chatbot phrase 7',
            "That's top secret!"
        ]
    ],
    [
        r"(.*)(location|city)(.*)",
        ["Hyderabad, India."]
    ],
    [
        r"(.*)raining in (.*)",
        [
            "No rain in the past 4 days here in %2.",
            "In %2, there is a 50% chance of rain."
        ]
    ],
    [
        'sample chatbot phrase 3',
        [
            'sample chatbot phrase 8'
        ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ['sample chatbot phrase 9']
    ],
    [
        r"who (.*)(cricketer|batsman)(.*)",
        ["Virat Kohli."]
    ],
    [
        r"quit",
        ["Bye for now. See you soon!"]
    ],
    [
        r"(.*)",
        ["Our customer service will reach you."]
    ]
]
