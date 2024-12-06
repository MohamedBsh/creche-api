from fastapi import APIRouter
from creche.db.operations.caregiver import (
    read_all_caregivers,
    read_caregiver,
    create_caregiver,
)
from creche.db.db_interface import DBInterface
from creche.db.models import DBCaregiver
from creche.db.operations.caregiver import CaregiverCreateData

router = APIRouter()


@router.get("/caregivers")
def api_read_all_caregivers():
    caregiver_interface = DBInterface(DBCaregiver)
    return read_all_caregivers(caregiver_interface)


@router.post("/caregivers")
def api_create_caregiver(caregiver: CaregiverCreateData):
    caregiver_interface = DBInterface(DBCaregiver)
    return create_caregiver(caregiver, caregiver_interface)


@router.get("/caregivers/{caregiver_id}")
def api_read_caregiver(caregiver_id: int):
    caregiver_interface = DBInterface(DBCaregiver)
    return read_caregiver(caregiver_id, caregiver_interface)
