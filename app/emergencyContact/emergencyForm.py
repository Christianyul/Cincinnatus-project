from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField, FileField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf.file import FileField
from flask_wtf import Form


class EmergencyForm(Form):
    name = StringField('Nombres:', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('Apellidos:', validators=[InputRequired(), Length(min=3,max=50)])
    phone_mobile = StringField('Telefono Celular:', validators=[InputRequired(), Length(min=12, max=12)])
    phone_home = StringField('Telefono Hogar:', validators=[InputRequired(), Length(min=12, max=12)])
    relationship = StringField('Relacion:', validators=[InputRequired()])
    # student = IntegerField('ID estudiantes', validators=[InputRequired()])
