from flask_wtf import FlaskForm
from wtforms  import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    pitch= TextAreaField('Your Pitch')
    my_category= SelectField('category:', choices=[('Business', 'Business'),('Technology', 'Technology'),('Health', 'Health'),('Interview', 'Interview'),('Politics','Politics')])
    
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post your Comment')
    
    
class UpdateProfileForm(FlaskForm):
    bio= TextAreaField('Write something about yourself')
    submit = SubmitField('Submit')
    
    
