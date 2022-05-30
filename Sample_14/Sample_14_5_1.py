class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


drink1 = Drink('coffee', 100)
print('1.\t', drink1.price)
print('2.\t', drink1.get_price())
drink1.price = 10
print('3.\t', drink1.price)
print('4.\t', drink1.get_price())
