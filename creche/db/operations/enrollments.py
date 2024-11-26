from creche.db.engine import DBSession
from creche.db.models import DBEnrollment, DBChild, DBCaregiver, DBCreche, to_dict
from datetime import date
from pydantic import BaseModel

class EnrollmentCreateData(BaseModel):
    start_date: date
    end_date: date
    price: int
    child_id: int
    caregiver_id: int
    creche_id: int

class InvalidEnrollmentDates(Exception):
    pass

def create_enrollment(enrollment_data: EnrollmentCreateData):
    session = DBSession()
    ## retrieve child, caregiver, and creche from the database
    child = session.query(DBChild).get(enrollment_data.child_id)
    caregiver = session.query(DBCaregiver).get(enrollment_data.caregiver_id)
    creche = session.query(DBCreche).get(enrollment_data.creche_id)
    days = (enrollment_data.end_date - enrollment_data.start_date).days
    if days <= 0:
        raise InvalidEnrollmentDates("Start date must be before end date")

    enrollment_dict = enrollment_data.model_dump()
    enrollment_price = creche.price * days
    enrollment_dict["price"] = enrollment_price
    enrollment_dict["child"] = child
    enrollment_dict["caregiver"] = caregiver
    enrollment_dict["creche"] = creche

    new_enrollment = DBEnrollment(**enrollment_dict)
    session.add(new_enrollment)
    session.commit()
    return enrollment_dict.model_dump()


def delete_enrollment(id: int):
    session = DBSession()
    enrollment = session.query(DBEnrollment).get(id)
    session.delete(enrollment)
    session.commit()
    return enrollment

def read_all_enrollments():
    session = DBSession()
    enrollments = list[DBEnrollment] = session.query(DBEnrollment).all()
    return enrollments.model_dump()

def read_enrollment(id: int):
    session = DBSession()
    enrollment = session.query(DBEnrollment).get(id)
    return enrollment.model_dump()

def read_enrollments_by_creche_and_price(creche_id: int, price: int):
    session = DBSession()
    enrollments = session.query(DBEnrollment).filter(DBEnrollment.creche_id == creche_id, DBEnrollment.price == price).all()
    return enrollments.model_dump()

def read_enrollments_by_parent(parent_id: int):
    session = DBSession()
    enrollments = session.query(DBEnrollment).filter(DBEnrollment.parent_id == parent_id).all()
    return enrollments.model_dump()
