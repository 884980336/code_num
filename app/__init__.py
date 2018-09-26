from flask import Flask
from .main import undifind

app = Flask(__name__)
app.register_blueprint(undifind.us)