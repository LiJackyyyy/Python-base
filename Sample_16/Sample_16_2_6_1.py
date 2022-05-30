file_a = open('file_name_XXX_4.txt', 'w+')


print('1.\t目前讀寫位置:', file_a.tell())
data = ['juice\t 80\n', 'milk\t 70\n']
file_a.writelines(data)
print('2.\t目前讀寫位置:', file_a.tell())
file_a.seek(0)
print('3.\t目前讀寫位置:', file_a.tell())
lines = file_a.readlines()
for i in lines:
    j = i.split()
    print('飲品:{0[0]:^8}價格為:{0[1]}'.format(j))
print('4.\t目前讀寫位置:', file_a.tell())
file_a.close()
