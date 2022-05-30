file_a = open('file_name_XXX.txt', 'r+')

lines = file_a.readlines()
for i in lines:
    print(i, end="")
data = ['water\t 80\n', 'milktea\t 70\n']
file_a.writelines(data)

file_a.close()
