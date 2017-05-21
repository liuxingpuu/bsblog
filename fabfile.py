# -*- coding: utf-8 -*-
"""fabric 部署脚本"""
from fabric.api import hosts, env, run, put
from fabric.colors import green,red
from fabric.contrib.project import rsync_project

env.user = 'root'

PROJECT_NAME = 'bsblog'
PROGRAM_NAME = 'blog'
LOG_FILE_PATH = '/data/' + PROJECT_NAME
REMOTE_DIRECTORY = '/home/' + PROJECT_NAME
LOCAL_CONFIG_PATH = './docs'

@hosts("123.206.215.185")
def testsetup():
    rsync_project(REMOTE_DIRECTORY, '../'+PROJECT_NAME+'/', delete=True)

    run('sudo mkdir -p %s' % LOG_FILE_PATH)

    # 创建nginx脚本
    put(LOCAL_CONFIG_PATH+'/'+'t'+PROJECT_NAME+'.conf', '/etc/nginx/conf.d/',use_sudo=True)
    run("sudo nginx -t")
    run("sudo nginx -s reload")

    put(LOCAL_CONFIG_PATH+'/'+'t'+PROJECT_NAME+'.ini', '/etc/supervisord.d/',use_sudo=True)
    run("sudo supervisorctl reread")
    run("sudo supervisorctl update")

    status()

# @hosts("123.206.215.185")
# def testdeploy():
#     rsync_project(REMOTE_DIRECTORY, '../'+PROJECT_NAME+'/', delete=True)
#     run("sudo supervisorctl restart %s" % PROJECT_NAME)
#     status()

@hosts("108.61.246.118")
def deploy():
    rsync_project(REMOTE_DIRECTORY, '../'+PROJECT_NAME+'/', delete=True)
    run("sudo supervisorctl restart %s" % PROGRAM_NAME)
    status()

def status():
    status = run("sudo supervisorctl status %(project_name)s" % dict(project_name=PROGRAM_NAME))
    if status.index("RUNNING") != -1:
        print(green(status))
    else:
        print(red(status))
