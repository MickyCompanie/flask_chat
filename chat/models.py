from datetime import datetime
from chat import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	messages = db.relationship('Message', backref='author', lazy=True)

	def __str__(self):
		return self.username


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(150), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __str__(self):
		return self.id