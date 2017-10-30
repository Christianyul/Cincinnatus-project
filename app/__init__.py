from flask import Flask
from config import config
from flask_login import LoginManager
login_manager = LoginManager()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	login_manager.init_app(app)
	login_manager.login_view = "RegisterRouting.login"
	login_manager.login_message =""


	# Configuracion de los BluePrints
	from .courses import CourseRouting as CourseRouting
	app.register_blueprint(CourseRouting)

	from .users import UserRouting as UserRouting
	app.register_blueprint(UserRouting)

	from .student import StudentRouting as StudentRouting
	app.register_blueprint(StudentRouting)

	from .emergencyContact import EmergencyRouting as EmergencyRouting
	app.register_blueprint(EmergencyRouting)

	from .medicalData import MedicalRouting as MedicalRouting
	app.register_blueprint(MedicalRouting)

	from .register import RegisterRouting as RegisterRouting
	app.register_blueprint(RegisterRouting)

	return app
