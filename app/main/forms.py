from flask_wtf import FlaskForm
from wtforms  import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    pitch= TextAreaField('Your Pitch',validators=[InputRequired])
    my_category= SelectField('Your Category',validators=[InputRequired])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment',validators=[InputRequired])
    submit = SubmitField('Post your Comment')
    
    
class UpdateProfileForm(FlaskForm):
    bio= TextAreaField('Write something about yourself',validators=[InputRequired])
    submit = SubmitField('Submit')
    
    
