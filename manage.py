from app import create_app
from flask import Flask
from flask_script import Manager,Server


#instance for creating the app
app = create_app('production')
manager = Manager(app)

manager.add_command('server', Server)

if __name__=='__main__':
    manager.run()