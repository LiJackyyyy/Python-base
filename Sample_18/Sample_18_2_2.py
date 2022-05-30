import os

path_t_1 = "C:\\Python_Class\\workspace\\Sample_18\\os_test"
print("1.\t", os.listdir(path_t_1))

os.mkdir(path_t_1 + "\\a_dir_name")
print("2.\t", os.listdir(path_t_1))

