file_a = open('file_name_XXX.txt', 'r')
data = file_a.readlines()
print('data', data)
for i in data:
    print(i, end="")

file_a.close()
