import multiprocessing as mp
import os
import time

def get_drink(name,price):
    print("PID", os.getpid())
    time.sleep(3)
    print("產品:{0},價格:{1}".format(name, price))

if __name__ =="__main__":
    start = time.time()
    print("1.\t In main PID:", os.getpid())
    data = {"coffee": 100, "tae": 90, "juice": 80}
    for i in data:
        process_1 = mp.Process(target=get_drink, args=(i, data[i]))
        process_1.start()
    end = time.time()
    print("2.\tIn the PID:", os.getpid())
    print("Total time:", end - start)
