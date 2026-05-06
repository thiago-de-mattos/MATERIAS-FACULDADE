from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from Inseto_repository import InsetoRepository

router = APIRouter(prefix="/insetos", tags=["Insetos"])

@router.post("/")
def create_inseto(inseto: InsetoCreate, db: Session = Depends(get_db)):
    repo = InsetoRepository(db)
    return repo.create(inseto.dict())

@router.get("/")
def list_insetos(db: Session = Depends(get_db)):
    repo = InsetoRepository(db)
    return repo.get_all()

@router.get("/{inseto_id}")
def get_inseto(inseto_id: int, db: Session = Depends(get_db)):
    repo = InsetoRepository(db)
    return repo.get_by_id(inseto_id)

@router.put("/{inseto_id}")
def update_inseto(inseto_id: int, data: dict, db: Session = Depends(get_db)):
    repo = InsetoRepository(db)
    return repo.update(inseto_id, data)

@router.delete("/{inseto_id}")
def delete_inseto(inseto_id: int, db: Session = Depends(get_db)):
    repo = InsetoRepository(db)
    return repo.delete(inseto_id)