n = ['apple', 'b', 'c', 'd']
p = [10, 20, 30, 40]
print('產品', n)
print('價格:', p)
newp = [int(i * 0.9) if 80 < i else
        int(i * 0.5) if 20 < i <= 80 else
        int(i * 0.1) for i in p]
print('---全面商品打一折-----')
print('打折後:', newp)
