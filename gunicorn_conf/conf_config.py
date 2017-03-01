

bind = 'unix:/data/blog/blog.sock'
import os
host = os.getenv('HOSTNAME')
# bind = str(host)+':8088'
workers=1
worker_class = 'gevent'
proc_name = 'tblog'
pidfile = '/tmp/tmjweb.pid'
errorlog = '/data/mjweb/mjweb.log'