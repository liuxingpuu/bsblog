from flask.ext.wtf import Form
from wtforms.validators import Required, Length
from wtforms import StringField, BooleanField, PasswordField, SubmitField

class LoginForm(Form):
    username = StringField('username',validators=[Required,Length(1,64)])
    password = PasswordField('password',validators=Required)
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')