class Origin:

    def __init__(self, country, variety, company):
        self.country = country
        self.variety = variety
        self.company = company

    def get_country(self):
        return '產地:' + self.country

    def get_variety(self):
        return '品種:' + self.variety

    def get_company(self):
        return '銷售公司' + self.company


class Company(Origin):
    def __init__(self, country, variety, company):
        super().__init__(country, variety, company)

    def get_company(self):
        return '銷售分店' + self.company


product = Company('India', 'Arabica', '一號店')
p_c = product.get_country()
p_v = product.get_variety()
p_o = product.get_company()
print(p_c, p_v, p_o)
