from fastapi import APIRouter, Depends
from app.services.specialization import get_all_specialization
from app.db.database import get_db
from app.schemas import specialization as schemas

specializations_route = APIRouter()


@specializations_route.get("/specialization", response_model=schemas.SpecializationSchema)
async def get_specialization(db=Depends(get_db)):
    specializations_data = await get_all_specialization(db)
    return specializations_data