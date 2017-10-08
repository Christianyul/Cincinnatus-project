from wtforms import StringField, PasswordField, IntegerField, RadioField, validators
from wtforms.validators import *
from wtforms.fields.html5 import EmailField
from flask_wtf import Form


class UserForm(Form):
    name = StringField('Nombre:', validators=[InputRequired(), Length(min=3,max=30)])
    user_name = StringField('Usuario:', validators=[InputRequired(), Length(min=3,max=30)])
    password= PasswordField('Password:', validators=[InputRequired(), Length(min=3,max=30)])
    email = EmailField('Email:', validators=[InputRequired()])
    user_type=RadioField('Tipo de Usuario', choices=[('Admin','Admin'),('Student','Student'),('Owner','Owner')], validators=[InputRequired()])
