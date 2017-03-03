# -*- coding: utf-8 -*-

from .base import BaseConfig

class WebConfig(BaseConfig):
    # DEBUG = False
    TESTING = False

    DATABASE_URLS = {
        'default': 'postgresql://qipai:qipai#xq5@10.133.195.48:9999/statdb',
        'blogdb': 'postgresql://liuxingpu:liuxingpu@127.0.0.1:5432/blogdb',
    }


    REDIS_URLS = {
        "default": "redis://:crs-3e3gxvaw:qipai0918@10.66.152.122:6379/0",
    }