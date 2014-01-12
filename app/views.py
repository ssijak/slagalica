__author__ = 'Perun'
from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template("main-template.html")
