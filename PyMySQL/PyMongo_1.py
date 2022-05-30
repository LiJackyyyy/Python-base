from pymongo import MongoClient
import pymongo

connection = MongoClient(host="localhost", port=27017)
db = connection.Drink_dbname
collection = db["Drink_collection_name"]
print("collection", collection)

data = {"_id" : 12345,
        "drink": [{"hot": {"coffee": 100, "tea": 90}},
                  {"juice": {"apple": 95, "banana": 85}}],
        "table": ["", "A01", "A03", "A04", " A05"]}


try:
    result = collection.insert_one(data)
    print("已新增", data)
except pymongo.errors.DuplicateKeyError as err_name:
    print(err_name)
    print("已存在地址_id", data["_id"], "(因此不寫入)")
