from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField, FileField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf.file import FileField
from flask_wtf import Form


class EmergencyForm(Form):
    name = StringField('name', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('last_name', validators=[InputRequired(), Length(min=3,max=50)])
    phone_mobile = StringField('Telefono Celular', validators=[InputRequired()])
    phone_home = StringField('Telefono Hogar', validators=[InputRequired()])
    relationship = StringField('Relacion', validators=[InputRequired()])
    # student = IntegerField('ID estudiantes', validators=[InputRequired()])
