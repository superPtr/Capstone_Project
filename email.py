####Configure SMTP server and create a send message function####

import smtplib
from email.message import EmailMessage
import os

def configure_email(subject, body, to_email, from_email, smtp_server, port, login, password):
    #create the email message
    email = EmailMessage()
    email.set_content(body)
    email['Subject'] = subject
    email['From'] = from_email
    email['To'] = to_email

    try:
        #connect to an SMTP server
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  #secure the connection
            server.login(login, password)  #log in to the SMTP server
            server.send_message(email)  #send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")#debugging

def send_email(gmail, content, subject):
    configure_email(
        subject= subject,
        body= content,        
        to_email= gmail,
        from_email="IT Devices Suggestion System",
        smtp_server="smtp.gmail.com",
        port=587,
        login="custucct1013@gmail.com",
        password=os.environ['YOUR_EMAIL_KEY']
        )

send_email('cqyyy1018@gmail.com','hi', 'Your quote')