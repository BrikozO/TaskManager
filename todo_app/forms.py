from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo

from .forms_custom_validators import DateCheck
from .models import User


class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=32)])
    submit = SubmitField('Submit')


class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=32)])
    password_repeat = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username already exists!")


class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired(), Length(min=8, max=256)])
    expire_date = DateField('Expire Date', validators=[DataRequired(), DateCheck()])
    submit = SubmitField('Submit')
