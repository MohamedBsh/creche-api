from creche.db.engine import DBSession
from creche.db.models import DBEnrollment, DBChild, DBCaregiver, DBCreche
from datetime import date

class InvalidEnrollmentDates(Exception):
    pass

def create_enrollment(start_date: date, end_date: date, price: int, child_id: int, caregiver_id: int, creche_id: int):
    session = DBSession()

    ## retrieve child, caregiver, and creche from the database
    child = session.query(DBChild).get(child_id)
    caregiver = session.query(DBCaregiver).get(caregiver_id)
    creche = session.query(DBCreche).get(creche_id)
    days = (end_date - start_date).days
    if days <= 0:
        raise InvalidEnrollmentDates("Start date must be before end date")
    enrollment_price = creche.price * days
    new_enrollment = DBEnrollment(start_date=start_date, end_date=end_date, price=enrollment_price, child=child, caregiver=caregiver, creche=creche)
    session.add(new_enrollment)
    session.commit()
    session.refresh(new_enrollment)
    return new_enrollment

def delete_enrollment(id: int):
    session = DBSession()
    enrollment = session.query(DBEnrollment).get(id)
    session.delete(enrollment)
    session.commit()
    return enrollment

def read_all_enrollments():
    session = DBSession()
    enrollments = session.query(DBEnrollment).all()
    return enrollments

def read_enrollment(id: int):
    session = DBSession()
    enrollment = session.query(DBEnrollment).get(id)
    return enrollment

def read_enrollments_by_creche_and_price(creche_id: int, price: int):
    session = DBSession()
    enrollments = session.query(DBEnrollment).filter(DBEnrollment.creche_id == creche_id, DBEnrollment.price == price).all()
    return enrollments

def read_enrollments_by_parent(parent_id: int):
    session = DBSession()
    enrollments = session.query(DBEnrollment).filter(DBEnrollment.parent_id == parent_id).all()
    return enrollments
