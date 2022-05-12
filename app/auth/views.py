from . import auth
from flask import render_template,redirect, url_for,request
import os
from .forms import RegistrationForm,LoginForm,NewPasswordForm,ResetPasswordForm
from flask_login import login_user,logout_user,current_user


@auth.route()
def login():
    LoginForm()
    title = "PLEASE LOGIN | Your Ideas Matter!"
    return render_template('auth/login.html',title=title)