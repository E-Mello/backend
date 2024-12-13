# app/schemas/spe_med.py

from pydantic import BaseModel
from typing import List


class MedicalSpecializationBase(BaseModel):
    pass


class MedicalSpecializationCreate(MedicalSpecializationBase):
    pass


class MedicalSpecialization(MedicalSpecializationBase):
    id: int

    class Config:
        from_attributes = True


class MedicalSpecializationList(BaseModel):
    data: List[MedicalSpecialization]
