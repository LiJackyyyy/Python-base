def a(*args):  # 資料多筆,list,tuple,set在使用 (一定要加星號要參數前)
    print('資料:', args)  # 大多使用args
    print('資料的型態:', type(args))


a(31, 21, 54, 61)

