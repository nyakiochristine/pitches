import os
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import text
import jwt
from . import db,login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    hash_pass = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    profile_pic_path = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    
    
    pitch = db.relationship('Pitch',backref='user',lazy='dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')
    upvotes = db.relationship('UpVote',backref='user',lazy='dynamic')
    downvotes = db.relationship('DownVote',backref='user',lazy='dynamic')
    
    
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
    
class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer, primary_key = True)
    pitch_content = db.Column(db.String())
    pitch_category = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    
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



class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer,primary_key=True)
    comment_content = db.Column(db.String())
    pitch_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id')) 
    
    
    @classmethod
    def get_comments(cls,id):
        comments= Comment
        return comments
    
    
class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitching_id = db.Column(db.Integer)
    
    
    
    
    @classmethod
    def get_upvotes(cls,id):
        upvote= Upvote
        return upvote
    
    def __repr__(self):
        return f'{self.id_user}:{self.pitching_id}'
    
class Downvote(db.Model):
    __tablename__ = 'downvotes'
    
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitching_id = db.Column(db.Integer)
    
    @classmethod
    def get_downvotes(cls,id):
        downvote= Downvote
        return downvote  
    def __repr__(self):
        return f'{self.id_user}:{self.pitching_id}'
    
