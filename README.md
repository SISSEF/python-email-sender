# Python Email Sender

Send emails automatically using most email service providers with this simple script in Python!

## Overview
The two modules used in this script are *smtplib* and *email.mime.text*.

- `smtplib` is a Python standard library module that provides an implementation of the Simple Mail Transfer Protocol (SMTP) for sending email messages. It is used to send email messages over the Internet, using an SMTP server.
- `email.mime.text` is a module within the email package, which is also part of the Python standard library. It provides the `MIMEText` class, which is used to create plain text email messages. The `MIMEText` class takes the plain text message as an argument and creates an email message object, which can then be sent using an `smtplib` SMTP server.

## Usage
To use this email sender, you'll need the following information:

   - The address of the SMTP server you'll be using.
   - The port number used by the SMTP server.
   - Your email account credentials.

Follow these steps to run the email sender:

    1. Enter your email,password and SMTP Server information in the credentials.py file.
    2. Make sure both credentials.py and email_sender.py are in the same directory.
    3. Run the email_sender.py file."

## Cloning / Forking
This repositorie is licensed under a MIT [LICENSE].
