from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField, FileField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf.file import FileField
from flask_wtf import Form


class EmergencyForm(Form):
    name = StringField('Name:', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('Last Name:', validators=[InputRequired(), Length(min=3,max=50)])
    phone_mobile = StringField('Mobile Phone:', validators=[InputRequired(), Length(min=9, max=12)])
    phone_home = StringField('Home Phone:', validators=[InputRequired(), Length(min=9, max=12)])
    relationship = StringField('Relationship:', validators=[InputRequired()])

