import re

pattern_list = [r"^([0][9]\d{8})", r"^[A-Zaz][12]\d{8}"]
search_list = ["0912343545", "A123456789", "A345678987"]

for pattern_value in pattern_list:
    pattern_var = re.compile(pattern_value)
    for search_value in search_list:
        result = pattern_var.search(search_value)
        print("模式:{0:^8},字串{1:^8}".format(pattern_value, search_value), end="")
        if result is not None:
            print("匹配結果------OK------\t", result)
        else:
            print("匹配結果------NO------")

    print("-" * 30 )