# Data input from keyboard
product_name = input('Please enter product name:')
product_price = int(input('Please enter product price:'))
sale_nuber = int(input('Please enter quantity:'))

# Calculate
total_price = product_price * sale_nuber

# print to screen
print(product_name, '\t價格:',product_price, '元/單位')
print('銷售數量:', sale_nuber)
print('總金額:', total_price)
