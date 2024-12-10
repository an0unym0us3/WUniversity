import os
from email.message import EmailMessage
import ssl
import smtplib

sender = 'edulink.applicationhub@gmail.com'
password = 'vsnd fbdm ozqw mljo'
reciever = 's2014193@iisjapan.com'

sub = 'Hi!'
body = '''Just get this bot working already...
'''

mail = EmailMessage()
mail['From'] = sender
mail['To'] = reciever
mail['Subject'] = sub
mail.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, reciever, mail.as_string())
