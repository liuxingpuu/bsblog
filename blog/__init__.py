# -*- coding:utf-8 -*-
import importlib
from flask import Flask


def load_config_class(config_name):
    """导入config配置"""

    config_class_name = "%sConfig" % config_name.capitalize()

    app_name = __name__
    mod = importlib.import_module('%s.config.%s' % (app_name, config_name))
    config_class = getattr(mod, config_class_name, None)
    return config_class

def create_app(config_name):
    """创建app"""
    app = Flask(__name__)

    config_class = load_config_class(config_name)
    app.config.from_object(config_class)

    configure_blueprint(app)

    return app

def configure_blueprint(app):
    """注册初始化blueprint"""
    from .urls import routers

    for blueprint, url_prefix in routers:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
