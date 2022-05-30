class DrinkA:
    def size(self):
        return '大杯'


class DrinkB:
    def size(self):
        return '小杯'


def cup(par):
    return par.size()


a = DrinkA()
print('1.\t', cup(a))

b = DrinkB()
print('2.\t', cup(b))
