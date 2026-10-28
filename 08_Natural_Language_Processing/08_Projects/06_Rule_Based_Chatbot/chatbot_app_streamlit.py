"""Streamlit frontend for the NLTK rule-based chatbot."""

import streamlit as st
from nltk.chat.util import Chat

from rule_based_chatbot_nltk import pairs
from nltk.chat.util import reflections


# Page configuration
st.set_page_config(
    page_title="Rule-Based Chatbot",
    page_icon="💬",
    layout="centered"
)

# Initialize chatbot and conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                'The chatbot can help with general questions.'
            )
        }
    ]

if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chat(pairs, reflections)


# Header
st.title("Rule-Based Chatbot")
st.caption("A conversational demo built with Python, NLTK and Streamlit.")

st.info(
    "This chatbot uses predefined patterns and responses. "
    "It is a learning project, not a generative AI assistant."
)


# Sidebar
with st.sidebar:
    st.header("About")

    st.write(
        "This chatbot matches your messages against "
        "regular-expression patterns defined in chatbot.py."
    )

    st.markdown("### Try asking")
    st.markdown(
        'This is a sample chatbot response.'
    )

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Conversation cleared. Hello again!"
            }
        ]

        st.session_state.chatbot = Chat(pairs, reflections)
        st.rerun()


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Generate response using NLTK
    response = st.session_state.chatbot.respond(prompt.strip())

    if not response:
        response = "I didn't understand that. Please try another message."

    # Display bot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()