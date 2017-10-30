
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired


class LoginForm(Form):
    user = StringField('User', validators=[InputRequired()])
    password= PasswordField('Password', validators=[InputRequired()])