score = [99, 98, 87, 78, 56]

print('變更前的score資料:', score)
score.append(100) # 串列的尾端加入新的值
print('變更後的score資料:', score)

print()

score = [99, 98, 87, 78, 56]

print('變更前的score資料:', score)
score.insert(2,100)  # 指定的位置插入值,被插隊的值會順勢往後排
print('變更後的score資料:', score)

print()
score = [99, 98, 87, 78, 56]

print('變更前的score資料:', score)
del score[2]  # 以索引值為刪除依據
print('變更後的score資料:', score)

print()
print()
score = [99, 98, 87, 78, 56,87,87]

print('變更前的score資料:', score)
score .remove(87)  # 刪除指定的值，只有最左邊的刪除
print('變更後的score資料:', score)

print()
score = [99, 98, 87, 78, 56,87,87]

print('變更前的score資料:', score)
score .remove(87)  # 刪除指定的值，只有最左邊的刪除
print('變更後的score資料:', score)