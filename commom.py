import datetime


def format_time(unit):
    if unit < 10:
        res = '0{}'.format(unit)
    else:
        return str(unit)
    return res


def get_file_name(db_name):
    """ 获取数据库备份名称"""

    date = datetime.datetime.now()
    month = format_time(date.month)
    day = format_time(date.day)
    hour = format_time(date.hour)
    filename = '{db_name}_{month}{day}{hour}.sql.gz'.format(db_name=db_name, month=month, day=day, hour=hour)
    return filename