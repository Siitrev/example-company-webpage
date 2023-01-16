"""Contains two simple function. One for sending emails and second for validating the mail"""

import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header



regex =  re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def send_email(sender,password,reciever,smtp_server,smtp_port,email_message,subject):
    """It sends email to given address"""
    
    message = MIMEMultipart()
    message["To"] = Header(reciever)
    message["Subject"] = Header(subject)
    message["From"] = Header(reciever)
    message.attach(MIMEText(email_message,"plain","utf-8"))
    
    # Sending email
    
    with smtplib.SMTP(smtp_server,smtp_port) as server:
        server.starttls()
        server.ehlo
        server.login(sender,password)
        text = message.as_string()
        server.sendmail(sender,reciever,text)

def validate_email(email):
    """Validates email whether it is correct
        
        _type_: Bool
    """
    if re.fullmatch(regex,email):
        return True
    return False