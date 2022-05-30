from Sample_14_file_name import *

product = Company('India', 'Arabica', '一號店')
p_c = product.get_country()
p_v = product.get_variety()
p_cc = product.get_company()
print(p_c, p_v, p_cc)
print('-' * 30)
product = Origin('India', 'Arabica', '一號店')
p_c = product.get_country()
p_v = product.get_variety()
p_cc = product.get_company()
print(p_c, p_v, p_cc)
