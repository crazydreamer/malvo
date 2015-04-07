from flask.ext.wtf import Form
from wtforms import SubmitField


class LanguageChoice(Form):
    submit = SubmitField('Start')
