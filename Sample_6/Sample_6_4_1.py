# 錯誤範例 備註: 字串+字串 會變成字串連接
name_1 = input('Please enter first number:')
name_2 = input('Please enter second number:')


total_number = name_1 + name_2

#print
print('總數為:', total_number)
print('-' * 10)
# 正確範例 字串要先型態轉換
name_1 = int(input('Please enter first number:'))
name_2 = int(input('Please enter second number:'))


total_number = name_1 + name_2

#print
print('總數為:', total_number)