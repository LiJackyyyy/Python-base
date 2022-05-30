import Sample_14_file_name as Sfn


product = Sfn.Company('India', 'Arabica', '一號店')
p_c = product.get_country()
p_v = product.get_variety()
p_cc = product.get_company()
print(p_c, p_v, p_cc)
