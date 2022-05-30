import os
import time

def get_drink(name,price):
    print("PID", os.getpid())
    time.sleep(3)
    print("產品:{0},價格:{1}".format(name, price))

if __name__ =="__main__":
    start = time.time()
    data = {"coffee": 100, "tae": 90, "juice": 80}
    for i in data:
        get_drink(i, data[i])
        end = time.time()
    print("Total:", end - start)