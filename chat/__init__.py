from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ed39afc11dcf3c94d1ba06c68cb78f47'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../chat.db' # /// means it's a relative path
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from chat import routes