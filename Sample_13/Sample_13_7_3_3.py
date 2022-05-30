def dis(number):
    print('-'*10)
    return number *0.9


num = [100, 90, 80, 70]
for i in map(dis, num):
    print(i)

print(map(dis, num))
print(type(map(dis, num)))

