from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import NumberRange, InputRequired
from flask import Flask
from werkzeug.utils import secure_filename
import os

class AddForm(FlaskForm):
    proptitle = StringField('Property Title', validators=[InputRequired()])

    description = TextAreaField('Description', validators=[InputRequired()])

    number_of_rooms = IntegerField('No. of Rooms', validators=[InputRequired(), NumberRange(min=1)])

    price = IntegerField('Price', validators=[InputRequired(), NumberRange(min=1)])

    location = StringField('Location', validators=[InputRequired()])

    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images Only!')])
    
    number_of_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired(), NumberRange(min=1)])

    property_type = SelectField('Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[InputRequired()])