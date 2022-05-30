class Drink:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        print('In class price:', self.__price)

    def get_price(self):
        print('----get price-----')
        return self.__price

drink1 = Drink('coffee', 100)
print('1.\t', drink1.get_price())
