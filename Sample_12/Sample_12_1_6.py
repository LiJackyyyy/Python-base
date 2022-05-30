a = {'aa', 'bb', 'cc', 'dd', 'ee',  'cc', 'dd'}
b = {'aa', 'cc', 'bb', 'dd',  'cc', 'ee', 'dd'}
c = {'bb', 'cc', 'bb', 'dd',  'aa', 'cc', 'dd'}
sa = a == b
sb = a != b
sc = a == c
sd = a != c

print(sa)
print(sb)
print(sc)
print(sd)
