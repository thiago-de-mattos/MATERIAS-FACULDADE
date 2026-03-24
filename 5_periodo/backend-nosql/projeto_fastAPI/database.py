from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27018"

client = MongoClient(MONGO_URL)

db = client["aula_nosql"]

users_collection = db["users"]

carros_collection = db["carros"]