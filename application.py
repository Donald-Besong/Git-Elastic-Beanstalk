from flask import Flask
from flask import jsonify

from app import create_app
application = create_app()


@application.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Continuous Delivery Demo"


@application.route("/echo/<name>")
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
