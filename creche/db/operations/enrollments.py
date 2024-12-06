from creche.db.models import DBEnrollment
from datetime import date
from pydantic import BaseModel
from creche.db.db_interface import DBInterface
from creche.db.operations.interface import DataObject


class EnrollmentCreateData(BaseModel):
    start_date: date
    end_date: date
    price: int
    child_id: int
    caregiver_id: int
    creche_id: int
    parent_id: int


class InvalidEnrollmentDates(Exception):
    pass


def create_enrollment(
    enrollment_data: EnrollmentCreateData,
    enrollment_interface: DBInterface,
    child_interface: DBInterface,
    caregiver_interface: DBInterface,
    creche_interface: DBInterface,
    parent_interface: DBInterface,
) -> DataObject:
    creche = creche_interface.read_by_id(enrollment_data.creche_id)
    child = child_interface.read_by_id(enrollment_data.child_id)
    caregiver = caregiver_interface.read_by_id(enrollment_data.caregiver_id)
    parent = parent_interface.read_by_id(enrollment_data.parent_id)
    days = (enrollment_data.end_date - enrollment_data.start_date).days
    if days <= 0:
        raise InvalidEnrollmentDates("Start date must be before end date")

    enrollment_dict = {
        "start_date": enrollment_data.start_date,
        "end_date": enrollment_data.end_date,
        "price": creche["price"] * days,
        "child_id": child["id"],
        "caregiver_id": caregiver["id"],
        "creche_id": creche["id"],
        "parent_id": parent["id"],
    }

    return enrollment_interface.create(enrollment_dict)


def delete_enrollment(
    id: int, enrollment_interface: DBInterface
) -> DataObject:
    return enrollment_interface.delete(
        id
    )


def read_all_enrollments(
    enrollment_interface: DBInterface
) -> list[DataObject]:
    return enrollment_interface.read_all()


def read_enrollment(id: int, enrollment_interface: DBInterface) -> DataObject:
    return enrollment_interface.read_by_id(id)


def read_enrollments_by_creche_and_price(
    creche_id: int, price: int, enrollment_interface: DBInterface
) -> list[DataObject]:
    return enrollment_interface.read_all(
        DBEnrollment.creche_id == creche_id, DBEnrollment.price == price
    )


def read_enrollments_by_parent(
    parent_id: int, enrollment_interface: DBInterface
) -> list[DataObject]:
    return enrollment_interface.read_all(DBEnrollment.parent_id == parent_id)
