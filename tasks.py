from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

from config import BROKER_URI, BACKEND_URI

app = Celery('celery_worker', broker=BROKER_URI, backend=BACKEND_URI)

app.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True,
    beat_schedule={

        "get_wq_celery_log": {
            "task": "celery_worker.get_wq_celery_log",
            "schedule": timedelta(seconds=70),
        },

        "get_wq_druglistrpc": {
            "task": "celery_worker.get_druglistrpc_out",
            "schedule": timedelta(seconds=56),
        },

        "get_wq_access_log": {
            "task": "celery_worker.get_access_log",
            "schedule": timedelta(seconds=60),
        },

        "nginx_access": {
            "task": "celery_worker.get_wangqian_access",
            "schedule": timedelta(minutes=3),

        },

        "nginx_two_days_ago": {
            "task": "celery_worker.nginx_log_2_day_ago",
            "schedule": crontab(hour=1, minute=0),

        },

    }
)
