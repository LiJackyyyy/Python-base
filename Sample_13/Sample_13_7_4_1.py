def fun(n):
    if n ==1:
        return 1
    else:
        return n * fun(n-1)


ans = fun(3)
print(ans)

print('-' * 30)

def fun(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * fun(n-1)


ans = fun(-10)
print(ans)
