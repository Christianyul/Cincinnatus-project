from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField, FileField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf.file import FileField
from flask_wtf import Form


class RegisterForm(Form):
    name = StringField('name', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('last_name', validators=[InputRequired(), Length(min=3,max=50)])
    email = StringField('email', validators=[InputRequired()])
    gender = RadioField('gender', choices=[('Masculino','Masculino'),('Femenino','Femenino')], validators=[InputRequired()])
    inscription_date = DateField('Fecha de Ingreso (yyyy-mm-dd)', format='%Y-%m-%d', validators=[InputRequired()])
    ending_date = DateField('Fecha de Egreso (yyyy-mm-dd)', format='%Y-%m-%d', validators=[Optional()])
    retirement_date = DateField('Fecha de Retiro (yyyy-mm-dd)', format='%Y-%m-%d', validators=[Optional()])
    birthdate = DateField('Fecha de nacimiento (yyyy-mm-dd)', format='%Y-%m-%d', validators=[InputRequired()] )
    phone_mobile = StringField('Telefono Celular', validators=[InputRequired()])
    phone_home = StringField('Telefono Hogar', validators=[InputRequired()])
    id_document = StringField('Documento De Identidad', validators=[InputRequired()])
    status = RadioField('Estado Actual', choices=[('Activo','Activo'),('Retirado','Retirado'),('Terminado','Terminado')],default='Activo', validators=[InputRequired()])
    #select para los cursos
    #select para lecciones
    #input de arhivo para imagenes
    marital_status = RadioField('Estado Civil', choices=[('Soltero','Soltero'),('Casado','Casado')],default='Soltero', validators=[InputRequired()])
    nationality = StringField('Nacionalidad', validators=[InputRequired()])
    address= StringField('Direccion', validators=[InputRequired(), Length(min=3,max=200)])

#-------------MEDICAL DATA---------------#
    alergies = StringField('Alergies')
    intensity = RadioField('Intensidad', choices=[('Ninguna','Ninguna'),('Leve','Leve'),('Media','Media'),('Fuerte','Fuerte')],default='Ninguna',validators=[Optional()])
    special_condition = StringField('Condicion Especial', validators=[Optional()])
    blood_type = RadioField('Tipo de sangre',
    choices=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),
    ('AB+','AB+'),('AB-','AB-')], default='A+', validators=[InputRequired()])

    ars = StringField('ARS',)
    afiliation_type = StringField('Tipo de Afiliacion',validators=[Optional()])
    policy_number = IntegerField('Numero de Poliza',validators=[Optional()] )



#------------EMERGENCY CONTACT---------------#
    emname = StringField('name', validators=[InputRequired(), Length(min=3,max=50)])
    emlast_name = StringField('last_name', validators=[InputRequired(), Length(min=3,max=50)])
    emphone_mobile = StringField('Telefono Celular', validators=[InputRequired()])
    emphone_home = StringField('Telefono Hogar', validators=[InputRequired()])
    relationship = StringField('Relacion', validators=[InputRequired()])
    # student = IntegerField('ID estudiantes', validators=[InputRequired()])
