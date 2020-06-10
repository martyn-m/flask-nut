import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    ''' A class to contain application configuration
    '''

    NUT_SERVER = os.environ.get('NUT_SERVER')
    NUT_PORT = os.environ.get('NUT_PORT') or 3493
    NUT_USER = os.environ.get('NUT_USER')
    NUT_PASSWORD = os.environ.get('NUT_PASSWORD')
    NUT_UPS_NAME = os.environ.get('NUT_UPS_NAME')

    # TODO: Put this in a DB or something.
    APP_USER = os.environ.get('APP_USER')
    APP_PASSWORD_HASH = os.environ.get('APP_PASSWORD_HASH')

    # Key for Flask-WTF forms for CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CorrectHorseBatteryStaple'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False