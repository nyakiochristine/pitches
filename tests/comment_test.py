import unittest
from app.models import Pitch, User, Comment
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_kris = User(username='kris',password='nyakio',email='ase@edcg.com')
        self.new_pitch = Pitch(pitch_content = "This is my pitch", pitch_category='Technology',user=self.user_kris)
        self.new_comment = Comment(comment_content = "This is my comment", user=self.user_kris)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        my_user = db.session.query(User).filter(self.user.id==1).first()
        db.session.delete(my_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,"This is my comment")
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
        self.assertEquals(self.new_comment.user,self.user_kris)