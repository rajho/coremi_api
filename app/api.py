#!venv/bin/python
from flask import Flask

import models

#from app import app

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return "Hello World!"

if __name__ =- '__main__':
	models.initialize()
	app.run(debug=DEBUG, host=HOST, port=PORT)