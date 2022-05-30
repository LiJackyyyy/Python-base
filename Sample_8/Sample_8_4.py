i = 1  # 先後順序外圈執行到縮牌會優先執行完後再執行外圈
while i <= 3:
    j = 1
    while j <=3:
        print('外圈i執行第:', i, '圈,\t內圈j執行第', j, '圈')
        j += 1
    print('-' * 10)
    i += 1
print(' Program end.')
