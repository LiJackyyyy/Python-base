import datetime as dt

date_time = dt.datetime.now()
print("現在時間:", date_time)
print("1.\t", date_time.strftime('%c'))
print("2.\t", date_time.strftime('%x'))
print("3.\t", date_time.strftime('%X'))
print("4.\t", date_time.strftime('%Y'))
print("5.\t", date_time.strftime('%y'))
print("6.\t", date_time.strftime('%B'))
print("7.\t", date_time.strftime('%b'))
print("8.\t", date_time.strftime('%m'))
print("9.\t", date_time.strftime('%d'))
print("10.\t", date_time.strftime('%H'))
print("11.\t", date_time.strftime('%I'))
print("12.\t", date_time.strftime('%M'))
print("13.\t", date_time.strftime('%S'))
print("14.\t", date_time.strftime('%p'))
print("15.\t", date_time.strftime('%w'))
print("16.\t", date_time.strftime('%A'))
print("17.\t", date_time.strftime('%a'))
print("18.\t", date_time.strftime('%j'))
print("19.\t", date_time.strftime('%U'))
print("20.\t", date_time.strftime('%W'))

date_time_tz = dt.datetime.now().astimezone()
print(date_time_tz)
print(date_time_tz.strftime("%Z"))



