# -*- coding:utf-8 -*-

# from blog import app
from flask import render_template,Blueprint

main = Blueprint("main", __name__)

@main.route('/')
def index():
    return render_template('welcome.html', title='Welcome')

@main.route('/home')
def home():
    return render_template('base.html',title='base')