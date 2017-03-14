# -*- coding:utf-8 -*-

# from blog import app
from flask import render_template,Blueprint
from flask import current_app
from flask_login import current_user

from ..forms.auth import SignForm
from ..utils.db import blogdb

main = Blueprint("main", __name__)

@main.route('/')
def welcome():
    form = SignForm()
    return render_template('welcome.html', title='Welcome',form=form)

@main.route('/index')
def index():
    return render_template('index.html',title='base')

@main.route('/home')
def home():
    return render_template('base.html',title='base')

@main.route('/article')
def article():
    pass
    sql = """
    select * from article where user_id = %s
    """
    blogdb.get(sql)
    return render_template('article.html')