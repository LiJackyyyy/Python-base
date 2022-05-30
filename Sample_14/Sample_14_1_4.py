class Drink:
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


drink1 = Drink()
drink1.name = 'coffee'
drink1.price = 100
n1 = drink1.get_name()
p1 = drink1.get_price()
print(n1, '價格', p1, '元')

drink1 = Drink()
drink1.name = 'tea'
drink1.price = 80
n1 = drink1.get_name()
p1 = drink1.get_price()
print(n1, '價格', p1, '元')
