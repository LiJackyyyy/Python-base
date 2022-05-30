import datetime as dt

date_time = dt.datetime.now()
print("1.\t現在時間戳", date_time)

date_now_stamp = date_time.timestamp()
print("2.\t現在日期與時間轉為時間戳", date_now_stamp)

date_co = dt.datetime.fromtimestamp(date_now_stamp)
print("3.\t時間戳轉為現在時間與日期", date_co)
