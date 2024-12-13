#app/routes/spe_med.py

from fastapi import APIRouter, Depends
from app.services.spe_med import get_all_spe_med
from app.db.database import get_db
from app.schemas import spe_med as schemas

spe_medical_route = APIRouter()

@spe_medical_route.get("/spe_med", response_model=schemas.MedicalSpecializationList)
async def get_spe_med(db=Depends(get_db)):
    spe_medical_data = await get_all_spe_med(db)
    return spe_medical_data