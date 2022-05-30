file_a = open('file_name_XXX_2.txt', 'w')

data = ['coffee\t100\n', 'tea\t80\n']
file_a.writelines(data)

file_a.close()
