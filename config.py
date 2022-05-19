import os

class Config:
    '''
    general configuration
    '''
    SECRET_KEY = 'thisisme'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    
    
    
    MAIL_SERVER=os.environ.get('MAIL_SERVER')
    MAIL_PORT=os.environ.get('MAIL_PORT')
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    
    
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    @staticmethod
    def init_app(app):
        pass
    


class ProdConfig(Config):
    
    '''
    Production configuration child class
    
    
    '''
    pass
    
class DevConfig(Config):
   
    '''
    Development configuration child class
    '''
    
    DEBUG= True
    
config_options ={
    'development':DevConfig,
    'production':ProdConfig,
}

