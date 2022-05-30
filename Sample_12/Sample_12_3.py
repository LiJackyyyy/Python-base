a = {'aa', 'bb', 'cc', 'dd', 'ee'}
b = {'aa', 'bb', 'cc', 'rr', 'yy'}
print('1.\t:', a & b)  # 交集 有重複的
print('2.\t', a | b)   # 聯集 全部集合不會重複
print('3.\t', a - b)   # 差集 a - b 有的出現a有的
print('4.\t', b - a)   # 差集 b - a 有的出現b有的
print('5.\t', a ^ b)   # 對稱差集 出現沒有重複的
