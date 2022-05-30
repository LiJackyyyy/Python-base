# 兩個串列使用不同的資料，就需要建立新的串列，建立新的串列有兩種方式  1. list() or 2. copy()
score_1 = [99, 98, 87, 78, 56]
score_2 = list(score_1)
print('原本的score_1', score_1)
print('原本的score_2', score_2)
score_2[4] = 59.9
print('修改後的score_1:', score_1)
print('修改後的score_2:', score_2)
print('*' * 30)
print('id of score_1:', id(score_1))
print('id of score_2:', id(score_2))


print()
score_1 = [99, 98, 87, 78, 56]
score_2 = score_1.copy()
print('原本的score_1', score_1)
print('原本的score_2', score_2)
score_2[4] = 59.9
print('修改後的score_1:', score_1)
print('修改後的score_2:', score_2)
print('*' * 30)
print('id of score_1:', id(score_1))
print('id of score_2:', id(score_2))
