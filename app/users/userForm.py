from wtforms import StringField, PasswordField, IntegerField, RadioField, validators
from wtforms.validators import *
from wtforms.fields.html5 import EmailField
from flask_wtf import Form


class UserForm(Form):
    name = StringField('Name:', validators=[InputRequired(), Length(min=3,max=30)])
    user_name = StringField('User Name:', validators=[InputRequired(), Length(min=3,max=30)])
    password= PasswordField('Password:', validators=[InputRequired(), Length(min=3,max=30)])
    email = EmailField('Email:', validators=[InputRequired()])
    user_type=RadioField('User Type', choices=[('Admin','Admin'),('Student','Student')], validators=[InputRequired()])
