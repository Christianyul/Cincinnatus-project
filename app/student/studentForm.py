from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField, FileField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf.file import FileField
from flask_wtf import Form


class StudentForm(Form):
    name = StringField('name', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('last_name', validators=[InputRequired(), Length(min=3,max=50)])
    email = StringField('email', validators=[InputRequired()])
    image_path = FileField(u'pictures',validators=[FileAllowed(['jpg','png','svg'], 'Solo Imagenes!')])
    gender = RadioField('Genero', choices=[('Masculino','Masculino'),('Femenino','Femenino')], validators=[InputRequired()])
    inscription_date = DateField('Fecha de Ingreso (yyyy-mm-dd)', format='%Y-%m-%d')
    ending_date = DateField('Fecha de Egreso (yyyy-mm-dd)', format='%Y-%m-%d')
    retirement_date = DateField('Fecha de Retiro (yyyy-mm-dd)', format='%Y-%m-%d')
    birthdate = DateField('Digite una fecha (yyyy-mm-dd)', format='%Y-%m-%d')
    phone_mobile = StringField('Telefono Celular', validators=[InputRequired()])
    phone_home = StringField('Telefono Hogar', validators=[InputRequired()])
    id_document = StringField('Documento De Identidad', validators=[InputRequired()])
    status = RadioField('Estado Actual', choices=[('Activo','Activo'),('Retirado','Retirado'),('Terminado','Terminado')],default=Activo, validators=[InputRequired()])
    #select para los cursos
    #select para lecciones
    marital_status = RadioField('Estado Civil', choices=[('Soltero','Soltero'),('Casado','Casado')],default=Soltero, validators=[InputRequired()])
    nationality = StringField('Nacionalidad', validators=[InputRequired()])
    address= StringField('Direccion', validators=[InputRequired(), Length(min=3,max=200)])
