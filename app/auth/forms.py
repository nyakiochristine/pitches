from flask_wtf import FlaskForm
from wtforms  import StringField,PasswordField,SubmitField, ValidationError,BooleanField
from wtforms.validators import  Length,Email,EqualTo,DataRequired
from ..models import User


#Registration form

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')
    
#Add custom validators
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
#Login form class that gives users access to the application features
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    
    
    
class ResetPasswordForm(FlaskForm):
    email = StringField('Email',validators = [ Email()])
    submit = SubmitField('Reset Password')
    
    
class NewPasswordForm(FlaskForm):
    password = PasswordField('Password',validators = [])
    password_repeat = PasswordField('RepeatPassword',validators = [EqualTo('password')])
    submit = SubmitField('Change Password')