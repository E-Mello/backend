# app/routes/categories.py

from fastapi import APIRouter, Depends
from app.services.categorias import get_all_categorias
from app.db.database import get_db
from app.schemas import categorias as schemas

categories_route = APIRouter()

@categories_route.get("/categorias", response_model=schemas.CategoryList)
async def get_categorias(db=Depends(get_db)):
    categories_data = await get_all_categorias(db)
    return categories_data