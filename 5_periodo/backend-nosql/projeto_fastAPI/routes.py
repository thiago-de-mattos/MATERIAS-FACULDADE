from fastapi import APIRouter
from database import users_collection
from schemas import User

router = APIRouter()

@router.get("/users")
def list_users():
    users = []

    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)

    return users

#POST - CREATE USER
@router.post("/users")
def create_user(user: User):

    user_dict = user.model_dump()
    result = users_collection.insert_one(user_dict)
    
    return{
        "message": "user created",
        "id": str(result.inserted_id)
    }

    #GET - USER BY ID
@router.get("/users/{user_id}")
def get_id(user_id: str):
    from bson import ObjectId

    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if user:
        user["_id"] = str(user["_id"])
        return user
    return {"error": "user not found"}

    #Delete

@router.delete("/users/{user_id}")
def delete_id(user_id: str):
    from bson import ObjectId

    user = users_collection.delete_one({"_id": ObjectId(user_id)})

    if not user:
        return {"error": "user not found"}
    return{"delete sucessful"}

@router.patch("/users/{user_id}")
def update_id(user_id: str, data: dict):
    from bson import ObjectId

    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    if result.matched_count == 0:
        return {"error": "user not found"}
    
    return {"message": "update successful"}