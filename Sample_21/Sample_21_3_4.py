from multiprocessing import Pool
import os
import time

def calculate(i):
    print("PID", os.getpid())
    time.sleep(3)
    return i ** 3
if __name__ =="__main__":
    start = time.time()
    data = [1, 2, 3, 4, 5, 6]
    with Pool(processes = 3) as process_1:
        result = process_1.map(calculate, data)
    print("reslut:", result)
    end = time.time()
    print("Total time:", end - start)