import datetime

from config import APP_LOG_SAVE_PATH, NGINX_LOG_PATH
from tasks import app
import os


# nginx 日志的收集
@app.task(max_retries=2)
def get_wangqian_access():
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
