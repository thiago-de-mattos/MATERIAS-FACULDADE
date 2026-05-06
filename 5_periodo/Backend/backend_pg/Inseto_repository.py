from sqlalchemy.orm import Session
from models import Insetos

class InsetoRepository:
    
    def __init__(self, db: Session):
        self.db = db

    def create(self, inseto: dict):
        db_inseto = Insetos(**inseto)
        self.db.add(db_inseto)
        self.db.commit()
        self.db.refresh(db_inseto)
        return db_inseto

    def get_all(self):
        return self.db.query(Insetos).all()

    def get_by_id(self, inseto_id: int):
        return self.db.query(Insetos).filter(Insetos.id == inseto_id).first()

    def update(self, inseto_id: int, data: dict):
        inseto = self.get_by_id(inseto_id)

        if not inseto:
            return None

        for key, value in data.items():
            setattr(inseto, key, value)

        self.db.commit()
        self.db.refresh(inseto)
        return inseto

    def delete(self, inseto_id: int):
        inseto = self.get_by_id(inseto_id)

        if not inseto:
            return None

        self.db.delete(inseto)
        self.db.commit()
        return inseto