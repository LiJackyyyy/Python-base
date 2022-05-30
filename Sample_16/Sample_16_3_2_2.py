import csv

file_a = open('file_name.csv', 'a', newline="")

write_f = csv.writer(file_a)
data = {"juice": 70,"milk": 60}
for i in data:
    write_f.writerow([i, data[i]])

file_a.close()
