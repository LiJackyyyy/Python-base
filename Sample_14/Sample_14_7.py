class DrinkA:
    def size(self):
        return '大杯'


class DrinkB:
    def size(self):
        return '小杯'


a = DrinkA()
print('1.\t', a.size())

b = DrinkB()
print('2.\t', b.size())
