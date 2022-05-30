n = ('a','b', 'c', 'd')
p = (10, 20, 30, 40)

for i in zip(n, p):
    print(i)

for i in  enumerate(n) :
    print(i)

print('*0' * 30 )
n = ('a','b', 'c', 'd')
p = (10, 20, 30, 40)

for i, j in zip(n, p ):
    print('商品:', n,'價格:', p)

print('*0' * 30 )
n = ('a','b', 'c', 'd')
p = (10, 20, 30, 40)

a1, a2, a3, a4 = zip(n, p)
print('1.\t', a1)
print('2.\t', a2)
print('3.\t', a3)
print('4.\t', a4)
