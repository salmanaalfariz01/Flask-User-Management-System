from os import getenv
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.getcwd(), 'instance', '.env'))

class DevelopmentConfig():
    SECRET_KEY = getenv('SECRET_KEY', 'dev_secret_key')
    SQLALCHEMY_DATABASE_URI = getenv(
        'SQLALCHEMY_DATABASE_URI',
        'mysql+pymysql://admin:123456@localhost/management'
    )
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


