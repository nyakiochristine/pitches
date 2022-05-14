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

if __name__=='__main__':
    manager.run()