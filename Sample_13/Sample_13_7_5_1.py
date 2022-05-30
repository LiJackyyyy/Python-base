def decorate(func):
    print(func)
    def wrapper():
        pass
    return wrapper


#@decorate
def message_name():
    pass


massage_name = decorate(message_name)