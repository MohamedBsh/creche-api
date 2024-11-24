from fastapi import APIRouter, Body
from creche.db.operations.caregiver import read_all_caregivers, read_caregiver, create_caregiver
router = APIRouter()

@router.get("/caregivers")
def api_read_all_caregivers():
    return read_all_caregivers()

@router.post("/caregivers")
def api_create_caregiver(
    first_name: str = Body(...), 
    last_name: str = Body(...), 
    qualifications: str = Body(...), 
    years_of_experience: int = Body(...), 
    caregiver_email_address: str = Body(...), 
    caregiver_phone_number: str = Body(...)
):
    return create_caregiver(first_name=first_name, last_name=last_name, qualifications=qualifications, years_of_experience=years_of_experience, caregiver_email_address=caregiver_email_address, caregiver_phone_number=caregiver_phone_number)

@router.get("/caregivers/{caregiver_id}")
def api_read_caregiver(caregiver_id: int):
    return read_caregiver(caregiver_id)