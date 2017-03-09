# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for

from ..forms.auth import SignForm
from ..utils.password import check_password,set_password

auth = Blueprint('auth',__name__)

@auth.route('/signin',methods=['GET','POST'])
def signin():
    form = SignForm()

    if form.validate_on_submit():

        return redirect(url_for('main.home'))
    return render_template('welcome.html', title='Welcome',form=form)


@auth.route('/signout',methods=['GET','POST'])
def signout():
    pass


@auth.route('signup',methods=['GET','POST'])
def signup():
    pass
