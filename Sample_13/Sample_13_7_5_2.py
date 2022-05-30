def decorate(func):
    print(func)
    def wrapper(data):
        print(data)
        data_m = '---------' + data + '-----------'
        return func(data_m)
    return wrapper


@decorate
def message_name(par):
    print(par)


message_name('coffee')
