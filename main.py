import streamlit as st

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Set page header
st.header("My Streamlit App")

# Get value from user
user_input = st.number_input("Enter a value", min_value=0.0, max_value=100.0, value=50.0, step=1.0)

# Display output
st.write("The value you entered is:", user_input)

miau = user_input * 4

st.write("The value you entered mutilplied by 4 is:", user_input)
