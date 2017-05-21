# -*- coding: utf-8 -*-
import logging

from flask.ext.login import UserMixin

from blog.utils.db import blogdb
from blog.utils.password import check_password


class User(UserMixin):

    def __init__(self,phone_number=None,user_id=None):
        if phone_number:
            sql = "select * from user_list where phone_number = '{}'".format(phone_number)
        elif user_id:
            sql = "select * from user_list where id = '{}'".format(user_id)
        user = blogdb.get(sql)
        if user:
            self.id = user['id']
            self.user_name = user["user_name"]
            self.password = user["password"]
            self.phone_number = user['phone_number']
            self.add_time = user['created_time']
            self.avatar_file = user['avatar_file']
            self.info = user

    def get_instance(self):
        if hasattr(self, "id"):
            return self
        return None

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

