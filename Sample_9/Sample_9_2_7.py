num = [31, 21, 54, 61, 56]

for i in num:
    if i > 100:
        print('Number is:', i)
        break
else:
    print('No element bigger than 100.')

print()
print()
num = [31, 21, 110, 61, 56]
for i in num:
    if i > 100:
        print('Number is:', i)
        break
else:
    print('No element bigger than 100.')

print()
print()

num = [31, 21, 110, 61, 56]
i = 0
while i < len(num):
    if num[i] > 100:
        print('Number is:', num[i])
        break
    i += 1
else:
    print('No element bigger than 100.')
