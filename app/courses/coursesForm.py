from wtforms import StringField, PasswordField, IntegerField, validators
from wtforms.validators import *
from flask_wtf import Form

class CourseForm(Form):
    name = StringField('Nombre:', validators=[InputRequired(), Length(min=3,max=30)])
    lesson = IntegerField('Cantidad de Lecciones:', validators=[InputRequired()])
    link= StringField('Link:', validators=[InputRequired()])
