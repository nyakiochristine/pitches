import os
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import text


class User(UserMixin):
    
    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")
    
    @password.setter
    def password(self, password):
        self.hash_pass= generate_password_hash(password)
        
    def set_password(self, password):
        self.hash_pass= generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.hash_pass,password)

    def _repr_(self):
        return f'User {self.username}'
    
class Pitch():
    
    
    @classmethod
    def get_pitch(cls,id):
        pitches = Pitch.query.filter_by(id=id).all()
        return pitches
    
    @classmethod
    def get_all_pitches(cls):
        pitches = Pitch.query.order_by(text('-id')).all()
        return pitches
    
    @classmethod
    def get_category(cls, cat):
        category = Pitch.query.filter_by(pitch_category = cat).order_by(text('-id')).all()
        
        return category        
    


