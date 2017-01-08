# -*- coding:utf-8 -*-

from blog import app
from flask import render_template


@app.route('/')
def index():
    return render_template('welcome.html', title='Welcome')

@app.route('/home')
def home():
    return render_template('base.html',title='base')
