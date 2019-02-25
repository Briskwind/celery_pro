from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

from config import BROKER_URI, BACKEND_URI

app = Celery('celery_worker', broker=BROKER_URI, backend=BACKEND_URI)

app.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True,
    beat_schedule={

        "send_wq_database_test": {
            "task": "celery_worker.send_wq_database_test",
            "schedule": crontab(hour=15, minute=41),

        },

        # 新势力应用日志
        # "get_xsl_api_access_log": {
        #     "task": "celery_worker.get_xsl_api_access_log",
        #     "schedule": timedelta(seconds=66),
        # },

        # "get_xsl_access_log": {
        #     "task": "celery_worker.get_xsl_access_log",
        #     "schedule": timedelta(seconds=75),
        # },

        # "get_xsl_eyaos_stderr": {
        #     "task": "celery_worker.get_xsl_eyaos_stderr",
        #     "schedule": timedelta(seconds=71),
        # },

        # 新势力日志相关
        # "get_xsl_nginx": {
        #     "task": "celery_worker.get_xsl_nginx",
        #     "schedule": timedelta(minutes=60),
        # },
        # "get_xsl_nginx_yesterday": {
        #     "task": "celery_worker.get_xsl_nginx_yesterday",
        #     "schedule": crontab(hour=1, minute=1),
        # },
        #
        # # 网签日志相关
        # "get_wq_celery_log": {
        #     "task": "celery_worker.get_wq_celery_log",
        #     "schedule": timedelta(minutes=30),
        # },
        #
        # "get_wq_druglistrpc": {
        #     "task": "celery_worker.get_druglistrpc_out",
        #     "schedule": timedelta(minutes=20),
        # },
        #
        # "get_wq_access_log": {
        #     "task": "celery_worker.get_access_log",
        #     "schedule": timedelta(minutes=10),
        # },
        #
        # "nginx_access": {
        #     "task": "celery_worker.get_wangqian_access",
        #     "schedule": timedelta(minutes=25),
        #
        # },
        #
        # "nginx_two_days_ago": {
        #     "task": "celery_worker.nginx_log_2_day_ago",
        #     "schedule": crontab(hour=1, minute=0),
        #
        # },

        # 数据库备份拉取
        # wq
        "get_wq_database": {
            "task": "celery_worker.get_wq_database",
            "schedule": crontab(hour=6, minute=20),

        },
        # 药监单
        "get_invoices_database": {
            "task": "celery_worker.get_invoices_database",
            "schedule": crontab(hour=6, minute=40),

        },
        # 基础数据库
        "get_djangodrug_db": {
            "task": "celery_worker.get_djangodrug_db",
            "schedule": crontab(hour=6, minute=30, day_of_week=0),

        },

    }
)
