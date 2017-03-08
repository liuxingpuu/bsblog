from flask import Blueprint, render_template, redirect, request, url_for, flash
from ..forms.auth import SignForm

auth = Blueprint('auth',__name__)

@auth.route('/signin',methods=['GET','POST'])
def signin():
    form = SignForm()
    print form.data
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template('welcome.html', title='Welcome',form=form)


@auth.route('/signout',methods=['GET','POST'])
def signout():
    pass


@auth.route('signup',methods=['GET','POST'])
def signup():
    pass
