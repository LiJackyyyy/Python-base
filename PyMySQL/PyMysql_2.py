import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                     database="python_mysql_class",
                                     user="root",
                                     password="password")

my_cursor = connection.cursor()

insert_commit = "INSERT INTO drink VALUES(%s, %s, %s, %s, %s, %s)"

data = ("DR005", "西瓜汁", None, "TW", 70, "飲品")
my_cursor.execute(insert_commit, data)
connection.commit()
