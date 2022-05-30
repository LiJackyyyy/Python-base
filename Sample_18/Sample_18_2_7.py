import os

path_t_1 = "C:\\Python_Class\\workspace\\Sample_18\\os_test"
os.chmod(path_t_1 + "\\a.txt", 0o700)
print("1.\t", os.access(path_t_1 + "\\a.txt", os.F_OK))
print("2.\t", os.access(path_t_1 + "\\a.txt", os.W_OK))
print("3.\t", os.access(path_t_1 + "\\a.txt", os.R_OK))
print("4.\t", os.access(path_t_1 + "\\a.txt", os.X_OK))

os.chmod(path_t_1 + "\\a.txt", stat.S_IREAD)
print("5.\t", os.access(path_t_1 + "\\d.txt", os.F_OK))