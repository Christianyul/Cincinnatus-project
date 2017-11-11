from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf import Form


class MedicalForm(Form):
    alergies = StringField('Alergies:', validators=[Optional()])
    special_condition = StringField('Special Condition:', validators=[Optional()])
    blood_type = RadioField('Blood Type:',
    choices=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),
    ('AB+','AB+'),('AB-','AB-')], validators=[InputRequired()])
    ars = StringField('ARS:', validators=[Optional()])
    afiliation_type = StringField('Afiliation Type:',validators=[Optional()])
    policy_number = IntegerField('Policy Number:',validators=[Optional()] )
