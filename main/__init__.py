from flask import Flask
from flask_sqlalchemy import *



app = Flask(__name__)
app.config['SECRET_KEY'] = '84hfurh98fhwhe89ihds98yh93wh9dha8deh89weh9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from main import routs