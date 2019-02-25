import datetime

from commom import get_file_name
from config import APP_LOG_SAVE_PATH, NGINX_LOG_PATH, DATABASE_BACKUP_PATH, XSL_NGINX_PATH, XSL_APP_LOG
from fabfile import sync_database
from tasks import app
import os




@app.task(max_retries=1)
def send_wq_database_test():
    """ 发送网签数据到测试服务器"""

    db_name = 'wangqian_xs'
    filename = get_file_name(db_name)
    command = 'scp /data/yumwei/daily_backup/{0} ssh new_wqtest:/data/yunwei/database_back'.format(filename)
    os.system(command)
    # 执行数据同步命令
    sync_database = '~/.pyenv/versions/yunwei/bin/fab -f /data/yumwei/celery_pro/fabfile.py sync_database'
    os.system(sync_database)




@app.task(max_retries=1)
def get_wq_database():
    """ 每天6:20拉取网签备份数据库"""

    db_name = 'wangqian_xs'
    filename = get_file_name(db_name)
    command = 'scp ssh wq:/data/daily_backup/{0} {1}'.format(filename, DATABASE_BACKUP_PATH)
    os.system(command)


@app.task(max_retries=1)
def get_invoices_database():
    """ 每天6:40拉取药监单备份数据库"""
    db_name = 'invoices'
    filename = get_file_name(db_name)
    command = 'scp ssh wq:/data/daily_backup/{0} {1}'.format(filename, DATABASE_BACKUP_PATH)
    os.system(command)


@app.task(max_retries=1)
def get_djangodrug_db():
    """ 周日 6:30 拉取基础数据库备份数据库"""

    db_name = 'djangodrug'
    filename = get_file_name(db_name)
    command = 'scp ssh wq:/data/daily_backup/{0} {1}'.format(filename, DATABASE_BACKUP_PATH)
    os.system(command)


@app.task()
def get_new_medicine_database():
    """ 拉取医药新势力数据库"""
    pass


# nginx 日志的收集


@app.task(max_retries=2)
def get_xsl_nginx():
    """ 新势力nginx 日志收集"""
    wangqian_access = 'kuaijie_access.log'
    command = 'scp ssh sy:/data/logs/nginx/{0} {1}'.format(wangqian_access, XSL_NGINX_PATH)
    os.system(command)


@app.task(max_retries=2)
def get_xsl_nginx_yesterday():
    """ 新势力nginx 昨日日志收集"""
    today = datetime.datetime.today()
    two_days_ago = today - datetime.timedelta(1)
    filename = 'kuaijie_access.log.{}'.format(two_days_ago.strftime('%Y-%m-%d'))
    command = 'scp ssh sy:/data/logs/nginx/{0} {1}'.format(filename, XSL_NGINX_PATH)
    os.system(command)



@app.task(max_retries=2)
def get_wangqian_access():
    """ 网签nginx 日志收集"""
    wangqian_access = 'wangqian_access.log'
    command2 = 'scp ssh wq:/data/logs/nginx/{0} {1}'.format(wangqian_access, NGINX_LOG_PATH)
    os.system(command2)


@app.task(max_retries=2)
def nginx_log_2_day_ago():
    # 每天凌晨执行
    today = datetime.datetime.today()
    two_days_ago = today - datetime.timedelta(2)
    filename = 'wangqian_access.log.{}'.format(two_days_ago.strftime('%Y-%m-%d'))
    command = 'scp ssh wq:/data/logs/nginx/{0} {1}'.format(filename, NGINX_LOG_PATH)
    os.system(command)


# 以下是应用日志的收集

@app.task(max_retries=2)
def get_access_log():
    """ 网签web日志"""
    command = 'scp ssh wq:/data/webroot/eyaos_signature/server/logs/access.log {save_path}'.format(
        save_path=APP_LOG_SAVE_PATH)
    os.system(command)


@app.task(max_retries=2)
def get_druglistrpc_out():
    """ 获取网签 druglistrpc 输出日志"""
    command = 'scp ssh wq:/home/wangqian/.pm2/logs/druglistrpc-out-2.log {save_path}'.format(
        save_path=APP_LOG_SAVE_PATH)
    os.system(command)


@app.task(max_retries=2)
def get_wq_celery_log():
    """ 获取网签 异步任务 输出日志"""
    command = 'scp ssh wq:/data/logs/wangqian/wangqiancelery.err.log {save_path}'.format(
        save_path=APP_LOG_SAVE_PATH)
    os.system(command)

@app.task(max_retries=2)
def get_xsl_eyaos_stderr():
    """ 新势力应用日志"""
    command = 'scp ssh sy:/data/logs/supervisor/eyaos-stderr.log {save_path}'.format(
        save_path=XSL_APP_LOG)
    os.system(command)


@app.task(max_retries=2)
def get_xsl_access_log():
    """ 新势力 access.log日志"""
    command = 'scp ssh sy:/data/xsl/eyaos_web/web/logs/access.log {save_path}'.format(
        save_path=XSL_APP_LOG)
    os.system(command)


@app.task(max_retries=2)
def get_xsl_api_access_log():
    """ 新势力 api_access.log日志"""
    command = 'scp ssh sy:/data/xsl/eyaos_web/web/logs/api_access.log {save_path}'.format(
        save_path=XSL_APP_LOG)
    os.system(command)


