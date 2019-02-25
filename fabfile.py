from fabric.api import local, env, run, lcd, cd
import datetime
from datetime import timedelta, datetime
import time

env.hosts = ['wqtest@47.98.176.227:53190']
env.key_filename = '~/.ssh/id_rsa'


def sync_database():
    print('# 执行数据同步命令')
    run('ls')
