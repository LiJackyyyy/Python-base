import os

path_t_1 = "C:\\Python_Class\\workspace\\Sample_18\\os_test"
print("1.\t", os.listdir(path_t_1))

os.rename(path_t_1 + "\\c.txt", path_t_1 + "\\d.txt")
print("2.\t", os.listdir(path_t_1))

