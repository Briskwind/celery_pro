import datetime


def format_time(unit):
    if unit < 10:
        res = '0{}'.format(unit)
    else:
        return str(unit)
    return res


def get_file_name(db_name):

    date = datetime.datetime.now()
    month = format_time(date.month)
    day = format_time(date.day)
    hour = format_time(date.hour)
    filename = '{db_name}_{month}{day}{hour}.sql.gz'.format(db_name=db_name, month=month, day=day, hour=hour)
    filename = 'wangqian_xs_011206.sql.gz'
    return filename