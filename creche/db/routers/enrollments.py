from fastapi import APIRouter
from creche.db.operations.enrollments import (
    read_all_enrollments,
    read_enrollment,
    create_enrollment,
    delete_enrollment,
    read_enrollments_by_creche_and_price,
    read_enrollments_by_parent,
)
from creche.db.operations.enrollments import EnrollmentCreateData
from creche.db.db_interface import DBInterface
from creche.db.models import DBEnrollment

router = APIRouter()


@router.get("/enrollments")
def api_read_all_enrollments():
    return read_all_enrollments()


@router.post("/enrollments")
def api_create_enrollment(enrollment: EnrollmentCreateData):
    enrollment_interface = DBInterface(DBEnrollment)
    return create_enrollment(enrollment, enrollment_interface)


@router.get("/enrollments/{enrollment_id}")
def api_read_enrollment(enrollment_id: int):
    enrollment_interface = DBInterface(DBEnrollment)
    return read_enrollment(enrollment_id, enrollment_interface)


@router.delete("/enrollments/{enrollment_id}")
def api_delete_enrollment(enrollment_id: int):
    enrollment_interface = DBInterface(DBEnrollment)
    return delete_enrollment(enrollment_id, enrollment_interface)


@router.get("/enrollments/creche/{creche_id}/price/{price}")
def api_read_enrollments_by_creche_and_price(creche_id: int, price: int):
    enrollment_interface = DBInterface(DBEnrollment)
    return read_enrollments_by_creche_and_price(
        creche_id, price, enrollment_interface
    )


@router.get("/enrollments/parent/{parent_id}")
def api_read_enrollments_by_parent(parent_id: int):
    enrollment_interface = DBInterface(DBEnrollment)
    return read_enrollments_by_parent(parent_id, enrollment_interface)
