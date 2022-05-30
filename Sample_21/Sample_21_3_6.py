import multiprocessing as mp
import time

def get_count():
    for i in range(100):
        print(i)
        time.sleep(1)
if __name__ =="__main__":
        process_1 = mp.Process(target=get_count)
        time.sleep(8)
        process_1.terminate()
