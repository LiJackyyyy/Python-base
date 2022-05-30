def a_1000():
    print('領1000')
def a_2000():
    print('領3000')
def a_3000():
    print('領5000')


a = [a_1000, a_2000, a_3000]
print('1.領1000\n2.領3000\n3.領5000\n')

ans = int(input('輸入操作編號 (1~3):')) - 1

if 0 <= ans <= 2:
    a[ans]()
else:
    print('輸入錯誤')

