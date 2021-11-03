from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import timedelta

# Flask
app = Flask(__name__, template_folder="templates", static_folder="Static")

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "xxxxxxxxxxxxxxxxxxxxxx"
app.config["SECRET_KEY"] = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
# reCAPTCHA
app.config["RECAPTCHA_USE_SSL"] = False
app.config["RECAPTCHA_PUBLIC_KEY"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
app.config["RECAPTCHA_PRIVATE_KEY"] = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
app.config["RECAPTCHA_OPTIONS"] = {"theme": "white"}
# Inactivity Logout
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes = 30)
# SQLAlchemy 
db = SQLAlchemy(app)

# Bcrypt
bcrypt = Bcrypt(app)

# Login
login_man = LoginManager(app)
login_man.login_view = "login_page"
login_man.login_message = "Ingresá con tu cuenta para poder acceder a este contenido."
login_man.login_message_category = "info"

from LogSur import routes
