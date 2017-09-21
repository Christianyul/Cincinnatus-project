from flask import Blueprint

# base = Blueprint('base', __name__, template_folder='templates')

StudentRouting = Blueprint('StudentRouting', __name__, template_folder='templates')

from . import routes
