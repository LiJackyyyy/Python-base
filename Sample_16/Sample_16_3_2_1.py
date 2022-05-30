import csv

file_a = open('file_name.csv', 'a', newline="")

write_f = csv.writer(file_a)
write_f.writerows([["coffee", 100], ["tea", 90]])

file_a.close()
