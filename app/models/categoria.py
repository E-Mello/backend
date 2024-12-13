# Path: app/models/categoria.py

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from datetime import datetime, timezone

class Categoria(Base):
    __tablename__ = 'categoria'

    id: Mapped[int]  = mapped_column(Integer, primary_key=True, index=True)
    creat_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    name: Mapped[str] = mapped_column(String, nullable=False)
    icon_url: Mapped[str] = mapped_column(String)