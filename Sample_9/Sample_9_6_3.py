n = ['apple', 'b', 'c', 'd']
p = [10, 20, 30, 40]
print('1.\t', zip(n,p))
print('*' * 30)
p1, p2, p3, p4 = zip(n,p)  # 解包也可以同時指定給變數
print(p1)
print(p2)
print(p3)
print(p4)
