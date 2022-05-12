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


