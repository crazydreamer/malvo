from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(Form):
    name = StringField('Team Name', validators=[DataRequired()])
    member_one = StringField('Member one\' name', validators=[DataRequired()])
    member_one_id = IntegerField('Member one\'s id', validators=[DataRequired()])
    member_one_phone = IntegerField('Member one\'s phone', validators=[DataRequired()])
    member_two = StringField('Member two\' name')
    member_two_id = IntegerField('Member two\'s id')
    member_two_phone = IntegerField('Member two\'s phone')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')