from flask import Blueprint

# base = Blueprint('base', __name__, template_folder='templates')

CourseRouting = Blueprint('CourseRouting', __name__, template_folder='templates')

from . import routes
