from functools import reduce

num = [100, 90, 80]
ans = reduce(lambda x, y: x+y, num)
print(ans)

print('-'*30)
from functools import reduce

num = [100, 90, 80]
ans = reduce(lambda x, y: x*y, num)  # xy等同於代號
print(ans)
