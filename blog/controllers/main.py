# -*- coding:utf-8 -*-

# from blog import app
from flask import render_template,Blueprint

from ..forms.auth import SignForm

main = Blueprint("main", __name__)

@main.route('/')
def index():
    form = SignForm
    return render_template('welcome.html', title='Welcome',form=form)

@main.route('/home')
def home():
    return render_template('base.html',title='base')