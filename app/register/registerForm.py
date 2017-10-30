from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf import Form


class RegisterForm(Form):
    name = StringField('Nombre:', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('Apellidos:', validators=[InputRequired(), Length(min=3,max=50)])
    email = EmailField('Email:', validators=[InputRequired()])
    gender = RadioField('Gender:', choices=[('Masculino','Masculino'),('Femenino','Femenino')], validators=[InputRequired()])
    inscription_date = DateField('Fecha de Ingreso:', format='%Y-%m-%d', validators=[InputRequired()])

    birthdate = DateField('Fecha de nacimiento:', format='%Y-%m-%d', validators=[InputRequired()] )
    phone_mobile = StringField('Telefono Celular:', validators=[InputRequired(), Length(min=9, max=12)])
    phone_home = StringField('Telefono Hogar:', validators=[InputRequired(), Length(min=9, max=12)])
    id_document = StringField('Documento De Identidad:', validators=[InputRequired()])
    status = RadioField('Estado Actual:', choices=[('Activo','Activo'),('Retirado','Retirado'),('Terminado','Terminado')],default='Activo', validators=[InputRequired()])
    marital_status = RadioField('Estado Civil:', choices=[('Soltero','Soltero'),('Casado','Casado')],default='Soltero', validators=[InputRequired()])
    address= StringField('Direccion:', validators=[InputRequired(), Length(min=3,max=200)])

#-------------MEDICAL DATA---------------#
    alergies = StringField('Alergias:', validators=[Optional()])
    intensity = RadioField('Intensidad:', choices=[('Ninguna','Ninguna'),('Leve','Leve'),('Media','Media'),('Fuerte','Fuerte')],default="Ninguna", validators=[Optional()])
    special_condition = StringField('Condicion Especial:', validators=[Optional()])
    blood_type = RadioField('Tipo de sangre:',
    choices=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),
    ('AB+','AB+'),('AB-','AB-')], validators=[InputRequired()])
    ars = StringField('ARS:', validators=[Optional()])
    afiliation_type = StringField('Tipo de Afiliacion:',validators=[Optional()])
    policy_number = IntegerField('Numero de Poliza:',validators=[Optional()] )


#------------EMERGENCY CONTACT---------------#
    emname = StringField('Nombres:', validators=[InputRequired(), Length(min=3,max=50)])
    emlast_name = StringField('Apellidos:', validators=[InputRequired(), Length(min=3,max=50)])
    emphone_mobile = StringField('Telefono Celular:', validators=[InputRequired(), Length(min=9, max=12)])
    emphone_home = StringField('Telefono Hogar:', validators=[InputRequired(), Length(min=9, max=12)])
    relationship = StringField('Relacion con el estudiante:', validators=[InputRequired()])
