from flask_wtf import FlaskForm # Base class
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    role = SelectField('Role: ', validators=[DataRequired()], choices=['Admin','Guest'])
    submit = SubmitField('Submit')