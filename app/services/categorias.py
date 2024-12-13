# app/services/categorias.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.schemas import categorias as schemas

async def get_all_categorias(db: AsyncSession):
    result = await db.execute(text('SELECT * FROM categoria'))
    data = result.fetchall()

    # Convert raw result to Pydantic model (schemas.Category)
    categories = [
        schemas.Category(
            id=row[0],
            name=row[2],
            icon_url=row[3],
            created_at=row[1] 
        )
        for row in data
    ]

    return {"data": categories} 
