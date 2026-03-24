from pydantic import BaseModel

class User(BaseModel):
    nome: str
    email: str
    idade: int

class Carro(BaseModel):
    nome: str
    marca: str
    placa: str
    ano: int
    cor: str