import streamlit as st
from send_email import send_email


st.header('Contact me')

with st.form(key='email_form'):
    user_email = st.text_input('You email address')
    text_area_message = st.text_area('Your message')
    received_message = f"""\
Subject: New message from {user_email} / Python portfolio app

From: {user_email}
{text_area_message}
"""
    button = st.form_submit_button('Submit')
    if button:
        send_email(received_message)
        st.info('Your email was sent successfully')
