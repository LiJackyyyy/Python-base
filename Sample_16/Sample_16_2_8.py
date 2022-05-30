file_a = open('file_name_XXX.txt', 'a+')
print('1.\t目前讀寫位置:', file_a.tell())
file_a.seek(0)
print('2.\t目前讀寫位置:', file_a.tell())
print('-'*20)
lines = file_a.readlines()
for i in lines:
    print(i, end="")

print('3.\t目前讀寫位置:', file_a.tell())
file_a.write('cake\t 60\n')

file_a.close()
