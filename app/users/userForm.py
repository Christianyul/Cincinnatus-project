from wtforms import StringField, PasswordField, IntegerField, RadioField, validators
from wtforms.validators import *
from flask_wtf import Form


class UserForm(Form):
    name = StringField('name', validators=[InputRequired(), Length(min=3,max=30)])
    user_name = StringField('User Name', validators=[InputRequired(), Length(min=3,max=30)])
    password= PasswordField('password', validators=[InputRequired(), Length(min=3,max=30)])
    email = StringField('email', validators=[InputRequired()])
    user_type=RadioField('Label', choices=[('Admin','Admin'),('Student','Student'),('Owner','Owner')], validators=[InputRequired()])
