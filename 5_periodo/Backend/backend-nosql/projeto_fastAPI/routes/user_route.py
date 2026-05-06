from fastapi import APIRouter
from schemas import User
from services.user_service import *

router = APIRouter()

@router.get("/users")
def list_users():
    return get_all_users_service()

#POST - CREATE USER
@router.post("/users")
def create_user(user: User):
    return create_user_service(user)

#GET - USER BY ID
@router.get("/users/{user_id}")
def get_id(user_id: str):
    return get_user_by_id_service(user_id)

#Delete
@router.delete("/users/{user_id}")
def delete_id(user_id: str):
    return delete_user_service(user_id)
    
@router.patch("/users/{user_id}")
def update_id(user_id: str, data: dict):
    return update_user_service(user_id, user)