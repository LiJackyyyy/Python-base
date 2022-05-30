n = ['apple', 'b', 'c', 'd']
p = [10, 20, 30, 40]
print('產品', n)
print('價格:', p)
newp = [int(i * 0.9) if i >= 20 else int(i * 0.5) for i in p]
print('---全面商品打五折-----')
print('打折後:', newp)
