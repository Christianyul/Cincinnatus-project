from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf import Form


class RegisterForm(Form):
    name = StringField('Name:', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('Last Name:', validators=[InputRequired(), Length(min=3,max=50)])
    email = EmailField('Email:', validators=[InputRequired()])
    gender = RadioField('Gender:', choices=[('Male','Male'),('Female','Female')], validators=[InputRequired()])
    inscription_date = DateField('Inscription Date:', format='%Y-%m-%d', validators=[InputRequired()])

    birthdate = DateField('BirthDate:', format='%Y-%m-%d', validators=[InputRequired()] )
    phone_mobile = StringField('Mobile Phone:', validators=[InputRequired(), Length(min=9, max=12)])
    phone_home = StringField('Home Phone:', validators=[InputRequired(), Length(min=9, max=12)])
    id_document = StringField('ID Document:', validators=[InputRequired()])
    status = RadioField('Status:', choices=[('Active','Active'),('Retired','Retired'),('Finished','Finished')],default='Active', validators=[InputRequired()])
    marital_status = RadioField('Marital Status:', choices=[('Single','Single'),('Married','Married')],default='Single', validators=[InputRequired()])
    address= StringField('Address:', validators=[InputRequired(), Length(min=3,max=200)])

#-------------MEDICAL DATA---------------#
    alergies = StringField('Alergies:', validators=[Optional()])
    special_condition = StringField('Special Condition:', validators=[Optional()])
    blood_type = RadioField('Blood Type:',
    choices=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),
    ('AB+','AB+'),('AB-','AB-')], validators=[InputRequired()])
    ars = StringField('ARS:', validators=[Optional()])
    afiliation_type = StringField('Afiliation Type:',validators=[Optional()])
    policy_number = IntegerField('Policy Number:',validators=[Optional()] )


#------------EMERGENCY CONTACT---------------#
    emname = StringField('Name:', validators=[InputRequired(), Length(min=3,max=50)])
    emlast_name = StringField('Last Name:', validators=[InputRequired(), Length(min=3,max=50)])
    emphone_mobile = StringField('Mobile Phone:', validators=[InputRequired(), Length(min=9, max=12)])
    emphone_home = StringField('Home Phone:', validators=[InputRequired(), Length(min=9, max=12)])
    relationship = StringField('Relationship:', validators=[InputRequired()])
