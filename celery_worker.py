import datetime

from config import ACCESS_LOG_SAVE_PATH, WANGQIAN_ACCESS_LOG, WANGQIAN_ACCESS_LOG_2_DAY
from tasks import app
import os


@app.task
def get_wangqian_access():
    wangqian_access = 'wangqian_access.log'
    command2 = 'scp ssh wq:/data/logs/nginx/{0} {1}'.format(wangqian_access, WANGQIAN_ACCESS_LOG)
    os.system(command2)


@app.task
def nginx_log_2_day_ago():
    # 每天凌晨执行
    today = datetime.datetime.today()
    two_days_ago = today - datetime.timedelta(2)
    filename = 'wangqian_access.log.{}'.format(two_days_ago.strftime('%Y-%m-%d'))
    command = 'scp ssh wq:/data/logs/nginx/{0} {1}'.format(filename, WANGQIAN_ACCESS_LOG_2_DAY)
    os.system(command)


@app.task
def get_access_log():
    command = 'scp ssh wq:/data/webroot/eyaos_signature/server/logs/access.log {save_path}'.format(
        save_path=ACCESS_LOG_SAVE_PATH)
    os.system(command)

