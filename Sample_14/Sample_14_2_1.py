class Drink:  #建立類別
    def __init__(self, name, price, discount):  # 此行非函數,建立實體物件時，是在初始化作提供相關的資訊,後執行第15行
        self.name = name  # 語意:把自己的name屬性指定給name
        self.price = price
        self.discount = discount   # 此行非函數,建立實體物件時，是在初始化作提供相關的資訊,後執行第15行

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price, self.price * self.discount


drink1 = Drink('coffee', 100, 0.9)   # 實體物件 = 分類名稱第一字一定要大寫(物件)
n1 = drink1.get_name()
p1, p2 = drink1.get_price()
print(n1, '價格', p1, '元')
