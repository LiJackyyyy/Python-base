a = {'aa', 'bb', 'cc', 'dd', 'ee'}
b = {'aa', 'bb', 'rr', 'dd', 'ee'}
c = ('aa', 'bb', 'rr', 'dd', 'ee')
d = ['aa', 'bb', 'rr', 'dd', 'ee']
e = {'aa' : 12345, 'bb': 123,'cc': 123,'dd': 123, 'ee': 123}
print(a.union(b))
print(a.intersection(c))
print(a.difference(c))
print(a. symmetric_difference(c))