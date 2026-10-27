# Rule-Based Chatbot

A beginner-friendly chatbot built with **Python**, **NLTK**, and **Streamlit**. It matches user messages against regular-expression patterns and returns predefined responses. The project includes both a terminal version and a simple web interface.

> This is a rule-based demonstration, not an AI language model. It does not learn from conversations or provide live weather/location information.

## Features

- Responds to greetings and common questions.
- Recognises simple name-introduction messages.
- Uses regular expressions to match user input.
- Applies NLTK chat reflections.
- Provides a terminal-based chatbot.
- Includes a Streamlit chat interface with message history.
- Shows a helpful fallback response when no rule matches.

## Project Structure

    06_Rule_Based_Chatbot/
    ├── Rule_Based_Chatbot.py   # Chatbot rules and terminal version
    ├── app.py                  # Streamlit web interface
    ├── requirements.txt        # Required Python packages
    └── README.md               # Project documentation

## Requirements

- Python 3.9 or newer
- pip

## Installation

Open a terminal in this folder and install the dependencies:

    python -m pip install -r requirements.txt

## Run the Terminal Chatbot

    python Rule_Based_Chatbot.py

Type a message and press Enter. Type **quit**, **exit**, **bye**, or **goodbye** to leave.

## Run the Streamlit App

    python -m streamlit run app.py

Streamlit will display a local URL in the terminal. Open that URL in your browser to chat with the bot.

## How It Works

1. The chatbot stores regular-expression patterns and their possible responses in a list called **pairs**.
2. NLTK checks the user's message against the patterns in order.
3. The first matching rule supplies a predefined response.
4. The Streamlit interface stores the conversation in session state and displays the messages.
5. The final catch-all pattern provides a fallback response when no specific rule matches.

**Important:** Keep the fallback pattern **r".*"** at the end of the list because it matches almost every input.

## Example

| User message | Example response |
| --- | --- |
| hello | Hello! |
| my name is Zee | Hello Zee! How are you today? |
| help | A short list of the chatbot's capabilities |
| quit | Bye for now. See you soon! |

Responses can vary when a rule contains more than one possible reply.

## Customise the Chatbot

Edit the **pairs** list in Rule_Based_Chatbot.py. Each entry contains a regular-expression pattern and a list of responses. Add more specific patterns before the final fallback pattern. The bot only responds to patterns that you define.

## Limitations

- The chatbot uses predefined rules and cannot understand every phrasing.
- It does not use a trained machine-learning or large language model.
- Weather and location answers are not live data.
- Conversation history in the Streamlit app is kept in the current session.

## Technologies Used

- Python
- NLTK
- Streamlit

## Learning Outcomes

- Working with regular expressions
- Using NLTK's Chat and reflections
- Organising Python code into reusable functions
- Building a basic interactive interface with Streamlit
