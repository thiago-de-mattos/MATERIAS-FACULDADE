from fastapi import APIRouter
from database import carros_collection
from schemas import  Carro

router = APIRouter()

@router.get("/carros")
def list_carros():
    carros = []

    for carro in carros_collection.find():
        carro["_id"] = str(carro["_id"])
        carros.append(carro)

    return carros

@router.post("/carros")
def create_carro(carro: Carro):

    carro_dict = carro.model_dump()
    result = carros_collection.insert_one(carro_dict)
    
    return {
        "message": "carro criado",
        "id": str(result.inserted_id)
    }

@router.get("/carros/{carro_id}")
def get_carro(carro_id: str):
    from bson import ObjectId

    carro = carros_collection.find_one({"_id": ObjectId(carro_id)})

    if carro:
        carro["_id"] = str(carro["_id"])
        return carro
    return {"error": "carro não encontrado"}

@router.delete("/carros/{carro_id}")
def delete_carro(carro_id: str):
    from bson import ObjectId

    result = carros_collection.delete_one({"_id": ObjectId(carro_id)})

    if result.deleted_count == 0:
        return {"error": "carro não encontrado"}
    
    return {"message": "carro deletado com sucesso"}

@router.patch("/carros/{carro_id}")
def update_carro(carro_id: str, data: dict):
    from bson import ObjectId

    result = carros_collection.update_one(
        {"_id": ObjectId(carro_id)},
        {"$set": data}
    )

    if result.matched_count == 0:
        return {"error": "carro não encontrado"}
    
    return {"message": "atualização realizada com sucesso"}