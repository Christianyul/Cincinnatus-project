from wtforms import StringField, PasswordField, IntegerField, validators
from wtforms.validators import *
from flask_wtf import Form

class CourseForm(Form):
    name = StringField('name', validators=[InputRequired(), Length(min=3,max=30)])
    lesson = IntegerField('lesson', validators=[InputRequired()])
    link= StringField('link', validators=[InputRequired()])
