from flask import Flask
from flask_mail import Mail 
from .config import Config
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)

mail = Mail(app)
csrf.init_app(app)
from app import views