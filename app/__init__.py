import os

from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    
    return app
