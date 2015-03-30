from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(Form):
    name = StringField('Team Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    member_one_name = StringField('Name', validators=[DataRequired()])
    member_one_phone = IntegerField('Phone Number', validators=[DataRequired()])
    member_one_id = IntegerField('College ID')
    member_two_name = StringField('Name')
    member_two_phone = IntegerField('Phone Number')
    member_two_id = IntegerField('College ID')
    submit = SubmitField('Register')