import json
import datetime
import re

DATE_KEY = re.compile(r'date')

DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
TIME_FORMAT = '%H:%M:%S'
DATE_VALUE_KEY = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$')
DATETIME_VALUE_KEY = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$')
TIME_VALUE_KEY = re.compile(r'^[0-9]{2}:[0-9]{2}:[0-9]{2}$')

def _json_datetime_parser(dct):
    for k, v in dct.items():
        if re.search(DATE_KEY, k) and re.search(DATETIME_VALUE_KEY, v):
            dct[k] = datetime.datetime.strptime(v, DATETIME_FORMAT)
        elif re.search(DATE_KEY, k) and re.search(DATE_VALUE_KEY, v):
            dct[k] = datetime.datetime.strptime(v, DATE_FORMAT).date()
        elif re.search(DATE_KEY, k) and re.search(TIME_VALUE_KEY, v):
            dct[k] = datetime.datetime.strptime(v, TIME_FORMAT).time()
    return dct

def _json_datetime_serial(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime(DATETIME_FORMAT)
    elif isinstance(obj, datetime.date):
        return obj.strftime(DATE_FORMAT)
    elif isinstance(obj, datetime.time):
        return obj.strftime(TIME_FORMAT)
    return obj

json_str = '{"hoge_date": "2019-01-02", "hoge_date2": "2019-01-02 10:10:10", "hoge_date3": "10:10:10"}'
print(json_str)

dct = json.loads(json_str, object_hook=_json_datetime_parser)
print(dct)

json.dumps(dct, default=_json_datetime_serial)

with open('test.json', 'w') as f:
    json.dump(dct, f, indent=4, default=_json_datetime_serial)
