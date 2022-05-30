import json


try:
    file_a = open('file_name_JJJ.json', 'r')
except FileNotFoundError as error_name:
    print(error_name)
    print("Please check your file")
else:
    data = json.load(file_a)
    print(data["drink"][0])
    file_a.close()
finally:
    print("----program end -----")