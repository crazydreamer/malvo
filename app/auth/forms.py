from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SubmitField, \
    RadioField
from wtforms.validators import DataRequired, Optional


class RegistrationForm(Form):
    name = StringField('Team Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    language = RadioField(
        'Preferred Language', choices=[('c', 'C'), ('java', 'Java')],
        validators=[DataRequired()]
    )
    member_one_name = StringField('Name', validators=[DataRequired()])
    member_one_phone = IntegerField('Phone Number', validators=[DataRequired()])
    member_one_id = StringField('College ID', validators=[Optional()])
    member_two_name = StringField('Name', validators=[Optional()])
    member_two_phone = IntegerField('Phone Number', validators=[Optional()])
    member_two_id = StringField('College ID', validators=[Optional()])
    submit = SubmitField('Register')


class LoginForm(Form):
    team_name = StringField('Team Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
