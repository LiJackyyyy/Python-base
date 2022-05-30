import csv

file_a = open('file_name.csv', 'w', newline="")

write_f = csv.writer(file_a)
write_f.writerow(['產品名稱'"產品價格"])

file_a.close()