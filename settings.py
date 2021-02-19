import os

FLASK_APP = 'run'
FLASK_ENV = os.getenv('FLASK_ENV')
DEBUG = os.getenv('DEBUG', True)
SECRET_KEY = os.getenv('SECRET_KEY')
HOST = '127.0.0.1'
PORT = 8000
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:@127.0.0.1/Treinamento"
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', True)
