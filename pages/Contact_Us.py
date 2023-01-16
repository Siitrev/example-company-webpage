import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="The best company - Contact",layout="wide")

df = pd.read_csv("topics.csv")

with st.form("Contact"):
    email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?",options=df)
    text = st.text_area("Text")
    send = st.form_submit_button("Send")