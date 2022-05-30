import datetime as dt
date_time = dt.datetime.now()
print("1.\t現在日期與時間", date_time)
print("2.\t現在時間戳", date_time.timestamp())
print("3.\t現在日期", date_time.date())
print("4.\t現在星期幾", date_time.weekday()+1)
print("5.\t現在時間", date_time.time())
print('-' * 30)
print("6.\t", date_time.year)
print("7.\t", date_time.month)
print("8.\t", date_time.day)
print("9.\t", date_time.hour)
print("10.\t", date_time.minute)
print("11.\t", date_time.second)
print("12.\t", date_time.microsecond)
print("13.\t", date_time.tzinfo)
print("14.\t本地時間含時區", date_time.astimezone())
print("15.\t本地時間含時區", date_time.astimezone().tzinfo)
date_time_utc = dt.datetime.now(dt.timezone.utc)
print("16.\t本地時間含時區", date_time_utc)
print("17.\t本地時間含時區", date_time_utc.tzinfo)
