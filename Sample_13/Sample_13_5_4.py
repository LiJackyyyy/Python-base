def s():  # 錯誤範例 不同區的定義函數內區域變數，就算是相同的變數名稱，也是不同的變數
    b = '不知道'
    print(b)


def x():
    print(b)

