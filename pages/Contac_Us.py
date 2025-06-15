import streamlit as st

st.header("Contac Me")

with st.form(key="email_formos"):
    user_email = st.text_input("Your email address")
    mesagge = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("Y was pressed!")