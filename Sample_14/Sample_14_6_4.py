class Drink:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_name(self):
        return self.name

    @property
    def price_manage(self):
        return self.__price

    @price_manage.setter
    def price_manage(self, price):
        self.__price = price


class Flavor:
    def __init__(self, smell):
        self.smell = smell

    def get_smell(self):
        return '味道:' + self.smell


class OriginalDrink(Drink, Flavor):
    def __init__(self, name, price, country, variety, smell):
        super().__init__(name, price)
        Flavor.__init__(self, smell)
        self.country = country
        self.variety = variety

    def get_country(self):
        return '產地:' + self.country

    def get_variety(self):
        return '品種:' + self.variety


class Company(OriginalDrink):
    def __init__(self, company_name, name, price, country, variety, smell):
        super().__init__(name, price, country, variety, smell)
        self.company_name = company_name

    def get_company(self):
        return '銷售公司' + self.company_name


drink1 = Company('一號店', 'coffee', 100, 'Blue Mountain', 'Arabica', "good")
d_cp = drink1.get_company()
d_n = drink1.get_name()
d_p = drink1.price_manage
d_c = drink1.get_country()
d_v = drink1.get_variety()
d_s = drink1.get_smell()

print(d_cp, d_n, '價格', d_p, '元', '產地:', d_c, '品種:', d_v, '味道:', d_s)
