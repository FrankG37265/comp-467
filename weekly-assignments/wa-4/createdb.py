import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mlb"]
mycol = mydb["goats"]
mydict = {"name": "Aaron Judge", "address": "Tinsman Avenue"}

x = mycol.insert_one(mydict)

print(f"Collection names: {mydb.list_collection_names()}")
print(f"Database names: {myclient.list_database_names()}")
print(f"Inserted document ID: {x.inserted_id}")