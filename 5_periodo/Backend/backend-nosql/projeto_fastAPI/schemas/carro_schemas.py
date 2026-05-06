from pydantic import BaseModel

class Carro(BaseModel):
    nome: str
    marca: str
    placa: str
    ano: int
    cor: str