n = ['apple', 'b', 'c', 'd']
p = [10, 20, 30, 40]
# 將串列的元素打包，那麼解包的方式如
for n,p in zip(n, p):
    print('名稱:', n, '\t價格:', p)
