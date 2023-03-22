from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

welcome_blueprint = Blueprint('welcome', __name__)


@welcome_blueprint.route('/', methods=['GET', 'POST'])
def welcome():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Continuous Delivery Demo"
