import datetime
from datetime import timedelta

def unixTimeConverter(delta):
    now = datetime.datetime.now()
    time_diff = now - timedelta(days=int(delta))

    str_unix_time = [str(int(now.timestamp())), str(int(time_diff.timestamp()))]
    return str_unix_time[0], str_unix_time[1]
