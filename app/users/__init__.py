from flask import Blueprint

# base = Blueprint('base', __name__, template_folder='templates')

UserRouting = Blueprint('UserRouting', __name__, template_folder='templates')

from . import routes
