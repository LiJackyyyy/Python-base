import os

path_t_1 = "C:\\Python_Class\\workspace\\Sample_18\\os_test"
print("1.\t", os.listdir(path_t_1))

os.rmdir(path_t_1 + "\\b_dir_name")
print("2.\t", os.listdir(path_t_1))

