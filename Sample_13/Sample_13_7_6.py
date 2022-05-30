def function(x):
    while True:
        yield x
        x = x + 1


n = function(0)
print(n)

