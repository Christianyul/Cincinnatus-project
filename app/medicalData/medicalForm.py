from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf import Form


class MedicalForm(Form):
    alergies = StringField('Alergias:', validators=[Optional()])
    intensity = RadioField('Intensidad:', choices=[('Ninguna','Ninguna'),('Leve','Leve'),('Media','Media'),('Fuerte','Fuerte')],default="Ninguna", validators=[Optional()])
    special_condition = StringField('Condicion Especial:', validators=[Optional()])
    blood_type = RadioField('Tipo de sangre:',
    choices=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),
    ('AB+','AB+'),('AB-','AB-')], validators=[InputRequired()])
    ars = StringField('ARS:', validators=[Optional()])
    afiliation_type = StringField('Tipo de Afiliacion:',validators=[Optional()])
    policy_number = IntegerField('Numero de Poliza:',validators=[Optional()] )
