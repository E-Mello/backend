from datetime import datetime
from pydantic import BaseModel
from typing import List


class SpecializationSchema(BaseModel):
    id: int
    name: str
    creat_at: datetime

    class Config:
        from_attributes = True
