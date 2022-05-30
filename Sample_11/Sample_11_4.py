p = {'a': 100, 'b': 90, 'c': 80, 'd': 70, 'e': 10}
print('原價', p)
np = {i: int(p[i] * 0.9) if 80 < p[i] else
      int(p[i] * 0.5) if 20 < p[i] <= 80 else
      int(p[i] * 0.1)
      for i in p}
print('打折', np)

