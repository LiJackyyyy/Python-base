import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                     database="python_mysql_class",
                                     user="root",
                                     password="password")

my_cursor = connection.cursor()

delete_commit = "DELETE FROM drink WHERE product_id=%s"

data = "DR005"
my_cursor.execute(delete_commit, (data, ))
connection.commit()
