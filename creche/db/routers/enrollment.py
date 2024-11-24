from fastapi import APIRouter, Body
from creche.db.operations.enrollment import read_all_enrollments, read_enrollment, create_enrollment, delete_enrollment, read_enrollments_by_creche_and_price
from datetime import date
router = APIRouter()

@router.get("/enrollments")
def api_read_all_enrollments():
    return read_all_enrollments()

@router.post("/enrollments")
def api_create_enrollment(
    start_date: date = Body(...), 
    end_date: date = Body(...),  
    child_id: int = Body(...), 
    caregiver_id: int = Body(...),
    creche_id: int = Body(...),
    price: int = Body(...)

):  
    return create_enrollment(start_date=start_date, end_date=end_date, child_id=child_id, caregiver_id=caregiver_id, creche_id=creche_id, price=price)

@router.get("/enrollments/{enrollment_id}")
def api_read_enrollment(enrollment_id: int):
    return read_enrollment(enrollment_id)

@router.delete("/enrollments/{enrollment_id}")
def api_delete_enrollment(enrollment_id: int):
    return delete_enrollment(enrollment_id)

@router.get("/enrollments/creche/{creche_id}/price/{price}")
def api_read_enrollments_by_creche_and_price(creche_id: int, price: int):
    return read_enrollments_by_creche_and_price(creche_id, price)