from flask.ext.wtf import Form
from wtforms.validators import Required, Length
from wtforms import StringField, BooleanField, PasswordField, SubmitField

class SignForm(Form):
    username = StringField('username',validators=[Length(1,64)])
    password = PasswordField('password',validators=[Required()])