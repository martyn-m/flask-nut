from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from ups import Ups

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

ups = Ups(host=app.config['NUT_SERVER'],
                  port=app.config['NUT_PORT'],
                  login=app.config['NUT_USER'],
                  password=app.config['NUT_PASSWORD'],
)

from app import routes, models