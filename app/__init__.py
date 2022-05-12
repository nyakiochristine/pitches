from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options, DevConfig


#intialize extensions
bootstrap= Bootstrap()


#initialize app
def create_app(config_name):
    app= Flask(__name__)
    
    
    app.config.from_object(config_options[config_name])
    
    
    bootstrap.init_app(app)
    
    app.config.from_object(DevConfig)
    
    
    #registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    
    
    return app
