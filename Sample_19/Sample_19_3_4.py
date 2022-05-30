import time
import os

date = time.strftime("%Y%m%d", time.localtime())
dir_name = "dir_AAA" + date
path_b = "C:\\Python_Class\\workspace"

if dir_name not in os.listdir(path_b):
    os.mkdir(path_b + dir_name)
