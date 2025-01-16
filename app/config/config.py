from os import getenv
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.getcwd(), 'instance', '.env'))

class Config:
    SECRET_KEY = getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///../database/database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
