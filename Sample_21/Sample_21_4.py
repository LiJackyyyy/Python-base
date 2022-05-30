import threading
import os
import time

def get_drink(name, price):
    global global_name
    global_name = name
    print("get_drink PID", os.getpid())
    time.sleep(3)
    print("品名:{0},價格{1}".format(name, price))

def get_num():
    print("get_drink PID", os.getpid(), end="\t")
    print("In get num:", global_name)
    time.sleep(2)

if __name__ =="__main__":
    start = time.time()
    data = {"coffee": 100, "tea": 90, "juice": 80, "milk": 70, "water": 60}
    global global_name
    global process_1
    for i in data:
        process_1 = threading.Thread(target=get_drink, args=(i, data[i]))
        process_2 = threading.Thread(target=get_num)
        process_1.start()
        process_2.start()
    else:
        process_1.join()
    end = time.time()
    print("Total time:", end - start)
