n = [4, 9, 16, 25, 36]  # 記憶體位置不同會額外占空間
print('原本:', n)
rev_n = n[::-1]
print('改變數名稱後:rev_n', rev_n)
print(id(n))
print(id(rev_n))


print('-' * 20)
n = [4, 9, 16, 25, 36]
print('原本:', n)
n.reverse()
print('改後', n)
print(id(n))

print('-' * 20)  # reversed()不會占記憶體空間
n = [4, 9, 16, 25, 36]
print('原本:', n)
r_n = reversed(n)
print('改變數名稱後r_n:', r_n)

print('*' * 10)
for i in r_n:
    print(i)
