from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('../config')
#app.config.from_pyfile('../config.py')

#from app import api, models