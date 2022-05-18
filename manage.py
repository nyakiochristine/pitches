from app import create_app,db
from flask import Flask
from flask_script import Manager,Server
from app.models import User,Pitch, Comment


#instance for creating the app
app = create_app('production')
manager = Manager(app)

manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch = Pitch)

@manager.command
def test():
    '''
    Run the unit test
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__=='__main__':
    manager.run()
    db.create_all()