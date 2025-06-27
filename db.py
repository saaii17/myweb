from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['event_management']
users_collection = db['users']
