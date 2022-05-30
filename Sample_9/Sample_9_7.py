p = [100, 90, 80, 70]
print('price', p)
newp = [i * 0.9 for i in p if 80 <= i <= 90]
print('newp', newp)

print('-' * 30)
n1 = ['apple', 'b', 'c', 'd']
p1 = [10, 20, 30, 40]
print('產品', n1)
print('價格:', p1)
newp1 = [i * 0.5 for i in p1]
print('-----全面商品打五折-----')
print('打折後:', newp1)

