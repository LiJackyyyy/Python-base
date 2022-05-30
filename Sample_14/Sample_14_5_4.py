class Drink:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        print('In class price:', self.__price)

    @property
    def price_manage(self):
        print('----get price-----')
        return self.__price

    @price_manage.setter
    def price_manage(self, price):
        print('----set price-----')
        self.__price = price


drink1 = Drink('coffee', 100)
print('1.\t', drink1.price_manage)
drink1.price_manage = 400
print('2.\t', drink1.price_manage)
