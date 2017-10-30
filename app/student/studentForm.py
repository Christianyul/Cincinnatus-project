from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField, FileField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf.file import FileField
from flask_wtf import Form


class StudentForm(Form):
    name = StringField('Nombres:', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('Apellidos:', validators=[InputRequired(), Length(min=3,max=50)])
    email = EmailField('Email:', validators=[InputRequired()])
    gender = RadioField('Genero:', choices=[('Masculino','Masculino'),('Femenino','Femenino')], validators=[InputRequired()])
    inscription_date = DateField('Fecha de Ingreso:', format='%Y-%m-%d', validators=[InputRequired()])
    ending_date = DateField('Fecha de Egreso:', format='%Y-%m-%d', validators=[Optional()])
    retirement_date = DateField('Fecha de Retiro:', format='%Y-%m-%d', validators=[Optional()])
    birthdate = DateField('Fecha de nacimiento:', format='%Y-%m-%d', validators=[InputRequired()] )
    phone_mobile = StringField('Telefono Celular:', validators=[InputRequired(), Length(min=9, max=12)])
    phone_home = StringField('Telefono Hogar:', validators=[InputRequired(), Length(min=9, max=12)])
    id_document = StringField('Documento De Identidad:', validators=[InputRequired()])
    status = RadioField('Estado Actual:', choices=[('Activo','Activo'),('Retirado','Retirado'),('Terminado','Terminado')],default='Activo', validators=[InputRequired()])
    marital_status = RadioField('Estado Civil:', choices=[('Soltero','Soltero'),('Casado','Casado')],default='Soltero', validators=[InputRequired()])
    address = StringField('Direccion:', validators=[InputRequired(), Length(min=3,max=200)])
