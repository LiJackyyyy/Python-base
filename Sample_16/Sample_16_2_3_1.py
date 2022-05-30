file_a = open('file_name_XXX.txt', 'r')
data = file_a.readlines()
print('data', data)
for i in data:
    print(i)
    j = i.split()
    print(j)
    print('飲品:{0[0]:^8}價格為:{0[1]}'.format(j))

file_a.close()
