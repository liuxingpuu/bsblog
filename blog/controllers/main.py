# -*- coding:utf-8 -*-

# from blog import app
from flask import render_template,Blueprint
from flask import current_app,request
from flask_login import current_user

from ..forms.auth import SignForm
from ..utils.db import blogdb

main = Blueprint("main", __name__)

user_id = '12345678'

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
    # sql = """
    # select * from article where user_id = %s
    # """
    # blogdb.query(sql)
    return render_template('article.html')

@main.route('/photo_album')
def photo_album():
    return render_template('photo_album.html')

@main.route('/about_me')
def about_me():
    return render_template('about_me.html')

@main.route('/edit_article', methods=["GET", "POST"])
def edit_article():
    article = request.form.to_dict()
    if article:
        sql = """
        insert into article (user_id,title,tags,content) VALUES (%s,%s ,%s ,%s)
        """
        blogdb.execute(sql,user_id,article['title'],article['tags'],article['content'])
    return render_template('edit_article.html')