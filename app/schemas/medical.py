# app/schemas/medical.py

from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class MedicalBase(BaseModel):
    name: str
    avatar_url: Optional[str] = None
    biography: str
    score: float


class MedicalCreate(MedicalBase):
    pass


class Medical(MedicalBase):
    id: int
    created_at: datetime
    category_id: int

    class Config:
        from_attributes = True


class MedicalList(BaseModel):
    data: List[Medical]


