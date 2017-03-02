# -*- coding: utf-8 -*-

from .base import BaseConfig

class LocalConfig(BaseConfig):
    # DEBUG = False
    TESTING = False

    DATABASE_URLS = {
        'default': 'postgresql://qipai:qipai#xq5@10.133.195.48:9999/statdb',
    }


    REDIS_URLS = {
        "default": "redis://:crs-3e3gxvaw:qipai0918@10.66.152.122:6379/0",
    }