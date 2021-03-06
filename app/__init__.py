from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options, DevConfig
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_simplemde import SimpleMDE


login_manager =LoginManager()
login_manager.session_protection = 'strong'
login_manager_view = 'auth.login'

#intialize extensions
bootstrap= Bootstrap()
db=SQLAlchemy()
mail= Mail()
simple = SimpleMDE



#initialize app
def create_app(config_name):
    app= Flask(__name__)
    
    
    app.config.from_object(config_options[config_name])
    
    
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    app.config.from_object(DevConfig)
    
    
    #registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')
    
    return app
