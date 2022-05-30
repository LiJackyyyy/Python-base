def a(p, q, pd):
    t = p * q
    dt = t * pd
    return t, dt  # 回傳出去這裡


n = 'coffee'
p = 100
q = 44
pd = 0.9
t_o = a # 指定為函數
print(type(t_o))
total, ad = t_o(p, q, pd)  # 回傳回來的變數為
print('產品:', n, '營業額', total, '打折後營業額', ad)

