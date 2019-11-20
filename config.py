from os import environ

class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = 'this_is_the_s3cret_k3y'
    FLASK_APP = 'run'
    FLASK_ENV = 'development'
    DEBUG = True

    # Specific Config
    MODEL_FILE = 'model.plk'