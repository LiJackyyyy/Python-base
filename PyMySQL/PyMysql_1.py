import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                     database="python_mysql_class",
                                     user="root",
                                     password="password")

my_cursor = connection.cursor()

my_cursor.execute("SELECT * FROM drink")
my_result = my_cursor.fetchall()

for x in my_result:
    print(x)
