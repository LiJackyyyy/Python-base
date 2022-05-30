import re

pattern_list = [r"^[^@&=\+\.]([0-9A-Za-z\.]*[^@&=\+])@[a-z]+(.com)"]
search_list = ["abcd1243@gmail.com", "abcd.1243@gmail.com", "abcd@1243@gmail.com"
               , "a=bcd1243@gmail.com", ".abcd1243@gmail.com", "abcd+1243@gmail.com"]

for pattern_value in pattern_list:
    pattern_var = re.compile(pattern_value)
    for search_value in search_list:
        result = pattern_var.search(search_value)
        print("模式:{0:^8},字串{1:^8}".format(pattern_value, search_value), end="")
        if result is not None:
            print("匹配結果------OK------\t", result)
            result_value = result.group()
            print("取得匹配資料:", result_value)
        else:
            print("匹配結果------NO------")

    print("-" * 30 )