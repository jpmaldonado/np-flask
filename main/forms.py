from flask_wtf import FlaskForm # Base class
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('Name please: ', validators=[DataRequired()])
    submit = SubmitField('Submit')