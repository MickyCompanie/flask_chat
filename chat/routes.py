from flask import render_template, url_for, flash, redirect
from chat import app, db, bcrypt
from chat.models import User, Message
from chat.forms import RegistrationForm, LoginForm, AddForm
from flask_login import login_user, current_user, logout_user


# messages = [
# {
# 'user': 'laureline',
# 'message': 'bonjour, comment vas ?'
# },
# {
# 'user': 'lena',
# 'message': 'tg'
# }
# ]


@app.route("/")
@app.route("/home")
def index():
	messages = Message.query.all()
	form = AddForm()
	return render_template('index.html', title='Home', form=form, messages=messages)


@app.route("/register", methods=["GET", "POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'account created for {form.username.data}! you can login now', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			# return redirect(url_for('index'))
		else:
			flash('Wrong username or password', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
	if current_user.is_authenticated:
		logout_user()
		return redirect(url_for('index'))
	else:
		return redirect(url_for('index'))



@app.route("/add", methods=["GET", "POST"])
def add():
	form = AddForm()
	if current_user.is_authenticated:
		message = Message(text=form.message.data, user_id=current_user.id)
		db.session.add(message)
		db.session.commit()
		return redirect(url_for('index'))
	else:
		return render_template('index.html', title='Home', messages=messages)