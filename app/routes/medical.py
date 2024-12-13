# app/routes/medical.py


from app.schemas import medical as schemas
from fastapi import APIRouter, Depends
from app.services.medical import get_all_medical, get_doctor_by_name
from app.db.database import get_db


route = APIRouter()


@route.get("/medical/{medical_name}")
async def get_medical_details(medical_name: str, db=Depends(get_db)):
    doctor = await get_doctor_by_name(db=db, medical_name=medical_name)
    return doctor


@route.get("/medical", response_model=schemas.MedicalList)
async def get_medical(db=Depends(get_db)):
    medical_data = await get_all_medical(db)
    return medical_data
