from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


#intialize extensions
bootstrap= Bootstrap()


#initialize app
def create_app():
    app= Flask(__name__)
    
    
    app.config.from_object(config_options[config_name])
    
    
    bootstrap.init_app(app)
    
    
    from .main import main as Blueprint
    app.register_blueprint(main_blueprint)
    
    return app
