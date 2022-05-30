file_a = open('file_name_XXX_3.txt', 'x')
data = ['juice\t80\n', 'milk\t70\n']
file_a.writelines(data)

file_a.close()
