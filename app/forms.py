from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    number_of_bedrooms = StringField('Number of Bedrooms', validators=[DataRequired()])
    number_of_bathrooms = StringField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    type = SelectField(u'Type', choices=[('House'), ('Apartment')])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])