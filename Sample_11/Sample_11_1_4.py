p = {'a': 10, 'b': 90, 'c': 30, 'd': 40}
k = p.keys()
v = p.values()
il = p.items()
print('1.\t', k)
print('2.\t', v)
print('3.\t', il)
print()
print('- ' * 30)
for i in k:
    print(i, end='\t')
print('\n', '-' * 30)
for i in v:
    print(i, end='\t')
print('\n', '-' * 30)
for i in il:
    print(i, end='\t')
