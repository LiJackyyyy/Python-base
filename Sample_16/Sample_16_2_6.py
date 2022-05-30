file_a = open('file_name_XXX_4.txt', 'w+')
data = ['juice\t80\n', 'milk\t70\n']
file_a.writelines(data)
file_a.seek(0)
lines = file_a.readlines()
for i in lines:
    j = i.split()
    print("j", j)
    print('飲品:{0[0]:^8}價格為:{0[1]}'.format(j))
file_a.close()
