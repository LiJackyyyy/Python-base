import json


def read_json(file_name):
    file_a = open(file_name, 'r')
    info = json.load(file_a)
    return info['table']


class MyNameIsException(BaseException):
    def __init__(self, num, message):
        self.num= num
        self.message = message

    def __str__(self):
        return self.num + "\t" + self.message

try:
    data = read_json("file_name_JJJ.json")
    print(data[1:])

    try:
       table_num = int(input("Please enter table number(1~5):"))
       if table_num not in ["1", "2", "3", "4", "5"]:
           raise MyNameIsException(table_num, "is not 1~5")
       print(data[int(table_num)])

    except MyNameIsException as error_name:
        print(error_name)
except FileNotFoundError as error_name:
    print(error_name)
    print('Pleas check your file')

