score = [99, 98, 87, 78, 56, 87, 87]
print('刪除前的score資料:', score)
remove_data = 100
if remove_data in score:
    score.remove(remove_data)
print('刪除後的score的資料', score)
