# -*- coding: utf-8 -*-

import logging



class User(object):

    def __init__(self,user_name=None):
        if user_name:
            sql = "select * from user_list where user_name = '{}'".format(user_name)
            pass