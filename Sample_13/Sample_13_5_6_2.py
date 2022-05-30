def s():
    p = 50
    n = 'string'
    def s2():
        nonlocal n
        n = 'coffee'
        print('3.\t', n)
    s2()
    print('4\t', n)
    print('2.\t', p)


p = 100
print('1.\t', p)
s()
