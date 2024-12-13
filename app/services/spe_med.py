#app/services/spe_med.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.schemas import spe_med as schemas


async def get_all_spe_med(db: AsyncSession):
    result = await db.execute(text("SELECT * FROM medical_specialization"))
    data = result.fetchall()

    spe_medical = [schemas.MedicalSpecialization(id=row[0]) for row in data]

    return {"data": spe_medical}