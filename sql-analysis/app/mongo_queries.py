import pymongo
import os
from dotenv import load_dotenv
from datetime import datetime




client = pymongo.MongoClient(
    "mongodb://username1:nothingspecial@cluster0-shard-00-00-zig1i.mongodb.net:27017,cluster0-shard-00-01-zig1i.mongodb.net:27017,cluster0-shard-00-02-zig1i.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# load_dotenv()

# DB_USER = os.getenv("MONGO_USER")
# DB_PASSWORD = os.getenv("MONGO_PASSWORD")
# CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME")

# connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
# print("----------------")
# print("URI:", connection_uri)

# client = pymongo.MongoClient(connection_uri)
# print("----------------")
# print("CLIENT:", type(client), client)

db = client.test_database_2
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_collection_2
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400
})

collection.insert_one({
    "name": "Ninetails",
    "level": 42,
    "exp": 70000,
    "hp": 600
})


print("DOCS:", collection.count_documents({})) # SELECT *
print('pika doc:', collection.count_documents({"name": "Pikachu"})) # WHERE with filer condtions
print('LOW EVOL:', collection.count_documents({"level": {"$lt": 31}})) # WHERE with filer condtions

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

# collection.insert_one({"name": "Blastoise", "lvl": 70})
# print("DOCS:", collection.count_documents({}))
# print(collection.count_documents({"name": "Blastoise"}))

# pikas_cursor = collection.find({"name": "Pikachu"})
# for pika in pikas_cursor:
#     print(pika)

new_objects = [
    {"name": "Articuno", "attack": 110},
    {"name": "Zapdos", "attack": 140},
    {"name": "Moltres", "attack": 130},
]
collection.insert_many(new_objects)
print("DOCS:", collection.count_documents({}))

# # which pokemon have an attack greater than 60?
# attackers = collection.find({"attack": {"$gt": 60}})
# for attacker in attackers:
#     print(attacker)