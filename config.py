

# celery redis config
HOST_IP = '127.0.0.1'
BROKER_URI = 'redis://%s:6379/11' % HOST_IP
BACKEND_URI = 'redis://%s:6379/11' % HOST_IP


# app log
APP_LOG_SAVE_PATH = ''

# nginx log
NGINX_LOG_PATH = ''



try:
    from local_settings import *
except Exception:
    pass
