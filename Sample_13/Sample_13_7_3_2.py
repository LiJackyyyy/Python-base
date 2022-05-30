a = [100, 90, 80, 70]
ans = map(lambda x: x*2, a)
print(a)
print(type(ans))
data = list(ans)
print(data)


print('-' * 30)
a = [100, 90, 80, 70]
for i in map(lambda x: x*2, a):
    print(i)
