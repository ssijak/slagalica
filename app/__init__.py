__author__ = 'Perun'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauthlib.client import OAuth

app = Flask(__name__)
#app.config.from_object('config')
#db = SQLAlchemy(app)
#
#oauth = OAuth(app)

from app import views, model