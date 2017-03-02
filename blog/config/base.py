# -*- coding: utf-8 -*-

class BaseConfig(object):

    DEBUG = True

    # Bootstrap
    BOOTSTRAP_SERVE_LOCAL = True

    # 应用私钥
    SECRET_KEY = 't(5hxsl0t*(^7v9dftc)k47cp0*miuic=4kw^1bm(iey#*z2-h'

    # Postgrsql数据库配置
    DATABASE_URLS = {
        'default': 'postgresql://echo:123456@127.0.0.1:5432/qipaiopdb',
    }

    # Redis数据库配置
    REDIS_URLS = {
        "default": "redis://@localhost:6379/0"
    }

    # Session以及Cookie配置
    # DEFAULT_DOMAIN = 'http://www.zonst.com/'
    # COOKIE_DOMAIN = ".admin.zonst.com"
    # COOKIE_MAX_AGE = 24*60*60
    #
    # SESSION_COOKIE_DOMAIN = ".admin.zonst.com"
    SESSION_COOKIE_NAME = 'session'


    # 统一账号接口
    # RBAC_SITE_ID = 1
    # RBAC_SECRET_KEY = "d93d3fef-c354-4ed4-b781-b6402ff1bc03"
    #
    # RBAC_USER_SALT_URL = 'http://rbac.api.xq5.com/auth/salt'
    # RBAC_USER_DATA_URL = "http://rbac.api.xq5.com/auth/login"
    # PUSH_ADDRESS = 'http://localhost:12000/'
