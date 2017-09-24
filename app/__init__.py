from flask import Flask
from config import config

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	# Configuracion de los BluePrints
	from .courses import CourseRouting as CourseRouting
	app.register_blueprint(CourseRouting)

	from .users import UserRouting as UserRouting
	app.register_blueprint(UserRouting)

	from .student import StudentRouting as StudentRouting
	app.register_blueprint(StudentRouting)

	from .emergencyContact import EmergencyRouting as EmergencyRouting
	app.register_blueprint(EmergencyRouting)

	return app
