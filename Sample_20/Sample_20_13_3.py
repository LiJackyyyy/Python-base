import re
pattern = "-"
dir_list = ["0912-345-678", "0934-567-789"]

pattern_var = re.compile(pattern)
for num in dir_list:
    result = pattern_var.split(num)
    print(result)

print('-'*30)
