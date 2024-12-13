# Path: app/models/specialization.py

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from app.models.base import Base
from app.models.assistentmedspe import medical_specialization_association
from typing import TYPE_CHECKING

# Usar importação condicional apenas para anotação de tipo
if TYPE_CHECKING:
    from app.models.medical import Medical

class Specialization(Base):
    __tablename__ = "specialization"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    creat_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    name: Mapped[str] = mapped_column(String, nullable=False)

    medicals: Mapped[list["Medical"]] = relationship(
        "Medical",
        secondary=medical_specialization_association,
        back_populates="specializations",
    )
