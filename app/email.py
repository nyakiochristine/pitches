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
    send_email('Reset Password',sender=app.config['MAIL_USERNAME'],recepients=[user.email],text_body=render_template('auth/reset_password.txt',user=user, token=token),html_body=render_template('auth/reset_password.html',user=user, token=token))

