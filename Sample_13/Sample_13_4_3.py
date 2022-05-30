def a(p, q, pd):
    t = p * q
    dt = t * pd
    return t, dt


n = 'coffee'
p = 100
q = 44
pd = 0.9
total, ad = a(p, q, pd)
print('產品:', n, '營業額', total, '打折後營業額', ad)


# d=discount, p= price, n = name, t = total
