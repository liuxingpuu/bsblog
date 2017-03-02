# -*- coding:utf-8 -*-
import os
import logging

from flask.ext.script import Manager, Server
from blog import app

# 配置日志
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')


config_name = os.getenv('local_config')
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()
