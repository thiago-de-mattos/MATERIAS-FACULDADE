from sqlalchemy.orm import mapped, mapped_column, relationship
from sqlalchemy import  String, Integer, Float, Boolean, Foreignkey, Datetime
from datetime import datetime
from database import Base

class Usuario(base):
    __tablename_ = "usuarios"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Maped[str] = mapped_column(String(100)) 
    email: Maped[str] = mapped_column(String(200)) 
    ativo: Maped[bool] = mapped_column(Boolean default=True) 
    
    pedidos: Mapped[List["Pedido"]] = relationship("Pedido", back_populates="usuario")
    
class Pedido(Base):
    __tablename__ = "pedidos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"))
    criado_em: Mapped[datetime] = mapped_column(Datetime, default=datetime.utcnow)
    status: Mapped[str] = mapped_column(String(50), default="Pendente")
    
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="pedidos")
    
    itens: Mapped[ist["PedidoItem"]] = relationship("PedidoItem", back_populates="pedido", cascade="all, delete-orphan")
    
class PedidoItem(Base):
    __tablename__ = "pedido_itens"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pedido_id: Mapped[int] = mapped_column(Integer, ForeignKey("pedidos.id"))
    produto_id: Mapped[str] = mapped_column(String(100))
    quantidade: Mapped[int] = mapped_column(Integer, default=1)
    
    pedido: Mapped["Pedido"] = relationship("Pedido", back_populates="itens")
    produto: Mapped["Produto"] = relationship("Produto")