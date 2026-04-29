from pydantic import BaseModel
from typing import Optional

#Entrada: criação de uma tarefa
class InsetoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    Ordem: Optional[str] = None

#Saída: Tarefa lida do banco
class InsetoResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str]
    ordem: Optional[str]

class Config:
    from_attributes = True #lê do ORM