from fabric.api import local, env, run, lcd, cd
import datetime
from datetime import timedelta, datetime
import time

from commom import get_file_name
from config import NEW_TEST_PASS

env.hosts = ['wqtest@47.98.176.227:53190']
env.key_filename = '~/.ssh/id_rsa'


def sync_database():

    sql_path = ' /data/yunwei/database_back/'
    db_name = 'wangqian_xs'
    filename = get_file_name(db_name)

    zip_file = ' /data/yunwei/database_back/{0}'.format(filename)
    gunzip_cmd = 'cd {0} && gunzip {1}'.format(sql_path, zip_file)

    run(gunzip_cmd)

    sql_file = zip_file[:-3]

    sync = 'mysql -h 172.16.91.197 -uroot -P3308 -p{0} -f wqxs_fortest <  {1}'.format(NEW_TEST_PASS, sql_file)
    run(sync)
