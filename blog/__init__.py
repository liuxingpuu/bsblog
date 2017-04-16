# -*- coding:utf-8 -*-
import importlib
import logging

from flask import Flask
from flask_login import current_user,  LoginManager

from tm.sql import DatabaseWrapper
from tm.sql import DatabaseClient

blogdb = DatabaseClient('blogdb')

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

    DatabaseWrapper.init_app(app)
    configure_blueprint(app)

    from .utils.filters import configure_template_filters
    configure_template_filters(app)
    configure_logging(app)

    return app

def configure_logging(app):
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

def configure_blueprint(app):
    """注册初始化blueprint"""
    from .urls import routers

    for blueprint, url_prefix in routers:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
