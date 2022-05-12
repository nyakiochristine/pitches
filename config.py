import os

class Config:
    '''
    general configuration
    '''
    
    
    @staticmethod
    def init_app(app):
        pass
    


class ProdConfig(Config):
    
    '''
    Production configuration child class
    
    
    '''
    
class DevConfig(Config):
   
    '''
    Development configuration child class
    '''
    
config_options ={
    'development':DevConfig,
    'production':ProdConfig,
}

