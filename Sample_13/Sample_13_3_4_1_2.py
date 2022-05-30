def a(q, w, e, p=10, c=5, s=5):  # 引數會優先取代參數
    print('a_q:', q, 'a_w:', w, 'a_e:', e)
    print('停車費', p, end='\t')
    print('清潔費', c, end='\t')
    print('騙錢費', s)
    print('Total', q + w + e + p + c + s)


a(10, 20, 30, c=50)  # 引數優先
