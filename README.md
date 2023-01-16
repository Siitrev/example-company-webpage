# example-company-webpage
Webapp made in streamlit as one of excercises in uni. It is a example sketch of a company website with a working contact page.
If you want a "Contact Us" page work you need to create ".env" file in the same folder and then fill it with correct data:
  SENDER_ADDRESS="email address" - from this email, content of a form will be sent to you
  PORT=587 - port on which smtp works 
  SMTP_SERVER_ADDRESS="server addres" - it can be sth like "smtp.gmail.com" or other options
  SENDER_PASSWORD="app password" - this is special key that allows this script to send mail via mail
  RECIEVER_ADDRESS="your email" - on this email content of a form will be sent
