from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.schemas import specialization as schemas


async def get_all_specialization(db: AsyncSession):
    result = await db.execute(text("SELECT * FROM specialization"))
    data = result.fetchall()

    specializations = [
        schemas.Spe(id=row[0], creat_at=row[1], name=row[2]) for row in data
    ]

    return {"data": specializations}
