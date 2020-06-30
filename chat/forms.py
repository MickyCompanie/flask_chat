from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from chat.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	password = StringField('Password', validators=[DataRequired()])
	confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('This unsername is already taken')


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	password = StringField('Password', validators=[DataRequired()])
	remember = BooleanField('remember me')
	submit = SubmitField('Login')

class AddForm(FlaskForm):
	message = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
	submit = SubmitField('Submit')