from flask import Flask
from flask import jsonify

from app import create_app
application = create_app()


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
