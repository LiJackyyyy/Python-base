# # 1.     函數的練習-power
# # 寫一函數power(x, n)用來計算x的n次方。
# # 說明：power (5,3)即計算5^3。
# # def power(x, y):
# #     reslut =x ** y
# #     print(reslut)
# #
# #
# # x = 5
# # y = 3
# # power(x, y)
#
# # 2.     函數的練習-is_prime
# # 寫一函數is_prime(n)用來判斷n是否為質數。
# # def is_prime(num):
# #     for i in range(2, num):
# #         if num % i != 0:
# #             return print("質數")
# #         elif num % i == 0:
# #             return print("不是質數")
# #
# #
# # a = int(input("輸入一整數:"))
# # is_prime(a)
#
#
# # 3.     函數的練習-prime
# # 寫一函數get_prime (n)用來找出第n個質數。
# def get_prime(num):
#     li = []
#     n = 1
#     while num != len(li):
#         n += 1
#         x = 0
#         for i in range(2, n):
#             if n % i != 0:
#                 x += 1
#
#         if x == n-2:
#             li.append(n)
#     print(li)
#
#
# num = int(input("輸入第幾個質數"))
# get_prime(num)
#
#
# # 4.     函數的練習-mersenne_prime
# # 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
# # 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
# # 說明：當p=3時，2^3-1=7，故7為Mersenne Prime。
# def is_mersenne_prime(n):
#     li = []
#     n = 1
#     P = 1
#     while len(li) < 5:
#         n += 1
#         x = 0
#         for i in range(2, n):
#             if n % i != 0:
#                 x += 1
#
#         if x == n-2:
#             while True:
#                 if 2 ** P - 1 == n:
#                     li.append(n)
#                     break
#                 elif 2 ** P - 1 < n:
#                     P += 1
#                 else:
#                     break
#
#
#     print(li)
#
#
# n = int(input("輸入一數值確認是否為Mersenne質數:"))
# is_mersenne_prime(n)
# 5.     遞迴函數的練習-factorial_recursive
# 寫一遞迴函數factorial (n)用來計算1*2*3*…*n的值。
# 提示：factorial (n) = n * factorial(n-1)，factorial(1)=1
# def factorial(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return n * factorial(n-1)
#
#
#
#
# n =int(input("輸入一數:"))
# ans = factorial(n)
# print(ans)
