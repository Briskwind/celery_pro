from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

from config import BROKER_URI, BACKEND_URI

app = Celery('celery_worker', broker=BROKER_URI, backend=BACKEND_URI)

app.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True,
    beat_schedule={

        "get_access_log": {

            "task": "celery_worker.get_access_log",
            "schedule": timedelta(seconds=100),
        },

        "wangqian_access": {
            "task": "celery_worker.get_wangqian_access",
            "schedule": timedelta(seconds=60),

        },
        "two_days_ago": {
            "task": "celery_worker.nginx_log_2_day_ago",
            "schedule": crontab(hour=1, minute=0),

        },
    }
)
