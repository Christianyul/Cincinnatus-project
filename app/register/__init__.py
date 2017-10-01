from flask import Blueprint

# base = Blueprint('base', __name__, template_folder='templates')

RegisterRouting = Blueprint('RegisterRouting', __name__, template_folder='templates')

from . import routes
