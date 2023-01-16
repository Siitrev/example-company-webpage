import streamlit as st
import pandas as pd
import os
from utils.helper import validate_email,send_email
from utils.constants import (SMTP_SERVER_ADDRESS,PORT,SENDER_PASSWORD,SENDER_ADDRESS,RECIEVER_ADDRESS)

st.set_page_config(page_title="The best company - Contact",layout="wide")

df = pd.read_csv("topics.csv")

with st.form("Contact"):
    email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?",options=df)
    text = st.text_area("Text")
    send = st.form_submit_button("Send")
    
message = f"""
-------------------------------------------------------------------------------------------------------
This message was sent by: {email}
-------------------------------------------------------------------------------------------------------

"""
message += text

if send:
    if validate_email(email):
        send_email(sender=SENDER_ADDRESS,password=SENDER_PASSWORD,
               reciever=RECIEVER_ADDRESS,smtp_server=SMTP_SERVER_ADDRESS,smtp_port=PORT,
               email_message=message,subject=topic)
        st.write("<p style='color: green'>Email has been sent!</p>",unsafe_allow_html=True)
    else:
        st.write("<p style='color: red'>Wrong email! Please try again.</p>",unsafe_allow_html=True)