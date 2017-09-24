from flask import Blueprint

# base = Blueprint('base', __name__, template_folder='templates')

MedicalRouting = Blueprint('MedicalRouting', __name__, template_folder='templates')

from . import routes
