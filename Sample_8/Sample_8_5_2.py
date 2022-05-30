stop_condition = int(input('請輸入要做到第幾迴圈時要跳出迴圈:(1~8):'))

for i in range(1, 8+1, 1):
    print('目前做到第', i, '圈', end='\t')  # end='\t' 代表此行最後一字強制換行
    if i == stop_condition:
        print()  # 此行代表換行 print()預設是換行
        continue
    print('Do something process.')

print()# 此行代表換行 print()預設是換行
print('Program end.')
