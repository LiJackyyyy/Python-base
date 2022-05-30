p = {'a': 10, 'b': 90, 'c': 30, 'd': 40}   # dictipnary只針對 key
print('1.\t', any(p))
print('2.\t', all(p))
print()
print()
o = {'a': 10, '': 90, '': 30, '': 40}
print('3.\t', any(o))
print('4.\t', all(o))
print()
print()
u = {'a': 10, '': 90, '': 30, '': 40}
print('5.\t', any(u))
print('6.\t', all(u))

print()
print()
n = [31, 21, 54, 61, 62]
print('1.\t', any(n))
print('2.\t', all(n))
print()
print()
n = [31, 21, 54, 61, None]
print('3.\t', any(n))
print('4.\t', all(n))
print()
print()
n = [0, 0, None, 0, 0]
print('5.\t', any(n))
print('6.\t', all(n))
