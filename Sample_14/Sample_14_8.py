class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        dr = self.name + '好喝\t'
        return dr

    def __int__(self):
        return self.price

    def __add__(self, other):
        price = self.price + other.price
        return price


drink1 = Drink('coffee', 100)
print(str(drink1))
print(int(drink1))
drink2 = Drink('tea', 90)
print(str(drink2))
print(int(drink2))
print('總額:', drink1 + drink2)
