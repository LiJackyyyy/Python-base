from multiprocessing import Pool
import os
import time

def get_drink(name,price):
    print("PID", os.getpid())
    time.sleep(3)
    print("產品:{0},價格:{1}".format(name, price))

if __name__ =="__main__":
    start = time.time()
    data = {"coffee": 100, "tae": 90, "juice": 80, "milk": 70, "latte": 60, "water": 50}
    with Pool(processes=3) as pool:
        for i in data:
            process_1 = pool.apply_async(get_drink, (i, data[i]))
        process_1.get()
    end = time.time()
    print("Total time:", end - start)