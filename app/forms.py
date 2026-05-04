from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class TodoForm(FlaskForm):
    task = StringField('Enter your task', validators=[DataRequired()])
    submit = SubmitField('Enter')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')