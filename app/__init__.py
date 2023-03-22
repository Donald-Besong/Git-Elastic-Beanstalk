import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    from .welcome import welcome_blueprint
    app.register_blueprint(welcome_blueprint, url_prefix='/welcome')

    return app
