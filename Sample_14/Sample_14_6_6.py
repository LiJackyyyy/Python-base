class ProductOrigin:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return '產品名稱:' + self.name

    def get_price(self):
        return {'價格:': self.price}


class ProductDiscount(ProductOrigin):
    def __init__(self, name, price, discount):
        ProductOrigin.__init__(self, name, price)
        self.discount = discount

    def get_price(self):
        return {'特價:': self.price * self.discount}


product = ProductOrigin('coffee', 100)
pn_1 = product.get_name()
pp_1 = product.get_price()
print(pn_1, pp_1)
print('-' * 20)
product2 = ProductDiscount('coffee', 100, 0.8)
pn_2 = product2.get_name()
pp_2 = product2.get_price()
print(pn_2, pp_2)
