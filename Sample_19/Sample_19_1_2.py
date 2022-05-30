import datetime as dt

print("1.\t", dt.timedelta(days=7))

date_time = dt.datetime.now()
print("2.\t", date_time)

date_time_a = date_time + dt.timedelta(days=7)
print("3.\t", date_time_a)

date_time_b = date_time + dt.timedelta(days=30)
print("4.\t", date_time_b)

date_time_c = date_time + dt.timedelta(days=-6)
print("5.\t", date_time_c)


