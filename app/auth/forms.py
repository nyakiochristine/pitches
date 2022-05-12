from flask_wtf import FlaskForm
from wtforms  import StringField,PasswordField,SubmitField, ValidationError,BooleanField
from wtforms.validators import Required, Length,Email


class RegistrationForm(FlaskForm):
    email = StringField
    username = StringField
    password = PasswordField
    password_confirm = PasswordField
    submit = SubmitField
    
    
class LoginForm(FlaskForm):
    email = StringField
    password = PasswordField
    remember = BooleanField
    submit = SubmitField
    
class ResetPasswordForm(FlaskForm):
    email = StringField
    submit = SubmitField
    
    
class NewPasswordForm(FlaskForm):
    password = PasswordField
    password_repeat = PasswordField
    submit = SubmitField