"""Streamlit frontend for the NLTK rule-based chatbot."""

import streamlit as st
from nltk.chat.util import Chat, reflections

from Rule_Based_Chatbot import pairs


st.set_page_config(
    page_title="Rule-Based Chatbot",
    page_icon="💬",
    layout="centered",
)

st.title("💬 Rule-Based Chatbot")
st.caption("A simple conversational demo built with Python, NLTK, and Streamlit.")
st.info("This chatbot uses predefined rules. It is a learning project, not a generative AI assistant.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm a rule-based chatbot. Say hello or type **help** to see what I can do.",
        }
    ]

with st.sidebar:
    st.header("About")
    st.write("This app matches your messages with regular-expression patterns defined in Rule_Based_Chatbot.py.")
    st.markdown("**Try asking:**")
    st.markdown("- Hello\n- My name is Zee\n- Help\n- Who created you?")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Conversation cleared. Hello again! What would you like to ask?",
            }
        ]
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    chatbot = Chat(pairs, reflections)
    response = chatbot.respond(prompt.strip())
    if not response:
        response = "I didn't understand that. Try typing 'help'."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
