# -*- coding:utf-8 -*-
import os
import logging

from flask.ext.script import Manager, Server
from blog import create_app

# 配置日志
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')


config_name = 'local'
app = create_app(config_name)
manager = Manager(app)
# manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()
