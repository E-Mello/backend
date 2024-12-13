# app/schemas/categorias.py

from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class CategoryBase(BaseModel):
    name: str
    icon_url: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CategoryList(BaseModel):
    data: List[Category]
