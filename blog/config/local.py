# -*- coding: utf-8 -*-

from .base import BaseConfig

class LocalConfig(BaseConfig):
    # DEBUG = False
    TESTING = False

    DATABASE_URLS = {
        'default': 'postgresql://lxp:lxp#555@127.0.0.1:9999/blogdb',
        'blogdb':'postgresql://liuxingpu:liuxingpu@127.0.0.1:5432/blogdb',
    }


    REDIS_URLS = {
        "default": "",
    }