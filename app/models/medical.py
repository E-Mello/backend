# Path: app/models/medical.py

from datetime import datetime, timezone
from sqlalchemy import Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.models.base import Base
from app.models.assistentmedspe import medical_specialization_association
from typing import TYPE_CHECKING, List

# Usar importação condicional apenas para anotação de tipo
if TYPE_CHECKING:
    from app.models.specialization import Specialization
    from app.models.categoria import Categoria  # Importando a categoria

class Medical(Base):
    __tablename__ = "medical"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    avatar_url: Mapped[str] = mapped_column(String, nullable=True)
    score: Mapped[float] = mapped_column(Float, nullable=False)
    biography: Mapped[str] = mapped_column(String, nullable=False)

    # Adicionando a relação com a categoria
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categoria.id"))
    category: Mapped["Categoria"] = relationship("Categoria", back_populates="medicals")

    specializations: Mapped[List["Specialization"]] = relationship(
        "Specialization",
        secondary=medical_specialization_association,
        back_populates="medicals",
    )
