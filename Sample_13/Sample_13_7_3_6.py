num = [100, 90, 80, 70, 60, 50]
ans = filter(lambda x: 60 <= x <= 90, num)
print(ans)
print(list(ans))


print('-'*30)

from collections.abc import Iterable
num = [100, 90, 80, 70, 60, 50]
ans = filter(lambda x: 60 <= x <= 90, num)
print(isinstance(ans, Iterable))
