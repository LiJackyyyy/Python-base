import os
import time

def get_drink():
    print("PID", os.getpid())
    time.sleep(100)


get_drink()