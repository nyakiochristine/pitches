from flask_wtf import FlaskForm
from wtforms  import StringField,PasswordField,SubmitField, ValidationError,BooleanField
from wtforms.validators import  Length,Email,EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your email address', validators=[Email()])
    
    username = StringField('Enter your username', validators=[])
    password = PasswordField('Password',validators = [EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [])
    submit = SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm):
    email = StringField('Your email address', validators = [Email()])
    password = PasswordField('Password',validators = [])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    
class ResetPasswordForm(FlaskForm):
    email = StringField('Email',validators = [ Email()])
    submit = SubmitField('Reset Password')
    
    
class NewPasswordForm(FlaskForm):
    password = PasswordField('Password',validators = [])
    password_repeat = PasswordField('RepeatPassword',validators = [EqualTo('password')])
    submit = SubmitField('Change Password')