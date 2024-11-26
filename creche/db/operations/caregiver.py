from creche.db.engine import DBSession
from creche.db.models import DBCaregiver
from pydantic import BaseModel

class CaregiverCreateData(BaseModel):
    first_name: str
    last_name: str
    qualifications: str
    years_of_experience: int
    caregiver_email_address: str
    caregiver_phone_number: str

def create_caregiver(caregiver_data: CaregiverCreateData):
    session = DBSession()
    new_caregiver = DBCaregiver(**caregiver_data.model_dump())
    session.add(new_caregiver)
    session.commit()
    return new_caregiver

def read_all_caregivers():
    session = DBSession()
    caregivers = session.query(DBCaregiver).all()
    return caregivers

def read_caregiver(id: int):
    session = DBSession()
    caregiver = session.query(DBCaregiver).get(id)
    return caregiver