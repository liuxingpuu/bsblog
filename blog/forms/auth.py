from flask.ext.wtf import Form
from wtforms.validators import Required, Length
from wtforms import StringField, BooleanField, PasswordField, SubmitField

class SignForm(Form):
    username = StringField('username',validators=[Required,Length(1,64)])
    password = StringField('password',validators=Required)
    submit = SubmitField('Log In')