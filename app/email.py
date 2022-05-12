from manage  import app
from flask_mail import Message
from flask import render_template
import os
from . import mail


def send_email(subject,sender, recipients,text_body,html_body):
    msg = Message(subject,sender=sender,recipients=recipients)
    msg.body = text_body
    msg.html= html_body
    mail.send(msg)
    
    
def send_reset_email(user):
    token = user.reset_password_token()
    send_email(user.email)
