from creche.db.engine import DBSession
from creche.db.models import DBCaregiver

def create_caregiver(first_name: str, last_name: str, qualifications: str, years_of_experience: int, caregiver_email_address: str, caregiver_phone_number: str):
    session = DBSession()
    new_caregiver = DBCaregiver(first_name=first_name, last_name=last_name, qualifications=qualifications, years_of_experience=years_of_experience, caregiver_email_address=caregiver_email_address, caregiver_phone_number=caregiver_phone_number)
    session.add(new_caregiver)
    session.commit()
    session.refresh(new_caregiver)
    return new_caregiver

def read_all_caregivers():
    session = DBSession()
    caregivers = session.query(DBCaregiver).all()
    return caregivers

def read_caregiver(id: int):
    session = DBSession()
    caregiver = session.query(DBCaregiver).get(id)
    return caregiver