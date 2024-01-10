from wtforms.validators import DataRequired, EqualTo
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from flask_wtf import FlaskForm


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    password2 = StringField('Password again)', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registration')


class Log_in(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Log_in')


class Profile(FlaskForm):
    but_logout = SubmitField('log out of profile')
    but_active = SubmitField('Issue random activity')