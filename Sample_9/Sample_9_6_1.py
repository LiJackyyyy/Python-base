n = ['a', 'b', 'c', 'd']
p = ['10', '20', '30', '40']
# 需要將多個串列合併(打包)，可以使用內建函數 zip()。
for i in zip(n, p):
    print(i)

# 資料打包的長度，往後算多的部分不會被打包
print('-' * 30)
n = ['a', 'b', 'c', 'd']
p = ['10', '20', '30']

for i in zip(n, p):
    print(i)
    print(type(i))