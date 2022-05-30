def a(**kwargs):  # 資料多筆 dictionary在使用 (一定要加兩個星號要參數前)
    print('資料:', kwargs)  # 大多使用kwargs
    print('資料的型態:', type(kwargs))


a(coffee=31, tea=21, juice=54, milk=61)
