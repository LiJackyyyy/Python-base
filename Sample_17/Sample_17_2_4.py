import json


def read_json(file_name):
    file_a = open(file_name, 'r')
    info = json.load(file_a)
    return info['table']


try:
    data = read_json("file_name_JJJ.json")
    print(data[1:])

    try:
       table_num = int(input("Please enter table number(1~5):"))
       print(data[table_num])

    except IndexError as error_name:
        print(error_name)
        print("Please enter table number(1~5):")
        print("NO other number")
    except ValueError as error_name:
        print(error_name)
        print("Please enter table number(1~5):")
        print("NO word")

except FileNotFoundError as error_name:
    print(error_name)
    print("Please check your file")
