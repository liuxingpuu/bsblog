# -*- coding:utf-8 -*-

# from blog import app
from flask import render_template,Blueprint
from flask import current_app,request,jsonify
from flask_login import current_user

from ..forms.auth import SignForm
from ..utils.db import blogdb
from ..utils.qiniu import qiniu_lib

main = Blueprint("main", __name__)

user_id = '12345678'

@main.route('/')
def welcome():
    form = SignForm()
    return render_template('welcome.html', title='Welcome',form=form)

@main.route('/index')
def index():
    sql = """
    select *,to_char(created_time,'YYYY-MM-DD HH24:MI:SS') as created_time from article where user_id = %s
    """
    objs = blogdb.query(sql,user_id)
    return render_template('index.html',title='base',objs=objs)

@main.route('/home')
def home():
    return render_template('base.html',title='base')

@main.route('/article')
def article():
    article_id = request.args.get('article_id',None)
    sql = """
    select *,to_char(created_time,'YYYY-MM-DD HH24:MI:SS') as created_time from article where user_id = %s and id =%s
    """
    objs = blogdb.query(sql,user_id,article_id)
    return render_template('article.html',objs=objs)

@main.route("/article_list")
def article_list():
    sql = """
    select *,to_char(created_time,'YYYY-MM-DD HH24:MI:SS') as created_time from article where user_id = %s
    """
    objs = blogdb.query(sql,user_id)
    return render_template('article_list.html',objs=objs)

@main.route('/photo_album')
def photo_album():
    objs = blogdb.query("select photo_url from photo_album where user_id =%s",user_id)
    photos = [objs[i:i+4] for i in range(0,len(objs),4)]
    return render_template('photo_album.html',photos=photos)

@main.route('/img_upload', methods=["GET", "POST"])
def img_upload():
    img_file = request.files.get('img_url')
    upload = qiniu_lib(access_key="3tp3FnwQn_jamkXiQE3HlOwHnItkyd2b_N6i2BMH",
                       secret_key="xogHUWGjKMKaQ5BY8ULNuSglPVYLCgICp9hDR7tT")

    if img_file:
        result = upload.upload(upload_file=img_file,bucket_name='qipai-activity', file_type='img')
    else:
        result = {"status":2, "errmsg":u"文件上传出错"}
    if result['status'] != 1:
        current_app.logger.error('ttt%s' % (result))

        return render_template("img_upload.html")
    img_url = result['file_url']
    blogdb.execute("insert into photo_album (user_id,photo_url) VALUES (%s,%s)",user_id,img_url)
    return render_template('img_upload.html')

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