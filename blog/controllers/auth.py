from flask import Blueprint, render_template, redirect, request, url_for, flash
from ..forms.auth import LoginForm

auth = Blueprint('auth',__name__)

@auth.route('/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
