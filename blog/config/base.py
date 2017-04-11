# -*- coding: utf-8 -*-

class BaseConfig(object):

    DEBUG = True

    # Bootstrap
    BOOTSTRAP_SERVE_LOCAL = True

    # 应用私钥
    SECRET_KEY = 't(5hxsl0t*(^7v9dftc)k47cp0*miuic=4kw^1bm(iey#*z2-h'

    # Postgrsql数据库配置
    DATABASE_URLS = {
        'default': 'postgresql://lxp:123456@127.0.0.1:5432/blogdb',
    }

    # Redis数据库配置
    REDIS_URLS = {
        "default": "redis://@localhost:6379/0"
    }


    SESSION_COOKIE_NAME = 'session'



