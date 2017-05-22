from flask.ext.wtf import Form
from wtforms.validators import Required, Length
from wtforms import StringField, BooleanField, PasswordField, SubmitField

class SignForm(Form):
    phone_number = StringField('phone_number',validators=[Length(1,64)])
    password = PasswordField('password',validators=[Required()])

class AddNoticeForm(Form):
    notice = StringField('notice')