n = [99, 98, 87, 78, 56, 4, 9, 16]
n1 = n[3:7]  # [a:b] 第b不算
print('1.\t', n1)
n2 = n[:7]
print('2\t', n2)
n3 = n[3]
print('3.\t', n3)
n4 = n[3:7:2]
print('4.\t', n4)
n5 = n[::-1]
print('5.\t', n5)
print('*' * 10)
n = [99, 98, 87, 78, 56, 4, 9, 16]
print('原本:', n)
n[3:7] = [100, 99.8, 87.87, 59.5]
print('改後:', n)

print('*' * 10)
n = [99, 98, 87, 78, 56, 4, 9, 16]
print('原本:', n)
del n[3:7]
print('改後:', n)
