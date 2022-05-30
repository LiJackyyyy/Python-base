import re

pattern_list = [r"\d{8}(news)", r"\d{8}(?!news)"]
search_list = ["abcd20211010newsabcda", "abcd20211010asd"]

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