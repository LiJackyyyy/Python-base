from pymongo import MongoClient
import pymongo

connection = MongoClient(host="localhost", port=27017)
db = connection.Drink_dbname
collection = db["Drink_collection_name"]
print("collection", collection)

id_name = 12345
my_query = {'_id': id_name}
data = list(collection.find(my_query))
print("data=", data)
print("type(data)", type(data))
