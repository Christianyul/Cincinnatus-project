from wtforms import StringField, PasswordField, IntegerField, RadioField, validators, DateField, SelectField, FileField
from wtforms.validators import *
from wtforms.fields.html5 import DateField, EmailField
from flask_wtf.file import FileField
from flask_wtf import Form


class StudentForm(Form):
    name = StringField('Name:', validators=[InputRequired(), Length(min=3,max=50)])
    last_name = StringField('Last Name:', validators=[InputRequired(), Length(min=3,max=50)])
    email = EmailField('Email:', validators=[InputRequired()])
    gender = RadioField('Gender:', choices=[('Male','Male'),('Female','Female')], validators=[InputRequired()])
    inscription_date = DateField('Inscription Date:', format='%Y-%m-%d', validators=[InputRequired()])
    ending_date = DateField('Ending Date:', format='%Y-%m-%d', validators=[Optional()])
    retirement_date = DateField('Retirement Date:', format='%Y-%m-%d', validators=[Optional()])
    birthdate = DateField('Birthdate:', format='%Y-%m-%d', validators=[InputRequired()] )
    phone_mobile = StringField('Mobile Phone:', validators=[InputRequired(), Length(min=9, max=12)])
    phone_home = StringField('Mobile Home:', validators=[InputRequired(), Length(min=9, max=12)])
    id_document = StringField('ID Document:', validators=[InputRequired(), Length(min=12, max=12)])
    status = RadioField('Status:', choices=[('Active','Active'),('Retirement','Retirement'),('Finished','Finished')],default='Active', validators=[InputRequired()])
    marital_status = RadioField('Marital Status:', choices=[('Single','Single'),('Married','Married')],default='Single', validators=[InputRequired()])
    address = StringField('Address:', validators=[InputRequired(), Length(min=3,max=200)])
