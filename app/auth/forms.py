from flask_wtf import FlaskForm
from wtforms  import StringField,PasswordField,SubmitField, ValidationError,BooleanField
from wtforms.validators import input_required, Length,Email,EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your email address', validators=[input_required(),Email()])
    
    username = StringField('Enter your username', validators=[input_required()])
    password = PasswordField('Password',validators = [input_required(),EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [input_required])
    submit = SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm):
    email = StringField('Your email address', validators = [input_required(),Email()])
    password = PasswordField('Password',validators = [input_required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    
class ResetPasswordForm(FlaskForm):
    email = StringField('Email',validators = [input_required(), Email()])
    submit = SubmitField('Reset Password')
    
    
class NewPasswordForm(FlaskForm):
    password = PasswordField('Password',validators = [input_required()])
    password_repeat = PasswordField('RepeatPassword',validators = [input_required(),EqualTo('password')])
    submit = SubmitField('Change Password')