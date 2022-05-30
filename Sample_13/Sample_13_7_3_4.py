def discount(number):
    print('-'*10)
    return number * 0.9


num = [1000, 900, 800]
ite = iter(num)

for i in map(discount, ite):
    print(i)
