import re
pattern = r"(\.txt)"
dir_list = ["AAA,py", "BBB.exe", "CCC.txt", "DDD.txt"]
pattern_var = re.compile(pattern)
for dir_name in dir_list:
    result = pattern_var.sub(".py", dir_name)
    print("模式:{0:^8},字串{1:^8}".format(dir_name, result))