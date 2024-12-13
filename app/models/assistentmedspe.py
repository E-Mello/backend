# Path: app/models/assistentmedspe.py

from sqlalchemy import ForeignKey, Table, Column
from app.models.base import Base

# Tabela auxiliar (junction table)
medical_specialization_association = Table(
    "medical_specialization",
    Base.metadata,
    Column("medico_id", ForeignKey("medical.id"), primary_key=True),
    Column("specialization_id", ForeignKey("specialization.id"), primary_key=True),
)