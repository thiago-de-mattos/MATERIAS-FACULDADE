from datetime import datetime

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    estoque: int    
    
class ProdutoResponse(ProdutoCreate):
    id: int
    
    class Config:
        orm_mode = True
        
class ItemCreate(BaseModel):
    produto_id: str
    quantidade: int = 1
    
class ItemResponse(ItemCreate):
    produto: ProdutoResponse
    quantidade: int
    
    class Config:
        orm_mode = True

class pedidoCreate(BaseModel):
    usuario_id: int
    itens: List[ItemCreate]
    
class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    criado_em: datetime
    status: str
    itens: List[ItemResponse]
    
    class Config:
       from_attributes = True

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    
class UsuarioResponse(UsuarioCreate):
    
    id: int
    ativo: bool
    pedidos: list[PedidoResponse] = []
    
    class Config:
        orm_mode = True