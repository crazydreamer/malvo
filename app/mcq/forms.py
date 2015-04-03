from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, Optional


class LanguageChoice(Form):
    language = RadioField('Language Choice', choices=[('c', 'C Programming Language'), ('java', 'Java')], validators=[DataRequired()])
    submit = SubmitField('Start')
