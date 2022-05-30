import json


try:
    file_a = open('file_name_JJJ.json', 'r')
    data = json.load(file_a)
    print(data["drink"][0])
    file_a.close()
except FileNotFoundError as error_name:
    print(error_name)
    print("Please check your file")
