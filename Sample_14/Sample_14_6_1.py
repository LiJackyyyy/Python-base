class Drink:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        print('In class price:', self.__price)

    def get_name(self):
        return self.name

    @property
    def price_manage(self):
        return self.__price

    @price_manage.setter
    def price_manage(self, price):
        self.__price = price


class OriginalDrink(Drink):
    def __init__(self, name, price, country, variety):
        super().__init__(name, price)
        self.country = country
        self.variety = variety

    def get_country(self):
        return '產地:' + self.country

    def get_variety(self):
        return '品種:' + self.variety


drink1 = OriginalDrink('coffee', 100, 'Blue Mountain', 'Arabica')
d_n = drink1.get_name()
d_p = drink1.price_manage
d_c = drink1.get_country()
d_v = drink1.get_variety()

print(d_n, '價格', d_p, '元', '產地:', d_c, '品種:', d_v)

