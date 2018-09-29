from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask.ext.mail import Mail


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object("settings.UseSetting")
from login.auth import Auth
auth = Auth(app)
email = Mail(app)

from .main import undifind
Session(app)

db.init_app(app)
app.register_blueprint(undifind.us)