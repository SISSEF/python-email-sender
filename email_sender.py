import smtplib
from email.mime.text import MIMEText
from credentials import *

def send_email(subject, message, sender_email, sender_password, recipient_email, smtp_server, smtp_port):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        server.send_message(msg)
        server.quit()
        print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print(f"Error: Email could not be sent. {e}")

if __name__ == '__main__':
    recipient_email = input("Please enter the recipient's email address: ")
    subject = input("Please enter the subject of the email: ")
    message = input("Please enter the message: ")
    send_email(subject, message, sender_email, sender_password, recipient_email, smtp_server, smtp_port)
