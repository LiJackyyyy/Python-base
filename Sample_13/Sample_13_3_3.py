def a(b, c):
    if b > c:
        b -= c
        print('提領', c)
        print('餘額', b)
    else:
        print('沒錢')


s = 2000
d = 10000
a(d, s)
