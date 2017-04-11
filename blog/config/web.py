# -*- coding: utf-8 -*-

from .base import BaseConfig

class WebConfig(BaseConfig):
    # DEBUG = False
    TESTING = False

    DATABASE_URLS = {
        'default': 'postgresql://lxp:lxp#555@127.0.0.1:9999/blogdb',
        'blogdb': 'postgresql://liuxingpu:liuxingpu@localhost:5432/blogdb',
    }


    REDIS_URLS = {
        "default": "",
    }