from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=32)])
    submit = SubmitField('Submit')


class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired(), Length(min=8, max=256)])
    expire_date = DateField('Expire Date', validators=[DataRequired()])
    submit = SubmitField('Submit')