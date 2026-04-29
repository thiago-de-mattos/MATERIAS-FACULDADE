from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from database import Base

class Insetos(Base):
    __tablename__ = "insetos"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    nome: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    descricao: Mapped[str] = mapped_column(
        String(300), nullable=True
    )
    Ordem: Mapped[str] = mapped_column(
        String(300), nullable=True
    )