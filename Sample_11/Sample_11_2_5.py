p = {'a': 10, 'b': 90, 'c': 30}  #

print('原本', p)
da = p.pop('b')
print(da)
print('改後', p)

print()
print()
p = {'a': 10, 'b': 90, 'c': 30}  #

print('原本', p)
da = p.popitem()
print(da)
print('改後', p)
