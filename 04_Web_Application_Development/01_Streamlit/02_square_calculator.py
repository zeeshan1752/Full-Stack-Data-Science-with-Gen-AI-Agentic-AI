import streamlit as st

st.title("Square Calculator")
st.write("Move the slider to select a number and calculate its square.")

number = st.slider("Pick a number", min_value=0, max_value=100, value=25)

squared_number = number ** 2

st.subheader("Result")
st.write(f"The square of **{number}** is **{squared_number}**.")
