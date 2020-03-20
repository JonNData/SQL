import pymongo
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

DB_USER = os.getenv("MONGO_USER")
DB_PASSWORD = os.getenv("MONGO_PASSWORD")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

# client = pymongo.MongoClient(connection_uri)
# print("----------------")
# print("CLIENT:", type(client), client)