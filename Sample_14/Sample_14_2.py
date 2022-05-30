class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


drink1 = Drink('coffee', 100)
n1 = drink1.get_name()
p1 = drink1.get_price()
print(n1, '價格', p1, '元')
