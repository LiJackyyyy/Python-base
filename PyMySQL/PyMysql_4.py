import mysql.connector
import datetime
connection = mysql.connector.connect(host="localhost",
                                     database="python_mysql_class",
                                     user="root",
                                     password="password")

my_cursor = connection.cursor()

insert_commit = "INSERT INTO drink VALUES(%s, %s, %s, %s, %s, %s)"

data = ("DR005", "西瓜汁", datetime.date(2024, 9, 22), "TW", 70, "飲品")
my_cursor.execute(insert_commit, data)
connection.commit()

try:
    my_cursor.execute(insert_commit,data)
except mysql.connector.InternalError as err_name:
    print("err_name")
else:
    connection.commit()
finally:
    print("program finish")
