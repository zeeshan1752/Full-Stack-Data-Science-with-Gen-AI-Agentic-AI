import numpy as np
import pandas as pd
import streamlit as st

st.title("Streamlit Widgets and Balloons")
st.write("Explore sidebar inputs, a sample DataFrame, and a button.")

st.sidebar.header("User Input Features")
user_name = st.sidebar.text_input("What is your name?", "Guest")
age = st.sidebar.slider("Select your age", min_value=0, max_value=100, value=25)
favorite_color = st.sidebar.selectbox(
    "What is your favorite color?",
    ["Blue", "Red", "Green", "Yellow"],
)

st.header(f"Welcome, {user_name}!")
st.write(f"You are {age} years old and your favorite color is {favorite_color}.")

st.subheader("Sample Data")
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=[f"Column {i}" for i in range(1, 6)],
)
st.dataframe(data, use_container_width=True)

if st.checkbox("Show raw data"):
    st.write(data)

if st.button("Send balloons!"):
    st.balloons()
    st.success("Great! You clicked the button.")
