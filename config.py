

# celery redis config
HOST_IP = '127.0.0.1'
BROKER_URI = 'redis://%s:6379/11' % HOST_IP
BACKEND_URI = 'redis://%s:6379/11' % HOST_IP


# wq access log
ACCESS_LOG_SAVE_PATH = ''

# nginx log
WANGQIAN_ACCESS_LOG = ''

# 2 days ago nginx log
WANGQIAN_ACCESS_LOG_2_DAY = ''




try:
    from local_config import *
except Exception:
    pass
