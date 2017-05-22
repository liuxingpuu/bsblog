# -*- coding:utf-8 -*-

# from blog import app
from flask import render_template,Blueprint,url_for
from flask import current_app,request,jsonify,redirect
from flask_login import current_user
from flask.ext.login import login_required

from ..forms.auth import SignForm,AddNoticeForm
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
    select *,to_char(created_time,'YYYY-MM-DD HH24:MI:SS') as time from article where user_id = %s
    order by created_time desc limit 10
    """
    objs = blogdb.query(sql,user_id)
    return render_template('index.html',title='base',objs=objs)

@main.route('/notice',methods=['GET','POST'])
def notice():
    obj = blogdb.get('select * from notice where is_show =1')
    if obj:
        return jsonify({'errno':0,'errmsg':obj['notice']})
    else:
        return jsonify({'errno':1,'errmsg':u'暂无公告'})

@main.route('/add_notice',methods=['GET','POST'])
@login_required
def add_notice():
    objs = blogdb.query("select *,to_char(created_time,'YYYY-MM-DD HH24:MI:SS') as created_time from notice order by id")
    form = AddNoticeForm()
    if form.validate_on_submit():

        sql = """
        insert into notice (notice) VALUES (%s)
        """
        blogdb.execute(sql,form.notice.data)
        return redirect(url_for('main.add_notice'))
    return render_template('add_notice.html',form=form,objs=objs)

@main.route('/delete_notice',methods=['GET','POST'])
@login_required
def delete_notice():
    id = request.args.get('id')
    blogdb.execute('delete from notice where id=%s',id)
    return redirect(url_for('main.add_notice'))

@main.route('/show_notice')
@login_required
def show_notice():
    id = request.args.get('id')
    is_show = request.args.get('is_show')
    blogdb.execute('update notice set is_show=%s where id=%s',is_show,id)
    blogdb.execute('update notice set is_show=0 where id !=%s',id)
    return redirect(url_for('main.add_notice'))

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

@main.route('/latest_article',methods=['GET','POST'])
def latest_article():
    objs = blogdb.query("select id,title,tags from article order by created_time desc limit 3")
    if objs:
        return jsonify({'errno':0,'errmsg':objs})
    else:
        return jsonify({'errno':1,'errmsg':u'暂无新的文章'})

@main.route('/photo_album')
def photo_album():
    objs = blogdb.query("select id,photo_url from photo_album where user_id =%s",user_id)
    photos = [objs[i:i+4] for i in range(0,len(objs),4)]
    return render_template('photo_album.html',photos=photos)

@main.route('/delete_photo', methods=["GET", "POST"])
@login_required
def delete_photo():
    id = request.args.get('id')
    blogdb.execute('delete from photo_album where id=%s',id)
    return redirect(url_for('main.photo_album'))

@main.route('/img_upload', methods=["GET", "POST"])
@login_required
def img_upload():
    img_file = request.files.get('img_url')
    upload = qiniu_lib(access_key="3tp3FnwQn_jamkXiQE3HlOwHnItkyd2b_N6i2BMH",
                       secret_key="xogHUWGjKMKaQ5BY8ULNuSglPVYLCgICp9hDR7tT")

    if img_file:
        result = upload.upload(upload_file=img_file,bucket_name='qipai-activity', file_type='img')
        if result['status'] != 1:
            current_app.logger.error('ttt%s' % (result))

            return render_template("img_upload.html")
        img_url = result['file_url']
        blogdb.execute("insert into photo_album (user_id,photo_url) VALUES (%s,%s)",user_id,img_url)
        return redirect(url_for('main.photo_album'))
    return render_template('img_upload.html')

@main.route('/about_me')
def about_me():
    return render_template('about_me.html')

@main.route('/add_article', methods=["GET", "POST"])
@login_required
def add_article():
    article = request.form.to_dict()
    if article:
        sql = """
        insert into article (user_id,title,tags,content) VALUES (%s,%s ,%s ,%s)
        """
        blogdb.execute(sql,user_id,article['title'],article['tags'],article['content'])
        return redirect(url_for('main.article_list'))
    return render_template('add_article.html')

@main.route('/edit_article',methods=["GET", "POST"])
@login_required
def edit_article():
    article_id = request.args.get('article_id')
    obj = blogdb.get('select * from article where id=%s',article_id)
    article = request.form.to_dict()
    if article:
        sql = """
        update article set title=%s,tags=%s,content=%s,modify_time=CURRENT_TIMESTAMP where id=%s
        """
        blogdb.execute(sql,article['title'],article['tags'],article['content'],article_id)
        return redirect(url_for('main.article_list'))
    return render_template('edit_article.html',article_id=article_id,obj=obj)

@main.route('/delete_article', methods=["GET", "POST"])
@login_required
def delete_article():
    article_id = request.args.get('article_id')
    blogdb.execute("delete from article where id=%s",article_id)
    return redirect(url_for('main.article_list'))