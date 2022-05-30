#當修改其中一個串列的資料時，另一個串列也會同時修改

score_1 = [99, 98, 87, 78, 56]
score_2 = score_1
print('原本的score_1', score_1)
print('原本的score_2', score_2)
score_2[4] = 59.9
print('修改後的score_1:', score_1)
print('修改後的score_2:', score_2)
print('*' * 30)
print('id of score_1:', id(score_1))
print('id of score_2:', id(score_2))
#~ id() 用來查看該變數在記憶體的位置