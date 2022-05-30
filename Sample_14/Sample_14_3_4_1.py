class Drink:  #建立類別
    count = 0

    def __init__(self, name, price, discount):  # 此行非函數,建立實體物件時，是在初始化作提供相關的資訊,後執行第15行
        Drink.count = Drink.count + 1
        self.name = name  # 語意:把自己的name屬性指定給name
        self.price = price
        self.discount = discount   # 此行非函數,建立實體物件時，是在初始化作提供相關的資訊

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price, self.price * self.discount

    @classmethod
    def get_count(cls):
        return cls.count


drink1 = Drink('coffee', 100, 0.9)   # 實體物件 = 分類名稱第一字一定要大寫(物件)
n1 = drink1.get_name()
p1, pd1 = drink1.get_price()
print(n1, '價格', p1, '元', '打折後:', pd1)

drink2 = Drink('tea', 80, 0.9)
n_2 = drink2.get_name()
p2, pd2 = drink2.get_price()
print(n_2, '價格', p2, '元', '打折後:', pd2)

print('合計為:', Drink.get_count(), '杯')
