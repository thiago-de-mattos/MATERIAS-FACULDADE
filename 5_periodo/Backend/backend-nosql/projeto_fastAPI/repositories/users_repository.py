from database import user_collection 
from bson import ObjectId

def create_user(user_dict):
    return user_collection.insert_one(user_dict)

def get_all_users():
    return list(user_collection.find())

def get_user_by_id(user_id):
    return user_collection.find_one({"_id": ObjectId(user_id)})

def update_user(user_id, user_dict):
    return user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user_dict}
    )

def delete_user(user_id):
    return user_collection.delete_one({"_id": ObjectId(user_id)})