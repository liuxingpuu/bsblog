# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for,flash
from flask import jsonify
from flask_login import login_user, logout_user, login_required, current_user

from ..forms.auth import SignForm
from ..utils.password import check_password,set_password
from blog.models.user import User

auth = Blueprint('auth',__name__)

@auth.route('/signin',methods=['GET','POST'])
def signin():
    form = SignForm()

    if form.validate_on_submit():
        user = User(form.phone_number.data.strip()).get_instance()
        if user is not None:
            if (user.check_password(raw_password=form.password.data)):
                login_user(user,form.remember_me.data)
                return redirect(url_for('main.index'))
        flash(u'用户名或者密码错误')

    return render_template('welcome.html', title='Welcome',form=form)


@auth.route('/signout',methods=['GET','POST'])
@login_required
def signout():
    logout_user()
    return redirect(url_for('auth.signin'))


@auth.route('signup',methods=['GET','POST'])
def signup():
    pass
