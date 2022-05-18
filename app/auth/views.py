from . import auth
from flask import render_template,redirect, url_for,request
import os
from .forms import RegistrationForm,LoginForm,NewPasswordForm,ResetPasswordForm
from flask_login import login_user,logout_user,current_user


@auth.route('/login',methods=['GET', 'POST'])
def login():
    form= LoginForm()
    title = "PLEASE LOGIN | Your Ideas Matter!"
    return render_template('auth/login.html',title=title,form=form)

@auth.route('/register')
def register():
    RegistrationForm()
    title = "Sign up for new ACCOUNT! | Welcome!"
    return render_template('auth/register.html',title=title)


@auth.route('/reset')
def reset_password():
    ResetPasswordForm()
    title = "RESET PASSWORD | Your Ideas Matter!"
    return render_template('auth/reset.html',title=title)

@auth.route('/new password/<token>')
def new_password():
    LoginForm()
    title = "PLEASE LOGIN | Your Ideas Matter!"
    return render_template('auth/change_password.html',title=title)


