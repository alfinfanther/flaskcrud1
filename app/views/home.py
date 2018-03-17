from flask import Blueprint
from flask import abort, render_template

home = Blueprint('home', __name__)

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")