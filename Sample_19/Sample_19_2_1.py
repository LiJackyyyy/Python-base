import datetime as dt

date_time = dt.datetime.now()
print("現在時間:", date_time)
a = dt.datetime.strftime(date_time,"%Y-%m-%d")
print(a)
b = dt.datetime.strftime(date_time,"%y-%m-%d")
print(b)
c = dt.datetime.strftime(date_time,"%H-%M-%S")
print(c)
d = dt.datetime.strftime(date_time,"%Y-%m-%d%H%M%S")
print(d)

