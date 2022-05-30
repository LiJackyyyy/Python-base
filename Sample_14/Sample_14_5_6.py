class Drink:
    def __init__(self, name, price, discount):
        self.name = name
        self.__price = price
        self.discount = discount
        print('In class price:', self.__price)

    def __calculate_discount(self):
        return self.__price * self.discount

    def get_name(self):
        return self.name

    def get_price(self):
        return self.__price, self.__calculate_discount()


drink1 = Drink('coffee', 100, 0.9)
n1 = drink1.get_name()
p1, pd1 = drink1.get_price()
print(n1, '價格', p1, '元', '打折後:', pd1)
# t_1 = drink1.__calculate_discount()
