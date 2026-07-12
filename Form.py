import streamlit as st
import pandas as pd

st.title("Streamlit Form Element")

with st.form(key="sample_form"):

    st.subheader("Text Inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide Your Feedback")

    st.subheader("Date and Time Inputs")
    dob = st.date_input('Select your date of birth')
    time = st.time_input('Choose your preffered time')

    st.subheader("Selectors")
    choice = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3", "Option 4"])
    gender = st.selectbox("Select your gender", ["Male", "Female"])
    slider_val = st.select_slider("Select a range: ", options=[1,2,3,4,5,6,7])

    st.subheader("Toggle & Checkboxes")
    notifications = st.checkbox("Recieve Notifications?")
    toggle_value = st.checkbox("Enable Dark Mode?",value=True)

    submit_btn = st.form_submit_button(label="Submit")
    if submit_btn:
        if not name:
            st.warning("Please fill in all the fields")
        else:
            st.balloons()
            st.success("Form Submitted Successfully")

st.subheader("Button")
if st.button("Click me"):
    st.write(f"Hello, {name}!")