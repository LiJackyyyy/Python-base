def f3():
    return 1
def f2():
    print('f3 start')
    b = f3()
    print('f3 end')
    return b
def f1():
    print('f2 start')
    c = f2()
    print('f2 end')
    return c

print('f1 start')
ans = f1()
print('f1 end')
print(ans)
