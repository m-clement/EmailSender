from email.message import EmailMessage
from user_info import *
import ssl
import smtplib

email_sender = email
email_password = password

# Input email details here
email_receiver = ""
subject = "Hello World!"
body = """
First code, a greeting,
'Hello, World!' on screen appears,
New journey begins.
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

